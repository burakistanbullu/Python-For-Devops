# AWS Daily Service Cost Fetcher

This project fetches **yesterday's AWS service-level costs** using the **AWS Cost Explorer API** and displays them in a simple, readable table.

It is designed to be **beginner-friendly**, easy to run, and provides a clean example of how to work with `boto3`, AWS Cost Explorer, and basic data processing in Python.


## Features
- Retrieves **UnblendedCost** for each AWS service
- Excludes **Credits** and **Refunds** for cleaner data
- Automatically calculates **yesterday’s date**
- Sorts services by cost in descending order
- Displays service name, cost, and currency
- Shows total daily cost
- Small & clean codebase — easy to understand and extend

## Requirements
- Python 3.8+
- AWS credentials configured locally  
  (via `~/.aws/credentials`, `AWS_ACCESS_KEY_ID`, etc.)
- Required Python package:

    ```bash
    pip install boto3
    ```

## Example Output

```bash
AWS service costs for 2025-01-14:

Amazon RDS                                9.2000 USD
Amazon EC2                                5.6700 USD
Amazon S3                                 1.2300 USD

Total: 16.1000 USD
```
