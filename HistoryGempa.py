
import requests
import matplotlib.pyplot as plt
from datetime import datetime
#Disediakan 5 pilihan Pulau-Pulau besar di Indonesia yaitu Sumatera, Jawa, Kalimantan, Sulawesi, Papua, dan pengabungan Bali-NTB-NTT. Tersedia juga beserta kordinatnya
Pulau_Pulau = [
    ["Sumatra", -6.0, 6.0, 95.0, 109.0],
    ["Jawa", -9.5, -5.5, 105.0, 114.0],
    ["Kalimantan", -4.0, 4.5, 108.0, 119.0],
    ["Sulawesi", -6.0, 6.5, 118.0, 126.0],
    ["Bali-NTB-NTT",-11.0, -7.0, 114.0, 126.0],
    ["Papua",       -10.0, 1.0, 136.0, 142.0]
]

print("=== Monitor Gempa (Indonesia) ===")

print("Pilih pulau yang mau kamu cek datanya: ")
x = 0
#Menampilkan pilihan pulau-pulau
for i in Pulau_Pulau:
    x += 1
    print (f"{x}. {i[0]}")

#User memasukan pilihan pulau 
Pilihan_Pulau = int(input("Region number: "))

#Mengklasifikasikan data-data yang sudah tersedia
Nama_Pulau =  Pulau_Pulau[Pilihan_Pulau -1] [0]
min_lat = Pulau_Pulau[Pilihan_Pulau -1] [1]
max_lat = Pulau_Pulau[Pilihan_Pulau -1] [2]
min_lon = Pulau_Pulau[Pilihan_Pulau -1] [3]
max_lon = Pulau_Pulau[Pilihan_Pulau -1] [4]

#User memasukan data-data yang diperlukan seperti start date, end date, dan minimum magnitude
start_date = input("Start date (YYYY-MM-DD): ")
end_date   = input("End date   (YYYY-MM-DD): ")
min_mag    = input("Minimum magnitude: ")

#Mengambil data dari API USGS menggunakan parameter yang sudah di input oleh user
url = (
    "https://earthquake.usgs.gov/fdsnws/event/1/query?"
    f"format=geojson&starttime={start_date}&endtime={end_date}"
    f"&minmagnitude={min_mag}"
    f"&minlatitude={min_lat}&maxlatitude={max_lat}"
    f"&minlongitude={min_lon}&maxlongitude={max_lon}"
)

response = requests.get(url)
data = response.json()

Gempa_Gempa = data["features"]

Magnitudo = []
Kedalaman = []

#Mengolah Datanya
for eq in Gempa_Gempa:
    mag = eq["properties"]["mag"]
    depth = eq["geometry"]["coordinates"][2]
    Magnitudo.append(mag)
    Kedalaman.append(depth)

#Mengolah Grafik antara magnitudo dan kedalaman gempa-gempanya
plt.scatter(Magnitudo, Kedalaman)
plt.xlabel("Magnitudo")
plt.ylabel("Kedalaman (km)")
plt.title(f"Magnitudo Gempa vs Kedalaman ({Nama_Pulau}, {start_date}- {end_date})")
plt.grid(True)

#Menampilakan hasil total gempa
print(f"Pulau: {Nama_Pulau}")
print(f"Kurun Waktu: {start_date} sampai {end_date}")
print(f"Minimum Magnitudo: {min_mag}")
print(f"Total Gempa yang ditemukan: {len(Magnitudo)}")
#Menampilkan Grafik
plt.show()
