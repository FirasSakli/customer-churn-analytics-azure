# Azure Architecture

## Storage Layer

The project uses Azure Data Lake Storage Gen2 as the central storage layer.

Container structure:

- bronze/: raw source data
- silver/: cleaned and validated datasets
- gold/: analytics-ready datasets

Data is uploaded after local validation to minimize cloud costs
and ensure data quality.

## Analytics Layer

Azure Synapse Serverless SQL is used to query Parquet data stored in
Azure Data Lake Storage Gen2.

Stable SQL views abstract the underlying file paths and provide a
consumption layer for BI tools such as Power BI.
