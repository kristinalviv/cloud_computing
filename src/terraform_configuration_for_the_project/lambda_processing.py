import json
from datetime import datetime
import boto3
from botocore.exceptions import ClientError

queue_client = boto3.client('sqs')
S3_client = boto3.client('s3')

bucket = 'processeddatafromsqs1terraform2'

def lambda_handler(event, context):
    queue_url = 'https://sqs.us-east-1.amazonaws.com/059479097961/queue'
    processed_time = datetime.now().strftime("%H:%M:%S")
    filename = f'{processed_time}.json'
    
    try:
        print(event)
        message = json.dumps(event)
        S3_client.put_object(Bucket=bucket, Key=filename, Body=message)
        
        return {
            'statusCode': 200,
            'body': json.dumps(f'Event:{event}, {filename}')
        }
    except ClientError as e:
        print('Error occured - ', e)
