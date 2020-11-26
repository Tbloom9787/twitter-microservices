import json, boto3

dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

with open('user_data.json') as json_file:
    users = json.load(json_file)
    
    table = dynamodb.Table('Users')
    for user in users:
        username = user['username']
        password = user['password']

        response = table.put_item(Item=user)

        print("Put item successful..")
        print(json.dumps(response, indent=4))
