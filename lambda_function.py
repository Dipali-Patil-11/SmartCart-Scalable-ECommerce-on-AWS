import json
import boto3
import uuid

# DynamoDB Resource
dynamodb = boto3.resource('dynamodb')

# Tables
products_table = dynamodb.Table('SmartCart')
cart_table = dynamodb.Table('SmartCartCart')


def lambda_handler(event, context):

    # Handle CORS Preflight Request
    if event.get("httpMethod") == "OPTIONS":
        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS,POST"
            },
            "body": ""
        }

    try:
        # Read Request Body
        body = json.loads(event["body"])

        product_id = body["ProductID"]

        # Save Cart Item
        cart_table.put_item(
            Item={
                "CartID": "C-" + str(uuid.uuid4()),
                "ProductID": product_id,
                "Quantity": 1,
                "Status": "Added"
            }
        )

        # Success Response
        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS,POST",
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "message": "Product Added Successfully"
            })
        }

    except Exception as e:

        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS,POST",
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "error": str(e)
            })
        }
