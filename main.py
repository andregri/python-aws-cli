import argparse
import boto3

import myS3.cmd

# create the top-level parser
parser = argparse.ArgumentParser(
    description="AWS CLI written in Python for learning purpose"
)
subparsers = parser.add_subparsers()

# create the parser for the "ec2" command
ec2_parser = subparsers.add_parser('ec2', help='ec2 command help')
ec2_group = ec2_parser.add_mutually_exclusive_group()
ec2_group.add_argument('--describe', action='store_true')
ec2_group.add_argument('--monitor', type=str)
ec2_group.add_argument('--unmonitor', type=str)
ec2_group.add_argument('--start', type=str)
ec2_group.add_argument('--stop', type=str)

# create the parser for the "s3" command
s3_parser = subparsers.add_parser('s3', help='s3 command help')
s3_subparser = s3_parser.add_subparsers()

## create the parser for the "s3" sub-commands
s3_listBuckets_parser = s3_subparser.add_parser('buckets', help='list buckets')
s3_listBuckets_parser.set_defaults(func=myS3.cmd.list_buckets)

s3_createBucket_parser = s3_subparser.add_parser('create', help='create a bucket')
s3_createBucket_parser.add_argument('bucket_name', action='store', type=str)
s3_createBucket_parser.set_defaults(func=myS3.cmd.create_bucket)

options = parser.parse_args()
print(options)
options.func(**options.__dict__)