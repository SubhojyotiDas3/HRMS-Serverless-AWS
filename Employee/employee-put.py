import json
import boto3

dynamodb = boto3.resource('dynamodb')
EMPLOYEE_TABLE = 'EmployeeTable'

def lambda_handler(event, context):
    body = json.loads(event['body'])
    table = dynamodb.Table(EMPLOYEE_TABLE)
    
    table.update_item(
        Key={'empId': body['empId']},
        UpdateExpression="SET empName = :name, empDept = :dept, empEmail = :email",
        ExpressionAttributeValues={
            ':name': body['empName'],
            ':dept': body['empDept'],
            ':email': body['empEmail']
        }
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Employee updated successfully!'})
    }
