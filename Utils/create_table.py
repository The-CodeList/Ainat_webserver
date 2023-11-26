import boto3

dynamodb = boto3.resource(
    "dynamodb",
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