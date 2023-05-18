def split_into_packets(file_path, packet_size):
    packets = []
    try:
        with open(file_path, "rb") as file:
            while True:
                data = file.read(packet_size)
                if not data:
                    break
                packets.append(data)
    except FileNotFoundError:
        print("Fichier non trouvé")
        return "N"
    return packets

def recreate_file_from_packets(packets, output_file_path):
    with open(output_file_path, "wb") as file:
        for packet in packets:
            file.write(packet)


print(">>> Bienvenue dans l'algorithme de cryptage !")

key_bytes = input(">>> Quelle sera la clé de cryptage/décryptage ?").encode('utf-8')
len_Bytes_packets = len(key_bytes)
xor = []

url = input("Chemin du fichier ?")

packets = split_into_packets(url, len_Bytes_packets)
if(packets != "N"):
    for packet in packets:
        xor.append(bytes([a ^ b for a, b in zip(packet, key_bytes)]))
    recreate_file_from_packets(xor, url)