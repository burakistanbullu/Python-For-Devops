#!/usr/bin/env python3
import subprocess
import datetime
import os
import sys
from datetime import timezone
import os
import requests

THRESHOLD_DAYS = 7

def get_not_after(cert_path: str) -> datetime.datetime:
    p = subprocess.Popen(["openssl", "x509", "-in", cert_path, "-noout", "-enddate"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    stdout, stderr = p.communicate()

    if p.returncode != 0:
        raise RuntimeError(f"openssl error: {stderr.decode(errors='ignore')}")

    line = stdout.decode().strip()  

    if not line.startswith("notAfter="):
        raise ValueError(f"Unexpected output: {line}")

    date_str = line.split("=", 1)[1]

    expires = datetime.datetime.strptime(date_str, "%b %d %H:%M:%S %Y %Z")
    return expires


def check_certificate(cert_path: str):
    try:
        expires_at = get_not_after(cert_path)

        now = datetime.datetime.now(timezone.utc)
        expires_at_utc = expires_at.replace(tzinfo=timezone.utc)

        diff = expires_at_utc - now
        days_left = diff.days

        if days_left <= THRESHOLD_DAYS:
            print(f"BE CAREFUL!! The certificate named {os.path.basename(cert_path)} expires on {expires_at_utc}. Days left: {days_left}")
        else:
            print(f"Everything is okay for the certificate named {os.path.basename(cert_path)} . Expires on {expires_at_utc}. Days left: {days_left}")


    except Exception as e:
        print(f"[ERROR] {cert_path}: {e}", file=sys.stderr)


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    cert_dir = os.path.join(script_dir, "certificates")

    print(f"Scanned directory: {cert_dir}")
    print(f"Threshold day value: {THRESHOLD_DAYS}")

    for root, dirs, files in os.walk(cert_dir):
        for filename in files:
            if filename.lower().endswith(".crt"):
                cert_path = os.path.join(root, filename)
                check_certificate(cert_path)

if __name__ == "__main__":
    main()

