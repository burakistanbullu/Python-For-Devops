# Certificate Expiration Checker

This project provides a simple Python script that scans a directory for *.crt* certificate files and checks their expiration dates.
If a certificate is close to expiration (based on a configurable threshold), the script prints a warning.


##Features
- Automatically scans the certificates/ directory
- Uses OpenSSL to retrieve certificate expiration dates
- Compares expiration date with the current time (UTC)
- Configurable expiration threshold (default: 7 days)
- Prints informative status messages and warnings

## Project Structure

```bash
.
├── certificate_checker.py   # Main script
└── certificates/            # Directory containing .crt files
```

## Usage
1. Place your certificate files (.crt) inside the certificates/ directory.
2. Run the script:
    ```bash
    python3 certificate_checker.py
    ```
3. Example output:

    ```bash
    Scanned directory: /path/to/certificates
    Threshold day value: 7
    BE CAREFUL!! The certificate named test.crt expires on 2026-05-19 09:25:34+00:00. Days left: 5
    ```
