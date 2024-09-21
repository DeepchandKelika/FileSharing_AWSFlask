# Flask-AWS-FileShare

A web-based file sharing tool built using Python, Flask, and integrated with AWS services like S3, DynamoDB, and SES.

## Overview

This project allows users to upload files, which are stored in an AWS S3 bucket. The application sends notifications using AWS SES and stores file metadata in DynamoDB.

## Video Demonstration
- Please refer FileSharing_AWS.mp4 file to watch the demonstration.

## Features

- **User Authentication**: Simple login system for secure access.
- **File Uploads**: Users can upload files to an AWS S3 bucket.
- **Email Notifications**: Notifies users via email using AWS SES after successful uploads.
- **File Metadata Storage**: Uses DynamoDB to store file metadata and user information.

## Prerequisites

- **Python 3.x**
- **AWS Account** with access to S3, DynamoDB, and SES
- **Flask**, **boto3* 


- luffyFileShare.py is used in AWS Lambda function to handle file metadata processing and send email notifications through SES after a file is uploaded to S3.
