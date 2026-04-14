# GCP Real-Time Data Pipeline

## 🚀 Overview
This project implements a scalable real-time data pipeline on Google Cloud Platform using Pub/Sub, Dataflow, and BigQuery. The pipeline ingests streaming data, processes it using Apache Beam, and stores structured data for analytics.

## 🏗️ Architecture
Python Publisher → Pub/Sub → Dataflow (Apache Beam) → BigQuery

## ⚙️ Tech Stack
- Google Cloud Platform (Pub/Sub, Dataflow, BigQuery)
- Python
- Apache Beam
- SQL

## 🔄 Data Flow
1. A Python script publishes streaming data to a Pub/Sub topic  
2. Dataflow pipeline (Apache Beam) consumes messages in real time  
3. Data is transformed, validated, and structured  
4. Processed data is loaded into BigQuery for analytics  

## 📊 Features
- Real-time streaming ingestion using Pub/Sub  
- Scalable processing using Dataflow  
- Schema enforcement for structured data  
- Near real-time analytics in BigQuery  

## 📂 Project Structure
- `scripts/publisher.py` – Publishes streaming data  
- `scripts/dataflow_pipeline.py` – Processes and loads data  

## ▶️ How to Run
1. Create Pub/Sub topic and subscription  
2. Create BigQuery dataset and table  
3. Deploy Dataflow pipeline  
4. Run publisher script  

## 📈 Example Query
```sql
SELECT * 
FROM `weather_dataset.weather_data`
ORDER BY timestamp DESC
LIMIT 10;
