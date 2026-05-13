"""Basic AWS Lambda handler."""

import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    """Entry point for the Lambda function.

    Parameters
    ----------
    event : dict
        Event payload passed to the function by the invoker.
    context : LambdaContext
        Runtime information provided by AWS Lambda.

    Returns
    -------
    dict
        An API Gateway-style response object.
    """
    logger.info("Received event: %s", json.dumps(event))

    name = "world"
    if isinstance(event, dict):
        # Support either a direct invocation payload or an API Gateway request.
        if "name" in event:
            name = event["name"]
        elif "queryStringParameters" in event and event["queryStringParameters"]:
            name = event["queryStringParameters"].get("name", name)

    body = {
        "message": f"Hello, {name}!",
        "input": event,
    }

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body),
    }
