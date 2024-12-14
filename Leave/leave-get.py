import json
import boto3

dynamodb = boto3.resource('dynamodb')
LEAVE_TABLE = 'LeaveTable'

def lambda_handler(event, context):
    table = dynamodb.Table(LEAVE_TABLE)
    
    response = table.scan()
    return {
        'statusCode': 200,
        'body': json.dumps(response['Items'])
    }
}
