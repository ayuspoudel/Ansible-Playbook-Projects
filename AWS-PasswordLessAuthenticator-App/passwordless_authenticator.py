import subprocess
import yaml

def get_user_input():
    pem_file = input("Enter the PEM file location: ")
    username = input("Enter the EC2 instance username: ")
    public_ip = input("Enter the EC2 public IP: ")
    password = input("Enter the new password for the user: ")
    return pem_file, username, public_ip, password

def ssh_into_ec2(pem_file, username, public_ip):
    ssh_command = ["ssh", "-o", "StrictHostKeyChecking=no", "-i", pem_file, f"{username}@{public_ip}"]
    try:
        result = subprocess.run(ssh_command, check=True)
        print("SSH connection established successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error connecting to EC2 instance: {e}")

def run_ansible_playbook(pem_file, username, public_ip, password):
    with open('playbook.yaml', 'r') as f:
        playbook = yaml.safe_load(f)
    playbook['vars']['username'] = username
    playbook['vars']['password'] = password

    with open('playbook_temp.yaml', 'w') as f:
        yaml.dump(playbook, f)

    ansible_command = [
        "ansible-playbook",
        "-i", f"{username}@{public_ip},",
        "playbook_temp.yaml",
        "--private-key", pem_file,
        "--ssh-common-args", "-o StrictHostKeyChecking=no"
    ]

    try:
        result = subprocess.run(ansible_command, check=True)
        print("Ansible playbook executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error running Ansible playbook: {e}")

def main():
    pem_file, username, public_ip, password = get_user_input()
    ssh_into_ec2(pem_file, username, public_ip)
    run_ansible_playbook(pem_file, username, public_ip, password)

if __name__ == "__main__":
    main()
