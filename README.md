# Housing Cost Analysis and Prediction (CRISP-DM)

- Santiago Beltrán Ruiz
- Laura González Ayala
- Tomás Macías Yepes

## Short description:
Using publicly available data and following the CRISP-DM methodology, this analysis investigates property price estimation and examines the real estate market in the Metropolitan Area of the Aburrá Valley.

## Results:
A model with a **(Mean Absolute Error) MAE** of **54,157,334 COP** trained with only 3980 entries (pre-processed data), that equals to a **Mean Absolute Percentage Error (MAPE)** of **11.53%**. Emphasis was made on data cleaning and building a robust ETL process that allowed for dimension completion and outlier detection. 

## What could be better?
Automating the ETL process and executing it periodically would allow access to a larger and more up-to-date dataset. Additionally, performing reverse geolocation lookups for each data point would enhance data integrity and could improve the accuracy of the price per square meter per zone variable, which may better explain price heterogeneity in nearby areas.
Developing methods to reliably predict unknown categorical values—such as stratum—would increase the available training data.

Incorporating spatially derived features, such as altitude, and distances to shopping centers, schools, or medical facilities, could help better capture location-based influences on property prices.

Finally, conducting a more in-depth descriptive analysis could help refine the focus of the data preparation and modeling phases.
