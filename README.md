<<<<<<< HEAD
# gcp-real-time-data-pipeline
Real-time data pipeline using Pub/Sub, Dataflow, and BigQuery
=======
# Real-Time Data Pipeline on GCP

## 🚀 Overview
This project demonstrates a real-time data pipeline built using Google Cloud Platform services. It ingests streaming data, processes it using Apache Beam, and stores it in BigQuery for analytics.

## 🏗️ Architecture
Publisher (Python) → Pub/Sub → Dataflow (Apache Beam) → BigQuery

## ⚙️ Tech Stack
- Google Cloud Platform (Pub/Sub, Dataflow, BigQuery)
- Python
- Apache Beam
- SQL

## 📊 Features
- Real-time data ingestion using Pub/Sub
- Stream processing using Dataflow
- Scalable data storage using BigQuery
- Schema-based structured streaming pipeline

## 📂 Project Structure
- `scripts/publisher.py` – Sends streaming data to Pub/Sub
- `scripts/dataflow_pipeline.py` – Processes and loads data into BigQuery

## ▶️ How to Run
1. Create Pub/Sub topic and subscription
2. Create BigQuery dataset and table
3. Run Dataflow pipeline
4. Start publisher script

## 📈 Example Query
```sql
SELECT * FROM `weather_dataset.weather_data`
ORDER BY timestamp DESC
LIMIT 10;
>>>>>>> 5efcb69 (Clean project structure)
