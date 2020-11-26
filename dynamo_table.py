import boto3

def create_dm_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.create_table(
        TableName = 'Messages',
        KeySchema = [
            {
                'AttributeName': 'message',
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
    dm_table = create_dm_table()
    print("Table status:", dm_table.table_status)
