#guys bisa ditulis disini ya 
import requests
import matplotlib.pyplot as plt
from datetime import datetime

# Bounding boxes for regions in Indonesia
REGIONS = {
    "1": ("Sumatra",     -6.0, 6.0, 95.0, 109.0),
    "2": ("Jawa",        -9.5, -5.5, 105.0, 114.0),
    "3": ("Kalimantan",  -4.0, 4.5, 108.0, 119.0),
    "4": ("Sulawesi",    -6.0, 6.5, 118.0, 126.0),
    "5": ("Bali-NTB-NTT",-11.0, -7.0, 114.0, 126.0),
    "6": ("Papua",       -10.0, 1.0, 136.0, 142.0),
    "7": ("Indonesia",   -11.0, 6.0, 95.0, 141.0)
}

print("=== Earthquake Monitor (Indonesia) ===")

print("Choose region:")
for key, value in REGIONS.items():
    print(f"{key}. {value[0]}")

region_choice = input("Region number: ")

if region_choice not in REGIONS:
    print("Invalid region choice.")
    exit()

region_name, min_lat, max_lat, min_lon, max_lon = REGIONS[region_choice]

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

earthquakes = data["features"]

magnitudes = []
depths = []
times = []

for eq in earthquakes:
    mag = eq["properties"]["mag"]
    depth = eq["geometry"]["coordinates"][2]
    time_ms = eq["properties"]["time"]
    time = datetime.utcfromtimestamp(time_ms / 1000)

    magnitudes.append(mag)
    depths.append(depth)
    times.append(time)

print(f"Region: {region_name}")
print(f"Total earthquakes found: {len(magnitudes)}")

plt.scatter(magnitudes, depths)
plt.xlabel("Magnitude")
plt.ylabel("Depth (km)")
plt.title(f"Earthquake Magnitude vs Depth ({region_name})")
plt.gca().invert_yaxis()
plt.grid(True)
plt.show()
