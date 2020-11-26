import boto3
import random
import json

def sendDirectMessage(recipient, sender , message, quick_replies=None, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    if quick_replies == 1:
        message = "Hey, I'll back you back in a minute."
    elif quick_replies == 2:
        message = "In class, cannot talk."
    elif quick_replies == 3:
        message = "Sounds good!"
    elif quick_replies == 4:
        message = "I'll be leaving soon."
    elif quick_replies == 5:
        message = "Have a great day!"

    message_ID = random.randint(0, 1000)

    # message_ID is linked to the sender of the message
    table = dynamodb.Table('Messages')
    response = table.put_item(
        Item={
            'message_ID': message_ID,
            'recipient': recipient,
            'sender': sender,
            'message': message
        }
    )

    return response

def replyToDirectMessage(messageId, reply, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
    
    recipient_ID = random.randint(0, 1000)

    # message_ID is still linked to the sender so it is now reply_ID
    table = dynamodb.Table('Messages')
    response = table.put_item(
        Item={
            'message_ID': recipient_ID,
            'recipient': recipient,
            'sender': sender,
            'reply_ID': messageId,
            'message': reply
        }
    )

    return response


if __name__ == "__main__":
    sent_message = sendDirectMessage("Joe", "Bob", "Testing direct messaging here", 0)

    print("Message Success!")
    json.dumps(sent_message)


