import boto3

dynamodb = boto3.resource(
    "dynamodb",
    aws_access_key_id=os.environ.get("ACCESS_KEY"),
    aws_secret_access_key=os.environ.get("SECRET_KEY"),
    region_name=os.environ.get("REGION")
)

# Create dynamo table
table = dynamodb.create_table(
    TableName = "users",
    KeySchema = [
        {
            "AttributeName": "email",
            "KeyType": "HASH"
        }
    ],
    AttributeDefinitions = [
        {
            "AttributeName": "email",
            "AttributeType": "S"
        }
    ],
    ProvisionedThroughput = {
        "ReadCapacityUnits": 5,
        "WriteCapacityUnits": 5
    }
)

table.meta.client.get_waiter("table_exists").wait(TableName="users")

print(table.item_count)