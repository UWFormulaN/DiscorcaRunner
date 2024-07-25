import subprocess
import time

def IsDiscorcaRunning(container_name):
    """Check if the specified Docker container is running."""
    try:
        # List all running containers and check if the specified container is in the list
        result = subprocess.run(['docker', 'ps', '--format', '{{.Names}}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        print(result.stdout)
        return container_name in result.stdout.strip().split('\n')
    except subprocess.SubprocessError as e:
        print(f"Error checking container status: {e}")
        return False

def RemoveContainer(container_name):
    """Remove the specified Docker container."""
    try:
        subprocess.run(['docker', 'rm', container_name], check=True)
        print(f"Container {container_name} removed successfully.")
    except subprocess.SubprocessError as e:
        print(f"Error removing container {container_name}: {e}")

def RunOrcaBot (container_name):
    try:
        subprocess.run(['docker', 'run', '-it', '--name', 'orcabot', '--restart=always', '--shm-size=100G', '-v', '/homeFAST/OrcaBot/Settings:/OrcaBot/Resources', '-v', '/homeFAST/OrcaBot/OrcaJobsArchive:/OrcaJobsArchive','mrdnalex/orcabot'], check=True)
        print(f"Container {container_name} removed successfully.")
    except subprocess.SubprocessError as e:
        print(f"Error removing container {container_name}: {e}")

container_name = "orcabot"

while True:
    if not IsDiscorcaRunning(container_name):
        print(f"Container {container_name} is not running. Removing it...")
        RemoveContainer(container_name)
        RunOrcaBot(container_name)
    else:
        print(f"Container {container_name} is running.")
    
    time.sleep(10)  # Wait for 10 seconds before checking again
