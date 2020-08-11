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

# print(spotify_data["artistName"].head())
sumMs = spotify_data["msPlayed"].sum()
print()
print("Average hours listen per day " + str(sumMs / 1000.0 / 3600 / 365))
print()

print("====== top by times played ======")
artistNames = spotify_data["artistName"]
counts = artistNames.value_counts()
print(counts)
counts[counts >= 400].plot(kind="bar")
print("============")

plt.show()

print("done")
