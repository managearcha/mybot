# MyBot.ps1

# Define the SSH connection details
$sshUser = "unix"
$sshHost = "managearcha"

# Establish the SSH connection
ssh "$sshUser@$sshHost"

# Run the Python script
& .\venv\Scripts\python.exe bot.py