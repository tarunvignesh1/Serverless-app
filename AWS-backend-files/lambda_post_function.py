import json
import boto3
from decimal import Decimal

# Initialize DynamoDB resource and specify the table name directly
dynamodb = boto3.resource('dynamodb')
table_name = 'WorkoutData'
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    try:
        # Extract username from query parameters
        username = event.get('queryStringParameters', {}).get('username')

        if not username:
            return {
                'statusCode': 400,
                'body': json.dumps('Missing username query parameter')
            }

        # Get item from DynamoDB
        response = table.query(
            KeyConditionExpression=boto3.dynamodb.conditions.Key('username').eq(username)
        )

        # Convert DynamoDB Decimal objects to native Python types
        items = response.get('Items', [])
        items = convert_decimals(items)

        # Return the fetched items
        return {
            'statusCode': 200,
            'body': json.dumps(items)
        }

    except Exception as e:
        print("Exception:", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error fetching data: {str(e)}')
        }

def convert_decimals(data):
    """ Convert DynamoDB Decimal objects to native Python types """
    if isinstance(data, list):
        return [convert_decimals(item) for item in data]
    elif isinstance(data, dict):
        return {k: convert_decimals(v) for k, v in data.items()}
    elif isinstance(data, Decimal):
        return float(data)
    else:
        return data
