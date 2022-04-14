import boto3
from pprint import pprint
import logging
from pathlib import Path

def list_buckets(**kwargs):
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    pprint(response)

def create_bucket(**kwargs):
    try:
        s3 = boto3.client('s3')
        response = s3.create_bucket(
            Bucket=kwargs['name'],
            ACL=kwargs['acl'],
            CreateBucketConfiguration={ 'LocationConstraint': kwargs['region'] }
        )
    except Exception as e:
        logging.error(e)
    else:
        pprint(response)

def upload_object(**kwargs):
    def callback(file_size):
        def cb(n_bytes):
            print(f'Uploaded {n_bytes} / {file_size} bytes ({n_bytes / file_size * 100}%)')
        return cb

    try:
        s3 = boto3.client('s3')
        filepath = Path(kwargs['path_to_file'])
        filename = filepath.name
        with open(filepath, 'rb') as data:
            s3.upload_fileobj(
                Bucket=kwargs['name'],
                Fileobj=data,
                Key=filename,
                Callback=callback(filepath.stat().st_size)
            )

    except Exception as e:
        logging.error(e)

def empty_bucket(**kwargs):
    try:
        s3 = boto3.client('s3')
        objects = s3.list_objects(Bucket=kwargs['name'])
        objs_to_delete = {
            'Objects': [{'Key': obj['Key']} for obj in objects['Contents']]
        }
        response = s3.delete_objects(Bucket=kwargs['name'], Delete=objs_to_delete)
        pprint(response)

    except Exception as e:
        logging.error(e)

def delete_bucket(**kwargs):
    try:
        s3 = boto3.client('s3')
        response = s3.delete_bucket(Bucket=kwargs['name'])
        pprint(response)
    
    except Exception as e:
        logging.error(e)