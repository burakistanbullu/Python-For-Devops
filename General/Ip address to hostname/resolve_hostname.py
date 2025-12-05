import socket

# IP adreslerini içeren dosya
input_file = "ip_addresses.txt"
# Sonuçların yazılacağı dosya
output_file = "hostnames.txt"

# Çıktı dosyasını temizle
with open(output_file, "w") as f:
    f.write("")

# Dosyadaki her IP adresini sırayla işle
with open(input_file, "r") as infile, open(output_file, "a") as outfile:
    for line in infile:
        ip_address = line.strip()
        if not ip_address:
            continue

        try:
            # IP adresinin hostname'ini çözümle
            hostname = socket.gethostbyaddr(ip_address)[0]
            outfile.write(f"{ip_address} : {hostname}\n")
        except socket.herror:
            outfile.write(f"{ip_address} : Hostname bulunamadı\n")

print(f"Tüm hostname'ler çözümlendi. Sonuçlar '{output_file}' dosyasına yazıldı.")
