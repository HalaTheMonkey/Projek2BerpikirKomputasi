#guys bisa ditulis disini ya 
import requests
import matplotlib.pyplot as plt
from datetime import datetime
#5 Pulau-Pulau besar di Indonesia beserta kordinatnya
Pulau_Pulau = [
    ["Sumatra", -6.0, 6.0, 95.0, 109.0],
    ["Jawa", -9.5, -5.5, 105.0, 114.0],
    ["Kalimantan", -4.0, 4.5, 108.0, 119.0],
    ["Sulawesi", -6.0, 6.5, 118.0, 126.0],
    ["Bali-NTB-NTT",-11.0, -7.0, 114.0, 126.0],
    ["Papua",       -10.0, 1.0, 136.0, 142.0]
]

print("=== Earthquake Monitor (Indonesia) ===")

print("Choose region:")
x = 0
for i in Pulau_Pulau:
    x += 1
    print (f"{x}. {i[0]}")
Pilihan_Pulau = int(input("Region number: "))
Nama_Pulau =  Pulau_Pulau[Pilihan_Pulau -1] [0]
min_lat = Pulau_Pulau[Pilihan_Pulau -1] [1]
max_lat = Pulau_Pulau[Pilihan_Pulau -1] [2]
min_lon = Pulau_Pulau[Pilihan_Pulau -1] [3]
max_lon = Pulau_Pulau[Pilihan_Pulau -1] [4]
start_date = input("Start date (YYYY-MM-DD): ")
end_date   = input("End date   (YYYY-MM-DD): ")
min_mag    = input("Minimum magnitude: ")

url = (
    "https://earthquake.usgs.gov/fdsnws/event/1/query?"
    f"format=geojson&starttime={start_date}&endtime={end_date}"
    f"&minmagnitude={min_mag}"
    f"&minlatitude={min_lat}&maxlatitude={max_lat}"
    f"&minlongitude={min_lon}&maxlongitude={max_lon}"
)

response = requests.get(url)
data = response.json()

Gempa-Gempa = data["features"]

magnitudes = []
depths = []

for eq in Gempa-Gempa:
    mag = eq["properties"]["mag"]
    depth = eq["geometry"]["coordinates"][2]
    magnitudes.append(mag)
    depths.append(depth)


print(f"Region: {Nama_Pulau}")
print(f"Total earthquakes found: {len(magnitudes)}")

plt.scatter(magnitudes, depths)
plt.xlabel("Magnitude")
plt.ylabel("Depth (km)")
plt.title(f"Magnitudo Gempa vs Kedalaman ({Nama_Pulau}, {start_date}- {end_date})")
plt.grid(True)
plt.show()


