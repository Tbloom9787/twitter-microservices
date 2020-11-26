import boto3
import random
import json

def send_dm(recipient, sender , message, quick_replies=None, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    message_ID = random.randint(0, 100)

    table = dynamodb.Table('Messages')
    response = table.put_item(
        Item={
            'message': message_ID,
            'recipient': recipient,
            'sender': sender,
            'message': message
        }
    )

    return response

if __name__ == "__main__":
    message = send_dm("Joe", "Bob", "Testing direct messaging here", 0)
    
    print("Message Success!")
    json.dumps(message)


