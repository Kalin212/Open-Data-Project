import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import sys

if os.path.isfile("basic panda/StreamingHistory0.json"):
    filepath = "basic panda/StreamingHistory0.json"
    print("loading from file")
else:
    print("cannot find file")
    sys.exit(1)

spotify_data = pd.read_json(filepath)

print(spotify_data)
print(spotify_data.columns)

print(spotify_data.iloc[0])
# print(spotify_data.iloc[0]["artistName"])

# https://stackoverflow.com/questions/44908383/how-can-i-group-by-month-from-a-date-field-using-python-pandas

spotify_data["endTime"] = pd.to_datetime(spotify_data["endTime"])

#print(spotify_data[spotify_data['trackName'].isin(['The End', 'Location', 'Magnolia'])])
spotify_data = spotify_data[spotify_data['artistName'] == 'JPEGMAFIA']

hours_by_month = spotify_data.groupby(spotify_data["endTime"].dt.strftime('%B'))['msPlayed'].sum() / 1000.0 / 3600

hours_by_month = hours_by_month[['August', 'September', 'October', 'November', 'December', 'January', 'February', 'March', 'April', 'May', 'June', 'July']]
print(hours_by_month.sum())

hours_by_month.plot(kind="bar")

plt.show()

print("done")
