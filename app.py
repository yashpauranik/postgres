import json
import Infodao


def lambda_handler(event, context):
    infObj = event["first_name"] , event["last_name"] , event["email"] , event["is_email_verified"] , event["mobile"]
    Infodao.insert(infObj)
    return table
lambda_handler(events,context)