import json
import os
import boto3

client = boto3.client('sesv2')


def handler(event, context):
    receiver = (json.loads(event['body'])).get('receiver') or 'test@test.com'
    sender = os.environ.get('SENDER_EMAIL') or 'test@test.com'

    client.send_email(
        FromEmailAddress=sender,
        Destination={
            'ToAddresses': [
                receiver,
            ]
        },
        Content={
            'Simple': {
                'Subject': {
                    'Data': 'Test email',
                    'Charset': 'UTF-8'
                },
                'Body': {
                    'Html': {
                        'Data': 'Hello there',
                        'Charset': 'UTF-8'
                    }
                }
            }
        }
    )
    response = {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Message sent!"
        })
    }
    return response
