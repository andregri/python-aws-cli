import boto3

client = boto3.client('ec2')

def describe_instances():
    response = ec2.describe_instances()
    return response