import json
from datetime import datetime
import boto3
from botocore.exceptions import ClientError

queue_client = boto3.client('sqs')

def lambda_handler(event, context):
    try:
        queue_url = 'https://sqs.us-east-1.amazonaws.com/059479097961/queue'
        invocation_time = datetime.now().strftime("%H:%M:%S")
        parsed = event['body'] 
        message = queue_client.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps({"time": invocation_time, "number": parsed, "request_id": context.aws_request_id}),
            MessageGroupId='http')
        print(message)
        return {
            'statusCode': 200,
            "isBase64Encoded": False,
            'body': json.dumps(f"Triggered at {invocation_time}. Number {event['body']}")
        }
    except ClientError as e:
        print('Error occur - ', e)
   