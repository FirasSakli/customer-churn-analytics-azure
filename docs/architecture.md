# Azure Architecture

## Storage Layer
The project uses Azure Data Lake Storage Gen2 as the central storage layer.

Container structure:
- bronze/: raw source data
- silver/: cleaned and validated datasets
- gold/: analytics-ready datasets

Data is uploaded after local validation to minimize cloud costs
and ensure data quality.