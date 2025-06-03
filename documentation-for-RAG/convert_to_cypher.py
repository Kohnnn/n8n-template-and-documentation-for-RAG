from typing import Dict, List
import json
import os
from datetime import datetime

class CypherGenerator:
    def convert_entities_to_cypher(self, entities: List[Dict]) -> str:
        """Convert entities to a direct Cypher query."""
        queries = []
        for entity in entities:
            query = f"""
CREATE (n:Entity {{
    name: "{entity['name']}",
    description: "{entity['description']}"
}})"""
            queries.append(query)
        return ';\n'.join(queries)

    def convert_relationships_to_cypher(self, relationships: List[Dict]) -> str:
        """Convert relationships to a direct Cypher query."""
        queries = []
        for rel in relationships:
            query = f"""
MATCH (e1:Entity {{name: "{rel['entity1']['name']}"}})
MATCH (e2:Entity {{name: "{rel['entity2']['name']}"}})
CREATE (e1)-[r:RELATES_TO {{
    type: "{rel['relation_type']}",
    description: "{rel['description']}"
}}]->(e2)"""
            queries.append(query)
        return ';\n'.join(queries)

    def save_cypher_to_file(self, final_query: str):
        """Save the Cypher query to a file."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"neo4j_query_{timestamp}.cypher"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(final_query)
        
        print(f"Cypher query has been saved to: {filename}")

    def process_json(self, json_data: str) -> None:
        """Process JSON data and generate Cypher query."""
        if isinstance(json_data, str):
            try:
                data = json.loads(json_data)
            except json.JSONDecodeError as e:
                raise Exception(f"Error parsing JSON: {e}")
        else:
            data = json_data

        all_queries = []

        for item in data:
            if item.get("error", False):
                continue

            if "entities" in item:
                entity_query = self.convert_entities_to_cypher(item["entities"])
                all_queries.append(entity_query)

            if "relationships" in item:
                rel_query = self.convert_relationships_to_cypher(item["relationships"])
                all_queries.append(rel_query)

        # Combine all queries with semicolons and proper line breaks
        final_query = ';\n'.join(all_queries) + ';'
        
        # Save to file
        self.save_cypher_to_file(final_query)

def load_json_file(file_path: str) -> dict:
    """Load JSON data from a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        raise Exception(f"Error: The file {file_path} was not found.")
    except json.JSONDecodeError as e:
        raise Exception(f"Error: Invalid JSON in file {file_path}: {str(e)}")
    except Exception as e:
        raise Exception(f"Error reading file {file_path}: {str(e)}")

def main():
    # Get the current directory and construct the file path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(current_dir, "kb_result.json")

    try:
        # Load the JSON data from file
        json_data = load_json_file(json_file_path)
        
        # Generate Cypher queries
        generator = CypherGenerator()
        generator.process_json(json_data)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()