import json
import boto3

dynamodb = boto3.resource('dynamodb')
LEAVE_TABLE = 'LeaveTable'

def lambda_handler(event, context):
    body = json.loads(event['body'])
    table = dynamodb.Table(LEAVE_TABLE)
    
    # Validate required fields
    if 'leaveId' not in body or 'leaveDays' not in body:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'leaveId and leaveDays are required!'})
        }
    
    # Update the leave record
    table.update_item(
        Key={'leaveId': body['leaveId']},
        UpdateExpression="SET leaveDays = :days",
        ExpressionAttributeValues={
            ':days': body['leaveDays']
        }
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Leave record updated successfully!'})
    }
