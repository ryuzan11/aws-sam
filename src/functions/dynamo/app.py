import json
from db.dynamo import create_dynamodb_client, create_scan_input, execute_scan
from util import Logger

log = Logger('dynamo')


def lambda_handler(event, context):
    http_method = event.get('httpMethod')
    log.info(event)
    log.info(http_method)

    try:

        dynamodb_client = create_dynamodb_client(region='ap-northeast-1')

        scan_input = create_scan_input('Item')

        scan_response = execute_scan(dynamodb_client, scan_input)

    except Exception as e:
        log.error(e)
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'hello world'
            })
        }

    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'hello world',
            'dbResponse': scan_response
        })
    }
