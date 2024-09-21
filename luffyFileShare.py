import boto3
import uuid

dynamodb = boto3.resource('dynamodb',
        aws_access_key_id='AWS_ACCESS_KEY_ID',
        aws_secret_access_key='AWS_SECRET_ACCESS_KEY',
        region_name='us-east-1')

table = dynamodb.Table('luffyDB')
ses = boto3.client('ses',
         aws_access_key_id='AWS_ACCESS_KEY_ID',
        aws_secret_access_key='AWS_SECRET_ACCESS_KEY',
        region_name='us-east-1')

def lambda_handler(event, context):
    try:
        emails = event['emails']
        filename = event['fileName']
        sender_email = "chandu.kelika@gmail.com"  
        subject = "File Sharing Notification"
        body = f"Dear user,\n\nA file named '{filename}' has been shared with you.\n\nYou can access it using the link: https://luffyfile.s3.us-east-1.amazonaws.com/{filename}\n\nBest regards,\nFile Sharing Tool"

        print(filename)
        
        response = ses.send_email(
            Source=sender_email,
            Destination={'ToAddresses': emails},
            Message={
                'Subject': {'Data':subject},
                'Body': {'Text': {'Data': body}},
            }
        )
        
        file_id = str(uuid.uuid4())
        
        file_info = {
        'fileID': file_id,  
        'FileName': filename
        #'UploadedBy': user_name, 
        }
        table.put_item(Item=file_info)
        
        return {
            'statusCode': 200,
            'body': 'Emails sent successfully.'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
        }
