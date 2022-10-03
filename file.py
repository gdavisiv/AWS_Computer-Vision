#!/usr/bin/env python3
#Importing Necessary Libraries
import boto3
def iterate_bucket_items(bucket):
    client = boto3.client('s3')
    paginator = client.get_paginator('list_objects_v2')
    page_iterator = paginator.paginate(Bucket='aws-test-img-bucket')
    for page in page_iterator:
        if page['KeyCount'] > 0:
            for item in page['Contents']:
                yield item
for i in iterate_bucket_items(bucket='aws-test-img-bucket'):
    print(i)
    print(bucket)
         

s3client = boto3.client('s3')
bucket = 'aws-test-img-bucket'
startAfter = '2020'
s3objects= s3client.list_objects_v2(Bucket=bucket, StartAfter=startAfter )

for object in s3objects['Contents']:
    print(object['Key']) 