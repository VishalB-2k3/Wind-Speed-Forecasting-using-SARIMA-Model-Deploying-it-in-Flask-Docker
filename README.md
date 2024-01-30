# Wind-Speed-Forecasting-using-SARIMA-Model-Deploying-it-in-Flask-Docker
NIWE Internship Work Project

1. Converted NetCDF files containing meteorological data into a structured CSV format using Python and xarray, enabling efficient data manipulation and extraction.
2. Preprocessed the dataset to handle missing values, performed feature engineering, and prepared the data for modeling purposes.
3. Developed a Seasonal Autoregressive Integrated Moving Average (SARIMA) model using Python's statsmodels library to forecast wind speed values for the year 1941. Optimized model parameters iteratively and evaluated model performance using diagnostic plots and evaluation metrics.
4. Built a user-friendly Flask web application to provide convenient access to the forecasting model, allowing users to input location and time parameters and retrieve forecasted wind speed values.
5. Implemented Docker containerization to package the web application and its dependencies into a portable container, ensuring consistency and reliability across different computing environments.
6. Visualized forecasted wind speed values using matplotlib, enabling intuitive interpretation of predicted trends and patterns.


Files :
1. FCT Model_NIWE - SARIMA Model Code
2. app.py - Flask App Code
3. dockerfile - DockerFile
4. Data Extraction_NIWE - NETCdf to CSV Conversion
5. Requirements txt for DockerFile
