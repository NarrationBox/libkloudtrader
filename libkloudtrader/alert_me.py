import os
import boto3
from botocore.exceptions import ClientError



def sms(number,message):
    try:
        client = boto3.client(
        "sns",
        aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
        region_name=os.environ['AWS_DEFAULT_REGION']
        )   
        topicarn=os.environ['SNS_TOPIC_ARN']
        client.subscribe(
        TopicArn=topicarn,
        Protocol='sms',
        Endpoint=number  
        )
        client.publish(Message=message, TopicArn=topicarn)
        print('SMS alert Created!')
    except Exception as e:
        raise ('Could not create an sms alert! Probabaly because you are running from your local machine. Please Push to your narwhal runtime to make it work.')


def email(email_id,message,sender="alerts@kloudtrader.com",subject="KloudTrader Narwhal Alerts"):
    SENDER = sender
    RECIPIENT = email_id
    AWS_REGION = os.environ['AWS_DEFAULT_REGION']
    SUBJECT = subject
    BODY_TEXT = message
    BODY_HTML = """<html>
    <head></head>
    <body>
    
    <p>For an queries please reply to this email
    <a href='mailto:support@kloudtrader.com'>
    </body>
    </html>
    """ 
 
    CHARSET = "UTF-8"
    client = boto3.client('ses',region_name=AWS_REGION)
    try:
        response = client.send_email(
        Destination={
            'ToAddresses': [
                RECIPIENT,
            ],
        },
        Message={
            'Body': {
                
                'Text': {
                    'Charset': CHARSET,
                    'Data': BODY_TEXT,
                },
            },
            'Subject': {
                'Charset': CHARSET,
                'Data': SUBJECT,
            },
        },
        Source=SENDER,
    )
        print('Email alert created!')
    except ClientError as e:
        raise (e.response['Error']['Message'])
    

def sms_and_email(number,email_id,message):
    sms(number,message)
    email(email_id,message)
    
