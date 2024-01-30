# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 20:19:06 2023

@author: Vini
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 10:21:02 2023

@author: Vini
"""

import datetime as dt
import numpy as np
import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt

def convert_time(df, offset=5.5):
    try:
        time_stamp = pd.to_datetime(df['time'].values) + pd.to_timedelta(offset, unit='h')
    except:
        print('Timestamp not available')
        return None

    return time_stamp

# Access the netCDF4 File
nc_file = r"D:\NIWE\adaptor.mars.internal-1702483552.6584578-7461-4-80b5f743-859f-4266-83fe-9d0f9a91089d.nc"
ds = xr.open_dataset(nc_file)

# Give the target latitude and longitude
niwe_latitude = 8.953708
niwe_longitude = 77.720113

# Nearest target coordinates from dataset with minimum difference
min_tgt_latitude = abs(ds.latitude - niwe_latitude).argmin().item()
min_tgt_longitude = abs(ds.longitude - niwe_longitude).argmin().item()

# Extract the target data from datasets
target_data = ds.sel(latitude=ds.latitude[min_tgt_latitude], longitude=ds.longitude[min_tgt_longitude])

# Converting the extracted data into a dataframe
df = target_data.to_dataframe()

# Reset to Pandas DataFrame
df.reset_index(inplace=True)

# Print the first few rows of the dataframe
print(df.head())

# Calculate wind direction at 100m
df['winddirection_100m'] = 57.3 * np.arctan2(df.u100, df.v100) + 180

# Calculate wind speed at 100m
df['windspeed_100m'] = np.sqrt((np.square(df.u100)) + (np.square(df.v100)))

# Convert time with offset
df['Timestamp'] = pd.to_datetime(df['time'].values) + dt.timedelta(hours=5.5)

# Save dataset to CSV file
df.to_csv('targetfinal_niwe.csv')

#Visualization
# Plotting wind direction at 100m
plt.figure(figsize=(12, 6))
plt.plot(df['Timestamp'], df['winddirection_100m'], label='Wind Direction (100m)')
plt.xlabel('Timestamp')
plt.ylabel('Wind Direction (degrees)')
plt.title('Wind Direction at 100m Over Time')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plotting wind speed at 100m
plt.figure(figsize=(12, 6))
plt.plot(df['Timestamp'], df['windspeed_100m'], label='Wind Speed (100m)')
plt.xlabel('Timestamp')
plt.ylabel('Wind Speed (m/s)')
plt.title('Wind Speed at 100m Over Time')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
