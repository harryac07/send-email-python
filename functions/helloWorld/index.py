import json
import os


def handler(event, context):
    body = {
        "message": "Hello World!",
        "input": event
    }
    print(os.environ.get('STAGE', 'dev'))
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
