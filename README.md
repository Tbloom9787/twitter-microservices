# twitter-microservices
Get Started:
* Set up DynamoDB Local with the following commands:
  sudo apt-get update
  sudo apt-get install awscli
  aws configure

* Install python requirements:
  sudo apt-get install python3-boto3
  sudo pip install flask-dynamo
  
* To run program:
  (dynamo_loader is a test loading for the user table and can be ran with: sudo python3 dynamo_loader.py but our focus is direct_messaging)
  
  Go to your local directory of ./dynamolocal in order to run the local database as:
  java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb
  
  Go to project folder and simply run:
  flask init
  
