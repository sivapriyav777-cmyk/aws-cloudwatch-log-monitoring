
import boto3
import json
import os
from datetime import datetime, timedelta, timezone
from collections import Counter


def fetch_cloudwatch_logs():
    client = boto3.client("logs")

    log_group = os.environ["LOG_GROUP_NAME"]

    end_time = datetime.now(timezone.utc)
    start_time = end_time - timedelta(hours=1)

    paginator = client.get_paginator("filter_log_events")

    messages = []

    for page in paginator.paginate(
        logGroupName=log_group,
        startTime=int(start_time.timestamp() * 1000),
        endTime=int(end_time.timestamp() * 1000)
    ):
        for event in page.get("events", []):
            messages.append(event["message"])

    return messages


def analyze_logs(messages):
    counts = Counter()

    for message in messages:
        text = message.upper()

        if "ERROR" in text:
            counts["ERROR"] += 1
        elif "WARNING" in text:
            counts["WARNING"] += 1
        elif "INFO" in text:
            counts["INFO"] += 1
        else:
            counts["OTHER"] += 1

    return {
        "total_logs": len(messages),
        "error_count": counts["ERROR"],
        "warning_count": counts["WARNING"],
        "info_count": counts["INFO"],
        "other_count": counts["OTHER"]
    }


def main():
    use_sample = os.getenv("USE_SAMPLE", "true").lower()

    if use_sample == "true":
        with open("sample_logs.txt", encoding="utf-8") as file:
            messages = file.read().splitlines()
    else:
        messages = fetch_cloudwatch_logs()

    report = analyze_logs(messages)

    with open("report.json", "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)

    print("CloudWatch Log Monitoring Report")
    print(json.dumps(report, indent=4))


if __name__ == "__main__":
    main()
