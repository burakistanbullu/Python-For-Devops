import socket

# Sunucu isimlerini içeren dosya
input_file = "server_names.txt"
# Sonuçların yazılacağı dosya
output_file = "server_ips.txt"

# Çıktı dosyasını temizle
with open(output_file, "w") as f:
    f.write("")

# Dosyadaki her sunucu ismini sırayla işle
with open(input_file, "r") as infile, open(output_file, "a") as outfile:
    for line in infile:
        server_name = line.strip()
        if not server_name:
            continue

        try:
            # Sunucu isminin IP adresini çözümle
            ip = socket.gethostbyname(server_name)
            outfile.write(f"{server_name} : {ip}\n")
        except socket.gaierror:
            outfile.write(f"{server_name} : IP bulunamadı\n")

print(f"Tüm IP adresleri çözümlendi. Sonuçlar '{output_file}' dosyasına yazıldı.")
