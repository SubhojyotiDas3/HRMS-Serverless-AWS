import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
EMPLOYEE_TABLE = 'EmployeeTable'

def lambda_handler(event, context):
    body = json.loads(event['body'])
    table = dynamodb.Table(EMPLOYEE_TABLE)
    
    item = {
        'empId': body.get('empId', str(uuid.uuid4())),
        'empName': body['empName'],
        'empDept': body['empDept'],
        'empEmail': body['empEmail']
    }
    
    table.put_item(Item=item)
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Employee added successfully!', 'employee': item})
    }

