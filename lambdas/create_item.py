import json
import boto3
import uuid

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("ItemsTable")

def lambda_handler(event, context):
    try:
        body = json.loads(event.get("body", "{}"))

      
        item = {
            "id": str(uuid.uuid4()),
            "name": body.get("name", "Untitled"),
            "description": body.get("description", "")
        }

        table.put_item(Item=item)

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Item created successfully",
                "item": item
            })
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
