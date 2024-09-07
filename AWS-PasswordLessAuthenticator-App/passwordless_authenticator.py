import subprocess

def get_user_input():
    pem_file = input("Enter the PEM file location: ")
    username = input("Enter the EC2 instance username: ")
    public_ip = input("Enter the EC2 public IP: ")
    return pem_file, username, public_ip

def ssh_into_ec2(pem_file, username, public_ip):
    ssh_command = ["ssh", "-i", pem_file, f"{username}@{public_ip}"]

    try:
        result = subprocess.run(ssh_command, check=True)
        print("SSH connection established successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error connecting to EC2 instance: {e}")

def main():
    pem_file, username, public_ip = get_user_input()
    ssh_into_ec2(pem_file, username, public_ip)

if __name__ == "__main__":
    main()
