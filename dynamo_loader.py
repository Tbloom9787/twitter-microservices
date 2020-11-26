import json

with open('user_data.json') as json_file:
    users = json.load(json_file)
    
    for user in users:
        username = user['username']
        password = user['password']
        email = user['email']

        response = table.put_item(
            Item = {
                'username': username,
                'password': password,
                'email': email,
            }
        )

        print("Put item successful..")
        print(json.dumps(response, indent=4))