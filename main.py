import argparse
import boto3

from myS3.parser import add_s3_parser

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

add_s3_parser(subparsers)

options = parser.parse_args()
print(options)
options.func(**options.__dict__)