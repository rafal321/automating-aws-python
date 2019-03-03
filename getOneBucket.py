#!/usr/bin/env python3.6
#getOneBucket.py

import boto3


s3 = boto3.resource('s3')
bucket = s3.Bucket('acg-raf-devops')

def list_bucket_objects():
    for obj in s3.Bucket('acg-raf-devops').objects.all():
        #print.(obj)
        print(">>> ", obj.bucket_name, obj.key)

list_bucket_objects()



