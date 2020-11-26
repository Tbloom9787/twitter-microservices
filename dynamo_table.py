import boto3


def create_user_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource(
            'dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")

    table = dynamodb.create_table(
        TableName='Users',
        KeySchema=[
            {
                'AttributeName': 'username',
                'KeyType': 'HASH'   # Partition key
            },
            {
                'AttributeName': 'password',
                'KeyType': 'RANGE'  # Sort Key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'username',
                'AttributeType': 'S',
            },
            {
                'AttributeName': 'password',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )

    return table

def create_dm_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")

    table = dynamodb.create_table(
        TableName = 'Messages',
        KeySchema = [
            {
                'AttributeName': 'message_ID',
                'KeyType': 'HASH'   # Partition key
            },
            {
                'AttributeName': 'recipient',
                'KeyType': 'RANGE'  # Sort Key
            }
        ],
        AttributeDefinitions = [
            {
                'AttributeName': 'message',
                'AttributeType': 'S',
            },
            {
                'AttributeName': 'recipient',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput = {
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )

    return table

if __name__ == "__main__":
    user_table = create_user_table()
    print("Table status:", user_table.table_status)
    
    dm_table = create_dm_table()
    print("Table status:", dm_table.table_status)
