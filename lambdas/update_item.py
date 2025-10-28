import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("ItemsTable")

def lambda_handler(event, context):
    try:
        # Extract ID from path
        item_id = event["pathParameters"]["id"]
        body = json.loads(event.get("body", "{}"))

        # Update item
        table.update_item(
            Key={"id": item_id},
            UpdateExpression="SET #n = :n, description = :d",
            ExpressionAttributeNames={"#n": "name"},
            ExpressionAttributeValues={
                ":n": body.get("name", ""),
                ":d": body.get("description", "")
            }
        )

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Item updated successfully"})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
