---

# Ansible Playbook for WebApp Deployment on EC2 with Apache2
  
This folder contains an Ansible playbook designed to automate the deployment of a web application on an AWS EC2 instance. It includes the installation of Apache2 and deployment of the `index.html` file to the web server.

## Folder Structure

- `hosts/`
  - `inventory.ini`: The inventory file listing the EC2 instances where the playbook will be executed.
  - `index.html`: The web application file to be deployed.
  - `main.yaml`: The Ansible playbook that installs Apache2 and copies `index.html` to the appropriate directory on the EC2 instance.

## Prerequisites

Ensure you have the following before running the playbook:
- Ansible installed on your local machine.
- Python and `boto3` installed for EC2 integration with Ansible.
- SSH access to the specified EC2 instances.

## Playbook Overview

The `main.yaml` playbook includes the following tasks:
1. **Apache2 Installation**: Installs Apache2 on the EC2 instances using the APT package manager.
2. **Deploy Web Application**: Copies the `index.html` file to `/var/www/html` on the EC2 instance and sets the correct ownership and permissions.

### Playbook Breakdown

- **Install Apache2**:
  The `ansible.builtin.apt` module is used to ensure Apache2 is installed and up-to-date on the EC2 instance.

- **Copy index.html**:
  The `ansible.builtin.copy` module copies the `index.html` file to the web server's root directory (`/var/www/html`), setting the owner as `root` and permissions to `0644`.

## Inventory

The `inventory.ini` file contains the list of EC2 instances (with their public IPs) that Ansible will target. Each entry in this file should be the format:
```bash
ubuntu@<EC2-public-IP>
```

### Current Inventory
```ini
ubuntu@3.86.166.19
ubuntu@3.86.189.188
```

## How to Run the Playbook

1. Navigate to the folder containing the playbook and the inventory file:
   ```bash
   cd Ansible-Playbook-WebDeployment-EC2
   ```

2. Run the playbook using the following command:
   ```bash
   ansible-playbook -i hosts/inventory.ini hosts/main.yaml
   ```

This will execute the playbook on all the EC2 instances listed in `inventory.ini`, installing Apache2 and deploying your web application.

