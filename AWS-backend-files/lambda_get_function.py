import json
import boto3
from decimal import Decimal
from datetime import datetime

# Initialize DynamoDB resource and specify the table name directly
dynamodb = boto3.resource('dynamodb')
table_name = 'WorkoutData'
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    try:
        # Extract and parse the input data from the event body
        body = json.loads(event.get('body', '{}'))
        username = body.get('username')
        workout_day = body.get('workoutDay')
        hours = body.get('hours')
        workout_date = body.get('workoutDate')

        # Log the received data for debugging
        print("Received data:", body)

        # Check if all necessary data is present
        if not username or not workout_day or not hours or not workout_date:
            return {
                'statusCode': 400,
                'body': json.dumps('Missing one or more required fields')
            }

        # Convert workout_date to ISO 8601 format if necessary
        try:
            workout_date = datetime.strptime(workout_date, '%Y-%m-%d').isoformat()
        except ValueError:
            return {
                'statusCode': 400,
                'body': json.dumps('Invalid date format, should be YYYY-MM-DD')
            }

        # Put the item in DynamoDB
        table.put_item(
            Item={
                'username': username,
                'workoutDay': workout_day,
                'hours': str(hours),  # Ensure hours is stored as Decimal
                'workoutDate': workout_date
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps('Workout data saved successfully!')
        }

    except Exception as e:
        print("Exception:", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error saving data: {str(e)}')
        }
