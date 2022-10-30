from Infodao import *
def lambda_handler(event, context):
    infoObj = event["first_name"] , event["last_name"] , event["email"] , event["is_email_verified"] , event["mobile"]
    return insert(infoObj)

event = {
  "first_name": "john",
  "last_name": "Azam",
  "email": "johnzam@gmail",
  "is_email_verified": True,
  "mobile": "8889998800"
}
response = lambda_handler(event,'')
print(response)
