# Resolve IP Addresses to Hostnames

This Python script reads a list of IP addresses from an input file and attempts to resolve each one to its corresponding hostname using reverse DNS lookup (socket.gethostbyaddr).
The results are written to an output file in a clean, readable format.

This tool is useful for DevOps, SRE, networking tasks, asset discovery, and processing security scan outputs.

## How It Works
-   The script opens ip_addresses.txt and reads it line by line.
-   For every IP address, the script attempts a reverse DNS lookup
-   If the hostname is resolved successfully, it's written to hostnames.txt
-   After processing all IP addresses, a completion message is printed.

## Usage
1. Add IP addresses into ip_addresses.txt
2. Run the script
3. Check the output file (hostnames.txt)


## File Structure

```bash
.
├── resolve_hostnames.py
├── ip_addresses.txt
└── hostnames.txt    (generated automatically)
```