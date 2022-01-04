import json
from util import Logger

log = Logger("test/lambda")


def lambda_handler(event, context):
    request_body = event.get("body")
    print(event)

    log.info(request_body)

    return {
        'statusCode': 200,
        'body': json.dumps({
            "requestBody": request_body
        })
    }
