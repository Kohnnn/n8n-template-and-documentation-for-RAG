#!/usr/bin/env python3
import os
import json
import re
import glob

def find_json_files(base_dir):
    """Find all JSON files in the given directory and its subdirectories."""
    pattern = os.path.join(base_dir, "**", "*.json")
    return glob.glob(pattern, recursive=True)

def is_api_key(value):
    """Check if a string looks like an API key."""
    if not isinstance(value, str):
        return False
    
    # Common API key patterns
    patterns = [
        r'[a-zA-Z0-9]{32,}',  # Long alphanumeric strings (32+ chars)
        r'key-[a-zA-Z0-9]+',  # key-prefixed
        r'sk-[a-zA-Z0-9]+',   # OpenAI style
        r'SG\.[a-zA-Z0-9_-]+', # SendGrid style
        r'[a-zA-Z0-9]{8}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{12}', # UUID style
        r'bearer [a-zA-Z0-9]+', # Bearer token style
        r'tvly-[a-zA-Z0-9-]+', # Tavily style
        r'xi-[a-zA-Z0-9-]+',   # Eleven Labs style
    ]
    
    for pattern in patterns:
        if re.search(pattern, value, re.IGNORECASE):
            return True
            
    # Keywords that suggest this might be an API key field
    keywords = ['api_key', 'apikey', 'token', 'secret', 'password', 'credential']
    
    for keyword in keywords:
        if keyword in value.lower():
            return True
            
    return False

def redact_string_values(obj, path=""):
    """Recursively scan JSON objects and redact API keys and sensitive data."""
    if isinstance(obj, dict):
        for key, value in list(obj.items()):
            current_path = f"{path}.{key}" if path else key
            
            # Check for credential objects
            if key == "credentials" and isinstance(value, dict):
                # Preserve credential structure but remove actual values
                for cred_key in value:
                    if isinstance(value[cred_key], dict) and "id" in value[cred_key] and "name" in value[cred_key]:
                        value[cred_key]["id"] = "REDACTED_ID"
            
            # For values that might contain JSON strings (like in parameters, jsonBody, etc.)
            elif isinstance(value, str) and ('{' in value and '}' in value) and ('"api_key":' in value or '"apiKey":' in value):
                try:
                    # Try to parse as JSON
                    json_value = json.loads(value)
                    # Check if it's a dictionary that might contain API keys
                    if isinstance(json_value, dict):
                        # Redact potential API keys in embedded JSON
                        redacted_json = redact_string_values(json_value, current_path)
                        obj[key] = json.dumps(redacted_json)
                except (json.JSONDecodeError, TypeError):
                    # If it's not valid JSON but still looks like an API key
                    if is_api_key(value):
                        obj[key] = "REDACTED_API_KEY"
            
            # For normal string values that look like API keys
            elif isinstance(value, str) and is_api_key(value):
                obj[key] = "REDACTED_API_KEY"
            
            # For specific key names that are likely to contain sensitive data
            elif key.lower() in ["api_key", "apikey", "token", "secret", "password", "key", "xi-api-key"] and isinstance(value, str):
                obj[key] = "REDACTED"
            
            # For specific field names in URL parameters
            elif key.lower() == "url" and isinstance(value, str) and "api_key=" in value:
                obj[key] = re.sub(r'(api_key=)[^&]+', r'\1REDACTED', value)
            
            # Continue recursion
            elif isinstance(value, (dict, list)):
                redact_string_values(value, current_path)
    
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            redact_string_values(item, f"{path}[{i}]")
    
    return obj

def process_file(filepath):
    """Process a single JSON file to remove API keys."""
    print(f"Processing {filepath}...")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Redact sensitive information
        redacted_data = redact_string_values(data)
        
        # Save the redacted file
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(redacted_data, f, indent=2)
        
        print(f"✓ Successfully processed {filepath}")
    except Exception as e:
        print(f"× Error processing {filepath}: {str(e)}")

def main():
    base_dir = "Real Case Example (Credit to @imgroup)"
    json_files = find_json_files(base_dir)
    
    print(f"Found {len(json_files)} JSON files to process")
    
    for file in json_files:
        process_file(file)
    
    print("Done! All API keys have been removed.")

if __name__ == "__main__":
    main() 