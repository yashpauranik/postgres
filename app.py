from Infodao import *
def lambda_handler(event, context):
    infoObj = event["first_name"] , event["last_name"] , event["email"] , event["is_email_verified"] , event["mobile"]
    drop()
    if create() == True :
        return insert(infoObj)

event = {
  "first_name": "jo",
  "last_name": "Add",
  "email": "jaada@gmail",
  "is_email_verified": True,
  "mobile": "0909000"
}
response = lambda_handler(event,'')
print(response)
