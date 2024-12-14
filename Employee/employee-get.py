import json
import boto3

dynamodb = boto3.resource('dynamodb')
EMPLOYEE_TABLE = 'EmployeeTable'

def lambda_handler(event, context):
    table = dynamodb.Table(EMPLOYEE_TABLE)
    
    response = table.scan()
    return {
        'statusCode': 200,
        'body': json.dumps(response['Items'])
    }
}
