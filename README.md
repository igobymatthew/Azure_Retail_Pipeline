# Azure Retail Pipeline

## Overview
This project demonstrates an end-to-end Azure-based data pipeline for a retail business scenario. It uses Azure Data Factory, Azure SQL Database, Databricks, SSIS, and Python for ingestion, transformation, and analysis of sales data.

## Architecture
- **ADF**: Ingests data from source to Azure SQL
- **SSIS**: Optional legacy ETL import
- **Databricks**: Performs heavy transformations and joins
- **Python**: Applies business rules and analytics
- **Azure SQL**: Stores cleaned and enriched data

## Structure
- `/data`: Sample source data
- `/notebooks`: Databricks notebooks
- `/python`: Python scripts for ETL and analytics
- `/ssis`: SSIS package files
- `/adf`: ADF pipeline definitions
- `/sql`: Database schema and stored procedures
- `/diagrams`: Architecture diagrams and flowcharts

## Instructions
1. Import data using ADF or SSIS
2. Run Databricks notebooks to clean and enrich data
3. Use Python scripts for anomaly detection
4. Store final results in Azure SQL for reporting
