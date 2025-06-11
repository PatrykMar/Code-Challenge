import datetime
from datetime import datetime
import os
import json
import boto3
from boto3.dynamodb.conditions import Key


client = boto3.client('dynamodb')
dynamodb = boto3.resource("dynamodb")
table_name = os.getenv('DYNAMODB_TABLE')
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    print(event)
    body= {}
    status_code = 200
    headers = {
        'Content-Type': 'application/json'
    }
    request_json = json.loads(event['body'])
    print(request_json)
    try:
        fe = Key('email_address').eq(request_json['email_address']) & Key('password').eq(request_json['password'])
        response = table.scan(FilterExpression=fe)
        body = response['Items']
        print(body)
        if not body:
            body = "Failed to login user " + request_json['email_address']
        else:
            time_now = datetime.now()
            formated_time = time_now.strftime("%Y-%m-%d %H:%M:%S")
            table.update_item(
                Key={
                    'email_address': request_json['email_address']},
                    UpdateExpression="SET last_login = :updated",
                    ExpressionAttributeValues= {':updated': formated_time}
            )
            body = "Login user successful " + request_json['email_address']
    except Exception as e:
        status_code = 400
        body = "Failed to login user " + request_json['email_address']

    body = json.dumps(body)
    res = {
        'statusCode': status_code,
        "headers": headers,
        "body": body
    }

    return res

