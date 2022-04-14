import boto3

def list_buckets():
    print('List of buckets')

def create_bucket(**kwargs):
    print(f'Creating bucket {kwargs["bucket_name"]}')