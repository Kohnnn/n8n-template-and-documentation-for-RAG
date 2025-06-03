# PowerShell script to merge markdown files
$inputDir = Split-Path -Parent $PSScriptRoot
$outputFile = Join-Path -Path $PSScriptRoot -ChildPath "merged_n8n_docs.md"

# Create output file with initial header
"# n8n Documentation`n" | Out-File $outputFile -Encoding utf8

# Define categories for grouping files
$categories = @{
    "General" = @()
    "Integrations" = @()
    "Integration App Nodes" = @()
    "Learning" = @()
    "Advanced" = @()
    "Release Notes" = @()
    "Other" = @()
}

# Get all markdown files (excluding the merged file)
$mdFiles = Get-ChildItem -Path $inputDir -Filter *.md | Where-Object { $_.Name -ne "merged_n8n_docs.md" }

# Categorize files
foreach ($file in $mdFiles) {
    $fileName = $file.Name
    
    if ($fileName -match "integrations.*app-nodes") {
        $categories["Integration App Nodes"] += $file.FullName
    }
    elseif ($fileName -match "integrations") {
        $categories["Integrations"] += $file.FullName
    }
    elseif ($fileName -match "learning|video") {
        $categories["Learning"] += $file.FullName
    }
    elseif ($fileName -match "advanced|ai") {
        $categories["Advanced"] += $file.FullName
    }
    elseif ($fileName -match "release") {
        $categories["Release Notes"] += $file.FullName
    }
    else {
        $categories["Other"] += $file.FullName
    }
}

# Debug output
Write-Host "Found files by category:"
foreach ($category in $categories.Keys) {
    Write-Host "$category`: $($categories[$category].Count) files"
}

# Process each category
foreach ($category in $categories.Keys | Sort-Object) {
    if ($categories[$category].Count -eq 0) { continue }
    
    # Add category header
    "`n## $category`n" | Out-File $outputFile -Append -Encoding utf8
    
    # Process each file in category
    foreach ($filePath in $categories[$category] | Sort-Object) {
        try {
            Write-Host "Processing file: $filePath"
            $content = Get-Content -Path $filePath -Raw -ErrorAction Stop
            
            # Extract frontmatter
            if ($content -match "(?ms)^---\r?\n(.*?)\r?\n---\r?\n") {
                $frontmatter = $Matches[1]
                
                # Extract title and URL
                $title = if ($frontmatter -match 'title:\s*"(.*?)"') { $Matches[1] } else { "Untitled" }
                $url = if ($frontmatter -match 'url:\s*"(.*?)"') { $Matches[1] } else { "#" }
                
                # Remove frontmatter
                $content = $content -replace "(?ms)^---\r?\n.*?\r?\n---\r?\n", ""
                
                # Remove boilerplate content
                $content = $content -replace '\[Skip to content\]\(.*?\)\r?\n*', ''
                $content = $content -replace '\[Edit this page\]\(.*?\)\r?\n*', ''
                $content = $content -replace '(?ms)Was this page helpful\?.*?Back to top', ''
                $content = $content -replace 'Version: .*?\r?\n', ''
                $content = $content -replace 'On this page.*?\r?\n', ''
                
                # Add section header with original title and URL
                "### $title" | Out-File $outputFile -Append -Encoding utf8
                "Original URL: $url`n" | Out-File $outputFile -Append -Encoding utf8
                
                # Add the main content (trimmed to remove extra whitespace)
                "$($content.Trim())`n" | Out-File $outputFile -Append -Encoding utf8
                "---`n" | Out-File $outputFile -Append -Encoding utf8
            }
        }
        catch {
            Write-Host "Error processing file $filePath : $_" -ForegroundColor Red
        }
    }
}

Write-Host "Documentation merged into $outputFile" 