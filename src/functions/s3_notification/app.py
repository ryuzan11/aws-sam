import os
import json
import urllib.parse
import boto3

print("Loading function")

s3 = boto3.client("s3")
TEST_FUNCTION_NAME = os.environ.get("TEST_FUNCTION_NAME")


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    key = urllib.parse.unquote_plus(event["Records"][0]["s3"]["object"]["key"], encoding="utf-8")

    try:
        # 受け取ったS3データからS3接続できることを確認
        s3_response = s3.get_object(Bucket=bucket, Key=key)
        print("CONTENT TYPE: " + s3_response["ContentType"])
    except Exception as e:
        print(e)
        print("Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.".format(key, bucket))
        raise e

    payload = json.dumps({
        "param1": "param1"
    })

    print(TEST_FUNCTION_NAME)

    try:

        print("lambda invoke開始")
        invoke_lambda_response = boto3.client("lambda").invoke(
            FunctionName=TEST_FUNCTION_NAME,
            InvocationType="Event",
            Payload=payload
        )

        print(invoke_lambda_response)

    except Exception as e:
        print(e)
        raise e

    return
