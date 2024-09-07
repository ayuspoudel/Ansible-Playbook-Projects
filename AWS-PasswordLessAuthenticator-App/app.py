import os
import subprocess
from getpass import getpass

def get_user_input():
    pem_file = input("Enter the PEM file location: ")
    username = input("Enter the EC2 instance username: ")
    public_ip = input("Enter the EC2 public IP: ")
    return pem_file, username, public_ip

def ssh_into_ec2(pem_file, username, public_ip):
    ssh_command = f"ssh -i {pem_file} {username}@{public_ip}"
    os.system(ssh_command)

def main():
    # Step 1: Get user input
    pem_file, username, public_ip = get_user_input()

    # Step 2: SSH into EC2
    ssh_into_ec2(pem_file, username, public_ip)

    # Step 3: Run Ansible playbook for configuring password authentication
    subprocess.run(["ansible-playbook", "-i", f"{username}@{public_ip},", "playbook.yml"])

if __name__ == "__main__":
    main()
