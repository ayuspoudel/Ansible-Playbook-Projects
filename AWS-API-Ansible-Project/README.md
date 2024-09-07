---

# AWS-API Ansible Project

This project contains Ansible playbooks and configuration files for automating the management of AWS EC2 instances using the AWS API. The playbooks handle tasks such as creating, configuring, and managing EC2 instances in AWS.

## Folder Structure

- `ec2/`: Contains tasks related to EC2 instance management.
- `group_vars/`: Stores global variables shared across all playbooks.
  - `all`: Contains general configuration variables for the project.
- `ec2_create.yaml`: The main playbook for creating an EC2 instance.
- `inventory.ini`: The inventory file listing the EC2 instances managed by Ansible.
- `pass.yml`: Encrypted variable file (likely for storing sensitive information like access keys).
- `vault.pass`: The Ansible vault password file used for decrypting `pass.yml`.

## Playbook Overview

### `ec2_create.yaml`

This playbook performs the following tasks:
1. **Create EC2 Instance**: Uses the AWS API to create and configure a new EC2 instance, using parameters like instance type, AMI, and security group settings from the `group_vars` and `pass.yml` files.
2. **Configure EC2 Instance**: After creation, the playbook ensures the instance is properly configured, including network settings and any required software installations.

## Role Initialization

To maintain modularity and reusability, roles were initialized for handling EC2 management tasks.

### Steps to Initialize the Role

1. Navigate to your project directory:
   ```bash
   cd AWS-API-Ansible-Project
   ```

2. Initialize a new Ansible role using the `ansible-galaxy` command:
   ```bash
   ansible-galaxy init ec2
   ```

   This will create the following structure under the `ec2/` directory:
   - `tasks/`: Contains YAML files defining tasks (e.g., creating EC2 instances, configuring software).
   - `handlers/`: Handles tasks that need to be triggered after specific actions.
   - `vars/`: Contains variables specific to the role.
   - `defaults/`: Contains default values for variables.
   - `meta/`: Stores metadata about the role.
   - `files/` and `templates/`: Stores files or templates to be copied to the managed machines.

## Ansible Vault Creation and Editing

Ansible Vault was used to store sensitive information (like AWS access keys) securely.

### Creating the Vault

1. To create a vault file (`pass.yml`), use the following command:
   ```bash
   ansible-vault create pass.yml
   ```

2. You will be prompted to enter a password for encrypting the file. This password will be required each time you need to edit or run the playbooks that use the vault.

3. Inside the `pass.yml` file, store sensitive information in YAML format. For example:
   ```yaml
   aws_access_key: YOUR_AWS_ACCESS_KEY
   aws_secret_key: YOUR_AWS_SECRET_KEY
   ```

### Editing the Vault

To edit an existing vault file, run:
```bash
ansible-vault edit pass.yml
```

You will be prompted to enter the vault password, after which you can edit the contents of the file.

### Vault Password File

To avoid manually entering the vault password each time, you can store the password in a file (`vault.pass`) and reference it when running the playbook:
```bash
ansible-playbook -i inventory.ini ec2_create.yaml --vault-password-file vault.pass
```

## Prerequisites

Before running the playbook, ensure the following are set up:
- AWS account with proper permissions to manage EC2 instances.
- AWS credentials stored in `pass.yml` or through environment variables.
- Ansible installed on your local machine.
- Python and `boto3` installed for interacting with the AWS API.

## Variables

Global variables are defined in:
- `group_vars/all`: General configuration options for EC2 instances such as default region, instance type, and key pair.
- `pass.yml`: Contains encrypted sensitive data such as AWS access keys and secrets.

You can customize the following key variables:

- **`aws_region`**: AWS region where the EC2 instances will be created.
- **`ec2_instance_type`**: Type of EC2 instance to create (e.g., `t2.micro`).
- **`ami_id`**: Amazon Machine Image (AMI) ID for the EC2 instance.

## How to Run the Playbook

1. Ensure the inventory and group variables are configured properly in `inventory.ini` and `group_vars/all`.
2. Decrypt the `pass.yml` file (if applicable) with the vault password stored in `vault.pass`.
3. Run the `ec2_create.yaml` playbook to create and configure a new EC2 instance:
   ```bash
   ansible-playbook -i inventory.ini ec2_create.yaml --vault-password-file vault.pass
   ```

## Inventory

The `inventory.ini` file is used to specify the EC2 instances managed by Ansible. This file is automatically updated when new instances are created by the `ec2_create.yaml` playbook.

