from http.client import responses

import requests

# import pandas as pd
"""
response = requests.get("https://developer.nrel.gov/api/alt-fuel-stations/v1.json?limit=1",
                        headers={
                            'x-api-key': 'DEMO_KEY'
                        })

print(response.status_code)
print(response.json())

"""

url = "https://opendata.ecdc.europa.eu/covid19/casedistribution/json/"

response = requests.get(url)

data = response.json()

df = pd.Dataframe(data[records])