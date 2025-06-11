import json
import os
import boto3


client = boto3.client('dynamodb',region_name='eu-west-1')
dynamodb = boto3.resource("dynamodb", region_name='eu-west-1')
table_name = os.getenv('DYNAMODB_TABLE')
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    print(event)
    body= {}
    status_code = 200
    headers = {
        'Content-Type': 'application/json'
    }
    try:
        print(event['pathParameters']['email_address'])
        body = table.get_item(
            Key = {'email_address': event['pathParameters']['email_address']},
        )
        body = body["Item"]
        response_body = [
            {'name': body['name'], 'email_address': body['email_address'],
             'password': body['password'], 'last_login': body['last_login']},
        ]
        body = response_body
    except Exception as e:
        status_code = 400
        body = "Failed to get user " + event['pathParameters']['email_address']

    body = json.dumps(body)
    res = {
        'statusCode': status_code,
        "headers": headers,
        "body": body
    }

    return res

