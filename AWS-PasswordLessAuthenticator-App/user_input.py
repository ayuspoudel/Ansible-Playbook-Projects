import os

def get_user_input():
    keypem_location = input("Enter the path to your key PEM file: ")
    public_ip = input("Enter the public IP of the EC2 instance: ")
    ec2_username = input("Enter the EC2 username: ")
    password = input("Enter the password for the EC2 instance: ")

    # Store variables in YAML file
    variables = {
        'keypem_location': keypem_location,
        'public_ip': public_ip,
        'ec2_username': ec2_username,
        'password': password
    }

    # Ensure the 'vars' directory exists
    os.makedirs('passwordless_authenticator/vars', exist_ok=True)
    with open('passwordless_authenticator/vars/user_input.yml', 'w') as file:
        for key, value in variables.items():
            file.write(f"{key}: {value}\n")

    # Create the dynamic inventory file
    inventory_content = f"""
[ec2]
{public_ip} ansible_user={ec2_username} ansible_ssh_private_key_file={keypem_location}
"""
    with open('inventory', 'w') as inventory_file:
        inventory_file.write(inventory_content)

    print("User input saved and inventory file created.")

if __name__ == "__main__":
    get_user_input()
