import subprocess

def ssh_into_ec2(pem_file, username, public_ip):
    # Add the StrictHostKeyChecking option to automatically accept the host key
    ssh_command = ["ssh", "-o", "StrictHostKeyChecking=no", "-i", pem_file, f"{username}@{public_ip}"]

    try:
        # Run the SSH command
        result = subprocess.run(ssh_command, check=True)
        print("SSH connection established successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error connecting to EC2 instance: {e}")

def run_ansible_playbook(pem_file, username, public_ip):
    # Command to run the Ansible playbook
    ansible_command = [
        "ansible-playbook",
        "playbook.yaml",
        "-i", f"{public_ip},",  # Include comma to avoid Ansible interpreting as a file
        "--private-key", pem_file,
        "-u", username,
        "--ssh-common-args", "'-o StrictHostKeyChecking=no'"
    ]
    
    try:
        # Run the Ansible playbook
        result = subprocess.run(ansible_command, check=True)
        print("Ansible playbook executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error running Ansible playbook: {e}")

def main():
    pem_file = input("Enter the PEM file location: ")
    username = input("Enter the EC2 instance username: ")
    public_ip = input("Enter the EC2 public IP: ")

    # SSH into the EC2 instance
    ssh_into_ec2(pem_file, username, public_ip)

    # Run the Ansible playbook
    run_ansible_playbook(pem_file, username, public_ip)

if __name__ == "__main__":
    main()
