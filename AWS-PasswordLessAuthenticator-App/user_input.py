import os
import json

def get_user_input():
    keypem_location = input("Enter the path to your key PEM file: ")
    public_ip = input("Enter the public IP of the EC2 instance: ")
    ec2_username = input("Enter the EC2 username: ")
    password = input("Enter the password for the EC2 instance: ")

    variables = {
        'keypem_location': keypem_location,
        'public_ip': public_ip,
        'ec2_username': ec2_username,
        'password': password
    }

    # Ensure the 'vars' directory exists
    os.makedirs('passwordless_authenticator/vars', exist_ok=True)

    with open('passwordless_authenticator/vars/user_input.yml', 'w') as file:
        json.dump(variables, file, indent=4)

if __name__ == "__main__":
    get_user_input()
