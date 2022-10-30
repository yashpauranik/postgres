import json

def lambda_handler(event, context):
    table = event["id"] , event["first_name"] , event["last_name"] , event["email"] , event["is_email_verified"] , event["mobile"]
    return table