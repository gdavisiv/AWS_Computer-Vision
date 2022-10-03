#!/usr/bin/env python3
#Importing Necessary Libraries
import boto3
import exif

s3client = boto3.client('s3')
bucket = 'aws-test-img-bucket'
startAfter = '2020'
s3objects= s3client.list_objects_v2(Bucket=bucket, StartAfter=startAfter)

for object in s3objects['Contents']:
    tmp = (object['Key'])
    print(tmp)
#Add a new Metadata label to the file
#https://exif.readthedocs.io/en/latest/api_reference.html#image-attributes
#
#use 'maker_note' | 'maker' | 'xp_subject' | 'xp_keywords' possibly??