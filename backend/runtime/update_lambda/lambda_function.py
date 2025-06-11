import json
import os

import boto3


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

        table.put_item(
            Item={
                'email_address': request_json['email_address'],
                'password': request_json['password'],
                'name': request_json['name'],
                'last_login': ""
            })
        body = 'Create User ' + request_json['name']
    except Exception as e:
        status_code = 400
        body = "Failed to create user " + request_json['name']

    body = json.dumps(body)
    res = {
        'statusCode': status_code,
        "headers": headers,
        "body": body
    }

    return res

