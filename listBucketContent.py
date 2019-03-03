#!/usr/bin/env python3.6

import boto3
import sys
s3 = boto3.resource('s3')

bcName = sys.argv[1]

def list_bucket_objects():
    for obj in s3.Bucket(bcName).objects.all():
        #print.(obj)
        print("--> ", obj.bucket_name, obj.key)

list_bucket_objects()
