param (
    [string]$directoryPath,
    [string]$time
)

# Check if the directory path is provided
if (-not $directoryPath) {
    Write-Error "Please provide a directory path."
    exit
}

# Retrieve the list of files and compare their lastwritetime with the date
Get-ChildItem -Path $directoryPath -Recurse | Where-Object { $_.LastWriteTime -gt (Get-Date).AddDays(-$time) }