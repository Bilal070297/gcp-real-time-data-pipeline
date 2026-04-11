import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import json

class ParseMessage(beam.DoFn):
    def process(self, element):
        data = json.loads(element.decode("utf-8"))
        yield {
            "city": data["city"],
            "temperature": float(data["temperature"]),
            "timestamp": float(data["timestamp"])
        }

def run():
    project_id = "project-93921294-15bc-440f-acb"
    subscription = "projects/{}/subscriptions/weather-sub".format(project_id)

    table_spec = "{}:weather_dataset.weather_data".format(project_id)

    options = PipelineOptions(
        streaming=True,
        project=project_id,
        region="europe-west1",
        temp_location="gs://your-bucket/temp"
    )

    with beam.Pipeline(options=options) as p:
        (
            p
            | "Read from PubSub" >> beam.io.ReadFromPubSub(subscription=subscription)
            | "Parse JSON" >> beam.ParDo(ParseMessage())
            | "Write to BigQuery" >> beam.io.WriteToBigQuery(
    table_spec,
    schema="city:STRING, temperature:FLOAT, timestamp:FLOAT",
    write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND,
    create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED
)
        )

if __name__ == "__main__":
    run()