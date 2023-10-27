import boto3
import json 


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('jitto-challenge-items')

def lambda_handler(event, context):

    # get single item by id
    if event.get('id') != None:
        response = table.get_item(
            Key={
    	        'id': event.get('id')
            }
        )  
        
        if 'Item' in response:
            return response['Item']
        else:
           return {
            	'statusCode': '404',
                'body': 'Not found'
            }
        
    # list all items
    else:
        response = table.scan()
        print(response)
        if 'Items' in response:
           return response['Items']
        else:
            return {
                'statusCode': '404',
                'body': 'Not found'
        }
        
