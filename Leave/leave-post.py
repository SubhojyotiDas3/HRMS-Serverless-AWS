import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
LEAVE_TABLE = 'LeaveTable'

def lambda_handler(event, context):
    body = json.loads(event['body'])
    table = dynamodb.Table(LEAVE_TABLE)
    
    item = {
        'leaveId': str(uuid.uuid4()),
        'empId': body['leaveEmpId'],
        'leaveDays': body['leaveDays']
    }
    
    table.put_item(Item=item)
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Leave record added successfully!', 'leave': item})
    }
