HRMS System Project

This project is a basic HRMS (Human Resource Management System) application built using AWS services. It provides functionalities to manage employee details and leave records through a web interface. The backend is powered by AWS Lambda and DynamoDB, while the frontend is hosted on Amazon S3.

Features

Employee Management

Add or update employee details (Name, Email, Department).

Delete an employee record.

View a list of all employees.

Search employees by name.

Leave Management

Add or update leave records.

Delete leave records.

Search Functionality

Search employees by their names and display their details.

Architecture

AWS Services Used:

Amazon S3: Hosts the static frontend (HTML, CSS, JavaScript).

AWS Lambda: Handles backend logic for CRUD operations.

Amazon API Gateway: Acts as an interface between the frontend and Lambda functions.

Amazon DynamoDB: Stores employee and leave records.

Prerequisites

AWS account.

Basic knowledge of AWS Lambda, DynamoDB, and API Gateway.

Node.js or Python environment for testing API calls (optional).

Setup Instructions

1. Create DynamoDB Tables

Employee Table:

Table Name: EmployeeTable

Primary Key: empId (String)

Leave Table:

Table Name: LeaveTable

Primary Key: leaveId (String)

2. Configure Lambda Functions

Roles and Permissions

IAM Role:

Create an IAM Role for the Lambda functions with the following permissions:

AWSLambdaBasicExecutionRole

AmazonDynamoDBFullAccess

Attach this role to all Lambda functions.

Lambda Functions

Create the following Lambda functions for each API:

Employee Management:

POST Employee: Adds a new employee.

PUT Employee: Updates employee details.

DELETE Employee: Deletes an employee record.

GET Employee: Fetches all employees or fetches an employee by empId.

Leave Management:

POST Leave: Adds a new leave record.

PUT Leave: Updates leave details.

DELETE Leave: Deletes a leave record.

GET Leave: Fetches all leave records or fetches a leave record by leaveId.

Refer to the provided Python scripts for each Lambda function.

3. Set Up API Gateway

Create a new REST API.

Define resources for /employee and /leave.

Create methods (POST, PUT, DELETE, GET) for each resource.

Integrate each method with the corresponding Lambda function.

Deploy the API to a stage and note the endpoint URL.

4. Host the Frontend on S3

Create an S3 bucket.

Enable static website hosting for the bucket.

Upload the provided HTML file (which includes CSS and JavaScript).

Update the API Gateway URL in the JavaScript section of the HTML file.

Running the Project

Open the hosted URL in your browser (provided by S3).

Use the interface to perform CRUD operations on employees and leave records.

Search for employees by name using the search functionality.

Files Provided

HTML File: Contains the UI for the project (includes embedded CSS and JavaScript).

Python Lambda Scripts: Separate scripts for each API functionality.

README File: Project documentation.

Additional Notes

Make sure the IAM role attached to Lambda has permissions to access DynamoDB.

Validate inputs on the frontend and backend to avoid invalid data.

Test the API Gateway endpoints using Postman or cURL if needed.

Example API Gateway Endpoints

Employee Management:

POST: https://<api-gateway-url>/employee

PUT: https://<api-gateway-url>/employee

DELETE: https://<api-gateway-url>/employee/{empId}

GET: https://<api-gateway-url>/employee (fetch all employees)

Leave Management:

POST: https://<api-gateway-url>/leave

PUT: https://<api-gateway-url>/leave

DELETE: https://<api-gateway-url>/leave/{leaveId}

GET: https://<api-gateway-url>/leave (fetch all leaves)

Future Enhancements

Add user authentication (e.g., AWS Cognito) for secure access.

Include advanced search and filtering options.

Expand leave management to support leave approvals and rejections.
