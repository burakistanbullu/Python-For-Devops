import socket

INPUT_FILE = "ip_addresses.txt"
OUTPUT_FILE = "hostnames.txt"

# Read the input file line by line and write results to the output file
with open(INPUT_FILE, "r") as infile, open(OUTPUT_FILE, "w") as outfile:
    for line in infile:
        ip_address = line.strip()

        # Skip empty lines
        if not ip_address:
            continue

        try:
            # Resolve IP address to hostname
            hostname = socket.gethostbyaddr(ip_address)[0]
            outfile.write(f"{ip_address} : {hostname}\n")
        except socket.herror:
            outfile.write(f"{ip_address} : Hostname could not be resolved\n")

print(f"All hostnames have been resolved. Results have been written to '{OUTPUT_FILE}'.")
