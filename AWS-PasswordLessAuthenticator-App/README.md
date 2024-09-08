
# AWS Passwordless Authenticator

## Overview

This project provides a solution for passwordless authentication to the AWS console from the machine where the code is executed. The solution uses Python for the initial setup and Ansible for the configuration management.

## Repository Structure

- **`.venv/`**: Virtual environment for Python dependencies.
- **`.vscode/`**: VS Code configuration files.
- **`passwordless_authenticator/`**: Contains code for passwordless authentication.
  - **`user_input.py`**: Python script for handling user input and authentication setup.
- **`inventory.ini`**: Ansible inventory file specifying the hosts for the playbook.
- **`playbook.yml`**: Ansible playbook for configuring the authentication setup.
- **`.DS_Store`**: macOS file that stores custom attributes of a folder.

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/Ansible-Playbook-Projects.git
   cd Ansible-Playbook-Projects/AWS-PasswordLessAuthenticator-App/
   ```

2. **Set Up Python Virtual Environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. **Install Python Dependencies**

   Install any required Python packages. You might need to create a `requirements.txt` file if not already present.

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Python Script**

   Execute the Python script to handle user input and initial setup.

   ```bash
   python passwordless_authenticator/user_input.py
   ```

5. **Run the Ansible Playbook**

   After the Python script has set up the necessary configuration, run the Ansible playbook to complete the setup.

   ```bash
   ansible-playbook -i inventory.ini playbook.yml
   ```

## Usage

1. Follow the instructions provided by the `user_input.py` script to configure your AWS credentials and settings.
2. Ensure that the Ansible playbook `playbook.yml` is correctly configured for your environment.

## Contributing

Feel free to submit pull requests or open issues for improvements or bug fixes.


## Contact

For any questions or feedback, please contact ayushpoudel@usf.edu.
