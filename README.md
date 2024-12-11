#Final Project for GEO 115 Programming in GIS
#Minerals.py
This Python script uses the arcpy library to automate geospatial processing tasks within ArcGIS Pro.

Here's a breakdown of the script's purpose:

1. Import Toolbox: Imports the "Data Management Tools" toolbox, which contains various geoprocessing tools.
2. Input Data: Defines input data paths for:
Mineral_Core_Location_csv: A CSV file containing mineral core location data.
Health_Status_Area_HSA_: Represents a feature class defining health status area boundaries.
3. XY Table To Point: Converts the CSV data into point features based on longitude and latitude fields.
The Minerals_Core_Location variable stores the output point features.

4. Select (Gold, Diamonds): Selects mineral core locations where the 'Corehole_Purpose' is 'Gold, Diamonds'.
The output of this selection is stored in Minerals_Select.
5. Clip: Clips the selected mineral core locations (Minerals_Select) to the boundaries of the health status area (Health_Status_Area_HSA_).
The clipped features are stored in Minerals_Clip.

6. Buffer (50Km):Creates a buffer around the clipped features (Minerals_Clip) with a distance of 50 kilometers.
The buffered features are stored in MineralsClip_Buffer.
