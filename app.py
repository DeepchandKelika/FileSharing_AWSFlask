import os, json
import boto3
from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)

secret_key = os.urandom(24)

app.secret_key = secret_key.hex()

users = {
     'deepchand':'deep1234',
     'luffy':'luffy1234',
     'zoro':'zoro1234'
}



# AWS S3 configuration
s3_client = boto3.client(
    's3',
    aws_access_key_id='AWS_ACCESS_KEY_ID',
    aws_secret_access_key='AWS_SECRET_ACCESS_KEY',
    region_name='us-east-1'
)
s3_bucket_name = 'luffyfile'



lambda_client = boto3.client (
   'lambda',
    aws_access_key_id='AWS_ACCESS_KEY_ID',
    aws_secret_access_key='AWS_SECRET_ACCESS_KEY',
    region_name='us-east-1'
    )



@app.route("/")
def index():
     return render_template('login.html')


@app.route("/loginVerify", methods = ['POST'])
def loginVerify():
    username = request.form['username']
    password = request.form['password']
   # print(username)
    if username in users.keys() and users[username] == password:
         return render_template('fileshare.html')
    else:
         error = "Invalid Username or Password"
         return render_template("login.html", error = error)





@app.route('/upload', methods=['GET', 'POST'])
def upload():
    
    if request.method == 'POST':
        file = request.files['file']
        
        #username = request.form['username']
        emails = request.form.getlist('email')
        emails = [email for email in emails if email]
        #print(emails)
        
        if file:

            s3_client.upload_fileobj(file, s3_bucket_name, file.filename,ExtraArgs={ 'GrantRead': 'uri="http://acs.amazonaws.com/groups/global/AllUsers"'})


            #send_email_notifications(emails, file.filename)

            flash('File uploaded and emails sent successfully.', 'success')
            payload = {'emails': emails,
                       'fileName': file.filename
                       #'username' : username
                       }
            lambda_client.invoke(
            FunctionName='luffyFileShare',
            InvocationType='Event',
            Payload=json.dumps(payload))

            return render_template('fileshare.html')

    return render_template('fileshare.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
