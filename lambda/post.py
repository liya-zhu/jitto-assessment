import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('jitto-challenge-items')

def lambda_handler(event, context):
    table.put_item(Item=event)
    return {
        'statusCode': 200,
        'message': "item has been added"
    }