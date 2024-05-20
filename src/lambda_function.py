import json
import boto3
import requests

sns = boto3.client('sns')

def lambda_handler(event, context):
    data = fetch_performance_data()
    changes = detect_significant_changes(data)
    
    if changes:
        send_alert(changes)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Performance monitoring completed!')
    }

def fetch_performance_data():
    # Placeholder for actual API call to fetch performance data
    response = requests.get('https://api.example.com/performance')
    return response.json()

def detect_significant_changes(data):
    # Placeholder for actual logic to detect significant changes
    changes = []
    for metric in data['metrics']:
        if metric['change'] > threshold:
            changes.append(metric)
    return changes

def send_alert(changes):
    message = f"Significant changes detected: {changes}"
    sns.publish(
        TopicArn='arn:aws:sns:region:account-id:topic-name',
        Message=message,
        Subject='Performance Alert'
    )
