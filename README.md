# Web API with AWS
This API allows users to retrieve a full table, retrieve a specific item, and add a new item to a DynamoDB table.  

## Structure
Utilize AWS Lambda for handling API requests, Amazon API Gateway for API management and routing, and AWS DynamoDB as the database for storing items.

## Setup

```bash
npm install -g serverless
```

## Deploy

In order to deploy the endpoint simply run

```bash
serverless deploy
```

## Usage

### List all items 
    curl https://y5uaxpcqy8.execute-api.us-east-1.amazonaws.com/prod/jitto-challenge

Example Result:

    [
      {
          "description": "idk",
          "id": "2",
          "name": "Apple"
      },
      {
          "description": "hello!",
          "id": "1",
          "name": "Julia"
      }
    ]

### Get one item
    # Replace the <id> part with a real id from your todos table
    curl https://y5uaxpcqy8.execute-api.us-east-1.amazonaws.com/prod/jitto-challenge?id=<id>

Example Result:

    {
      "description": "hello!",
      "id": "1",
      "name": "Julia"
    }


### Add new item
    curl -X POST https://y5uaxpcqy8.execute-api.us-east-1.amazonaws.com/prod/jitto-challenge --data '{ "id": <id>, "name": <name>, "description": <description> }'

Result:

    {
        "statusCode": 200,
        "message": "item has been added"
    }


## Scaling

### AWS Lambda

By default, AWS Lambda limits the total concurrent executions across all functions within a given region to 100. The default limit is a safety limit that protects you from costs due to potential runaway or recursive functions during initial development and testing. To increase this limit above the default, follow the steps in [To request a limit increase for concurrent executions](http://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html#increase-concurrent-executions-limit).

### DynamoDB

When you create a table, you specify how much provisioned throughput capacity you want to reserve for reads and writes. DynamoDB will reserve the necessary resources to meet your throughput needs while ensuring consistent, low-latency performance. You can change the provisioned throughput and increase or decrease capacity as needed.

This can be done via settings in the `serverless.yml`.

```yaml
  ProvisionedThroughput:
    ReadCapacityUnits: 1
    WriteCapacityUnits: 1
```
