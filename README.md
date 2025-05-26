# Mezmo → Fluent Bit → Chronosphere MVP

## Overview

This MVP demonstrates an observability pipeline with:
- A Python-based log generator (`app/log-generator.py`)
- A Fluent Bit configuration simulating Mezmo's pipeline (`fluentbit/fluent-bit.conf`)
- Architecture diagram placeholder (`assets/`)

## How to Run

1. Run the log generator:
```bash
python app/log-generator.py

2. Use Fluent Bit to process logs from `logs/app.log` and output them as structured JSON.

3. Forward Fluent Bit output to OpenTelemetry Collector → Chronosphere.

4. Alternatively, run the Docker file
   docker-compose up --build

5. All logs should be stored in a file called log
   
