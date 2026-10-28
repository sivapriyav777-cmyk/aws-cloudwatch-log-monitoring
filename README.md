
# AWS CloudWatch Log Monitoring

## Project Description
A Python-based log monitoring application
that retrieves and analyzes AWS CloudWatch logs.

## Technologies Used
- Python
- AWS CloudWatch Logs
- Boto3
- GitHub Actions
- JSON

## Features
- Retrieve logs from AWS CloudWatch
- Identify ERROR, WARNING and INFO messages
- Generate a JSON monitoring report
- Test using sample logs without AWS
- Run automated tests using GitHub Actions

## Installation
pip install -r requirements.txt

## Run Sample Monitoring
python cloudwatch_monitor.py

## Run Tests
python -m unittest discover -v

## AWS Configuration
Set USE_SAMPLE=false and LOG_GROUP_NAME
to enable CloudWatch log retrieval.

AWS credentials and region must also be
configured in the execution environment.

## Output
The application creates report.json
containing log counts by severity.
