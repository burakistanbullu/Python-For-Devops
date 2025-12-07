# Terraform Infrastructure Drift Checker

This script automates the detection of infrastructure drift by running terraform plan and notifying you via email if any changes are detected. It is intended to be used as a scheduled job (e.g., cron, CI pipeline) to continuously monitor your Terraform-managed infrastructure.

## Features
-   Runs terraform plan with -detailed-exitcode to check for drift
-   Sends an email notification when changes are detected
-   Logs important events using Python’s built-in logging
-   Configurable entirely through environment variables
-   Timeout protection for long-running Terraform commands

## Requirements
-   Python 3.8+
-   Terraform installed and accessible in $PATH
-   Valid SMTP credentials
-   Required environment variables defined (see below)


## Configuration

```bash
TERRAFORM_DIR:  Path to the Terraform project to check
EMAIL_FROM:     Sender email address
EMAIL_TO:       Recipient email address
SMTP_SERVER:    SMTP server hostname
SMTP_PORT:      SMTP server port (default: 587)
SMTP_USER:      SMTP authentication username
SMTP_PASSWORD:	SMTP authentication password
```
You can export them like this:

```bash
export TERRAFORM_DIR=/path/to/terraform
export EMAIL_FROM="alerts@example.com"
export EMAIL_TO="you@example.com"
export SMTP_SERVER="smtp.example.com"
export SMTP_PORT=587
export SMTP_USER="smtp-user"
export SMTP_PASSWORD="smtp-pass"
```

## Running the Script
Simply execute:
```bash
python3 check_infrastructure.py
```