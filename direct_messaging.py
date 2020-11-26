import boto3
import random

def send_dm(to, from ,message, quick_replies=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    
