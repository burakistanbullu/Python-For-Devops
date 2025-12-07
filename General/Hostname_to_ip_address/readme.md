# Resolve Hostnames to IP Addresses

This simple Python script reads a list of hostnames from an input file and resolves each one to its corresponding IP address.
It then writes the results into an output file in a clean, readable format.

This is useful for automation tasks, security scan outputs, DevOps workflows, or any scenario where you need to bulk-resolve hostnames.

## How It Works
-   Reads server names line-by-line from server_names.txt
-   Cleans each line (removes extra whitespace)
-   Attempts to resolve the hostname using socket.gethostbyname()
-   Writes either:
    -   <hostname> : <ip_address>
    -   or <hostname> : IP address could not be resolved
-   Saves all results into server_ips.txt

## Usage
1. Add your hostnames to server_names.txt
2. Run the script
3. Check the output file (server_ips.txt)


## File Structure

```bash
.
├── resolve_ips.py
├── server_names.txt
└── server_ips.txt   (generated automatically)
```