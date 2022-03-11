import argparse
import boto3

parser = argparse.ArgumentParser(
    description="AWS CLI written in Python for learning purpose"
)

subparsers = parser.add_subparsers()

ec2_parser = subparsers.add_parser('ec2')
ec2_group = ec2_parser.add_mutually_exclusive_group()
ec2_group.add_argument('--describe', action='store_true')
ec2_group.add_argument('--monitor', type=str)
ec2_group.add_argument('--unmonitor', type=str)
ec2_group.add_argument('--start', type=str)
ec2_group.add_argument('--stop', type=str)

args = parser.parse_args()

print(args)