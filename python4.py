import requests
import pandas as pd


def download_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to download data")


def process_data(data):
    rows = []
    for meteorite in data:
        try:
            mass = float(meteorite["mass"])
            year = meteorite['year']
            reclat = float(meteorite['reclat']),
            reclong = float(meteorite['reclong'])
            coordinates = [int(meteorite['geolocation']["coordinates"][0]), int(meteorite['geolocation']["coordinates"][1])]
        except KeyError:
            mass = None
            year = None
            reclat = None
            reclong = None
            coordinates = [None, None]
        row = {
            'name': meteorite['name'],
            'id': meteorite['id'],
            'nametype': meteorite['nametype'],
            'recclass': meteorite['recclass'],
            'mass':mass,
            'year': year,
            'reclat': reclat,
            'reclong': reclong,
            'coordinates': coordinates
        }
        rows.append(row)
    return rows


def export_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)


# Download the data from the provided link
url = "https://data.nasa.gov/resource/y77d-th95.json"
meteorite_data = download_data(url)

# Process the data into structured format
processed_data = process_data(meteorite_data)

# Export the data to CSV
output_filename = "meteorite_data.csv"
export_to_csv(processed_data, output_filename)
print("Data exported to", output_filename)
