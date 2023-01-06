# Anurat Wongbunmak
# 2488941@dundee.ac.uk
# Plotting the Grow Dataset
# https://towardsdatascience.com/easy-steps-to-plot-geographic-data-on-a-map-python-11217859a2db
# https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read a comma-separated values (csv) file into DataFrame.
df = pd.read_csv("GrowLocations.csv", delimiter=',', skiprows=0, low_memory=False) # [39294 rows x 8 columns]

# drop unused column
df = df.drop(["Type","SensorType","BeginTime","EndTime"], axis=1)
# .split
df["Serial"] = df["Serial"].str.split(".").str[0]
df["Code"] = df["Code"].str.split("_").str[1]
# rename
df = df.rename(columns={"Latitude": "Lon", "Longitude": "Lat"})
# filter out lat and lon = 0
df = df[(df["Lon"] != 0) | (df["Lat"] != 0)] # [33744 rows x 8 columns]
# bounding box for the map
df = df[(df["Lon"] > -10.592) & (df["Lon"] < 1.6848)]
df = df[(df["Lat"] > 50.681) & (df["Lat"] < 57.985)]
# drop duplicate
df = df.drop_duplicates() # [5624 rows x 3 columns]

print(df) # [1073 rows x 4 columns]

df.to_csv("dfnew.csv",index=False)

# A map of the UK from Openstreet map.
map7 = plt.imread("map7.png")

# The bounding box for the map is as follows:
axis = (-10.592,1.685,50.681,57.985)

# Create a new figure
fig, ax = plt.subplots(figsize = (8,7))
colors = np.random.randint(1073, size=(1073))
ax.scatter(df.Lon, df.Lat, zorder = 1, alpha = 0.8, c = colors, s = 50, cmap = "rainbow")
ax.set_title('Plotting the Grow Dataset/nAnurat 2488941')
ax.set_xlim(axis[0], axis[1])
ax.set_ylim(axis[2], axis[3])
ax.imshow(map7, zorder=0, extent = axis, aspect= 'equal')
plt.show()
