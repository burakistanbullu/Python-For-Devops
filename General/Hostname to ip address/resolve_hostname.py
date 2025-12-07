import socket

input_file = "server_names.txt"
output_file = "server_ips.txt"

# Open output file in write mode (clears existing content)
with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for line in infile:
        server_name = line.strip()
        if not server_name:
            continue

        try:
            ip = socket.gethostbyname(server_name)
            outfile.write(f"{server_name} : {ip}\n")
        except socket.gaierror:
            outfile.write(f"{server_name} : IP address could not be resolved\n")

print(f"All IP addresses have been resolved. Results have been written to '{output_file}'.")
