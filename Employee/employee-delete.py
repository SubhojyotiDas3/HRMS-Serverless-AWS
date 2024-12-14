import json
import boto3

dynamodb = boto3.resource('dynamodb')
EMPLOYEE_TABLE = 'EmployeeTable'

def lambda_handler(event, context):
    empId = event['pathParameters']['empId']
    table = dynamodb.Table(EMPLOYEE_TABLE)
    
    table.delete_item(Key={'empId': empId})
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Employee deleted successfully!'})
    }
