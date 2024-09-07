import os
import subprocess
import yaml
from getpass import getpass

def get_user_input():
    pem_file = input("Enter the PEM file location: ")
    username = input("Enter the EC2 instance username: ")
    public_ip = input("Enter the EC2 public IP: ")
    user_password = getpass("Enter the desired password for the user: ")  # Use getpass for secure input
    return pem_file, username, public_ip, user_password

def create_vars_file(pem_file, username, public_ip, user_password):
    user_data = {
        "pem_file": pem_file,
        "username": username,
        "public_ip": public_ip,
        "user_password": user_password
    }

    with open("vars/user_input.yml", "w") as vars_file:
        yaml.dump(user_data, vars_file)
    print("User inputs saved successfully in vars/user_input.yml")

def run_ansible_playbook(pem_file, username, public_ip):
    ansible_command = [
        "ansible-playbook",
        "playbook.yml",
        "-i", f"{username}@{public_ip},",
        "--private-key", pem_file,
        "-u", username,
        "--ssh-common-args", "'-o StrictHostKeyChecking=no'"
    ]
    
    try:
        subprocess.run(ansible_command, check=True)
        print("Ansible playbook executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error running Ansible playbook: {e}")

def main():
    # Step 1: Get user input
    pem_file, username, public_ip, user_password = get_user_input()

    # Step 2: Create the variables file for Ansible
    create_vars_file(pem_file, username, public_ip, user_password)

    # Step 3: Run the Ansible playbook
    run_ansible_playbook(pem_file, username, public_ip)

if __name__ == "__main__":
    main()
