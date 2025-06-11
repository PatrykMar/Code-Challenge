import json
import boto3
import os


client = boto3.client('dynamodb',region_name='eu-west-1')
dynamodb = boto3.resource("dynamodb", region_name='eu-west-1')
table_name = os.getenv('DYNAMODB_TABLE')
tableName = 'GenDBTablev1'

def lambda_handler(event, context):
    print(event)
    body= {}
    status_code = 200
    headers = {
        'Content-Type': 'application/json'
    }
    try:
        table.delete_item(
            Key = {'email_address': event['pathParameters']['email_address']},
        )
        body = 'Deleted user ' + event['pathParameters']['email_address']
    except Exception as e:
        status_code = 400
        body = "Failed to delete user " + event['pathParameters']['email_address']

    body = json.dumps(body)
    res = {
        'statusCode': status_code,
        "headers": headers,
        "body": body
    }

    return res

