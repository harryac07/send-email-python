import json
import os
import boto3

client = boto3.client('sesv2')


def handler(event, context):
    if not 'receiver' in event:
        event['receiver'] = 'test@test.com'
    SENDER_EMAIl = os.environ.get('SENDER_EMAIL') or 'test@test.com'

    client.send_email(
        FromEmailAddress=SENDER_EMAIl,
        Destination={
            'ToAddresses': [
                event['receiver'],
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
