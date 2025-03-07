# MyBot.ps1

# Activate the virtual environment
$venvPath = 'C:\Users\Admin\Documents\GitHub\mybot\.venv\Scripts\Activate.ps1'
if (Test-Path $venvPath) {
    . $venvPath
} else {
    Write-Error "Virtual environment activation script not found: $venvPath"
    exit 1
}

# Run the Python script
$pythonExecutable = '.venv\Scripts\python.exe'
$pythonScript = 'bot.py'
if (Test-Path $pythonExecutable) {
    & $pythonExecutable $pythonScript
} else {
    Write-Error "Python executable not found in virtual environment."
    exit 1
}