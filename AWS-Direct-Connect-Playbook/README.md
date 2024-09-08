

# AWS Direct Connect Playbook

This repository contains an Ansible playbook for configuring the AWS CLI using AWS credentials from a CSV file. The playbook reads access key ID and secret access key from the specified CSV file and configures the AWS CLI on macOS systems.

## Prerequisites

1. **Ansible**: Ensure Ansible is installed on your machine. You can install it via Homebrew:

   ```bash
   brew install ansible
   ```

2. **AWS CLI**: Ensure AWS CLI is installed. You can install it via Homebrew if not already installed:

   ```bash
   brew install awscli
   ```

3. **AWS Credentials CSV File**: Prepare a CSV file containing your AWS credentials. The file should be formatted as follows:

   ```
   Access key ID,Secret access key
   YOUR_ACCESS_KEY_ID,YOUR_SECRET_ACCESS_KEY
   ```

   Example file path: `/Users/yourusername/Desktop/AwsKeys/rootkey - aws cli.csv`

## Playbook Overview

The Ansible playbook `aws_connect.yaml` performs the following tasks:

1. **Read AWS Credentials CSV File**: Reads the CSV file containing AWS credentials.
2. **Decode Credentials**: Decodes the base64-encoded content of the file.
3. **Parse Credentials**: Extracts the access key ID and secret access key from the CSV file.
4. **Configure AWS CLI**: Configures the AWS CLI with the extracted credentials.
5. **Verify Configuration**: Runs a command to verify that the AWS CLI is correctly configured.
6. **Show Configuration**: Displays the IAM user or role associated with the configured credentials.

## Usage

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/ayuspoudel/Ansible-Playbooks-Project.git
   cd AWS-Direct-Connect-Playbook
   ```

2. **Update the Playbook**: Modify the `aws_credentials_file` variable in `aws_connect.yaml` to point to the path of your CSV file.

   ```yaml
   vars:
     aws_credentials_file: "/Users/yourusername/Desktop/AwsKeys/rootkey - aws cli.csv"
   ```

3. **Run the Playbook**:

   ```bash
   ansible-playbook aws_connect.yaml
   ```

4. **Check AWS CLI Configuration**: After running the playbook, you can verify the configuration by checking the output, which will include the IAM user or role information.

## Example Output

After running the playbook, you should see output similar to the following:

```
AWS CLI is configured. Caller Identity: {
    "UserId": "AIDXXXXXXXXXXXXXX",
    "Account": "123456789012",
    "Arn": "arn:aws:iam::123456789012:user/YourUsername"
}
```

## Troubleshooting

- **Ensure AWS CLI is installed**: Verify that the `aws` command is available in your terminal.
- **Check CSV file path**: Ensure the path to the CSV file is correct and accessible.
- **Review Ansible Output**: If errors occur, review the output for any clues and ensure the CSV file format is correct.


This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Replace `yourusername` in the `git clone` command and CSV file path with your actual GitHub username and file path as needed.
