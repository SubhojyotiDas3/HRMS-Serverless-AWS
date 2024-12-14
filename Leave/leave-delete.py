import json
import boto3

dynamodb = boto3.resource('dynamodb')
LEAVE_TABLE = 'LeaveTable'

def lambda_handler(event, context):
    empId = event['pathParameters']['empId']
    table = dynamodb.Table(LEAVE_TABLE)
    
    response = table.scan(
        FilterExpression="empId = :empId",
        ExpressionAttributeValues={':empId': empId}
    )
    
    for item in response['Items']:
        table.delete_item(Key={'leaveId': item['leaveId']})
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Leave record(s) deleted successfully!'})
    }
