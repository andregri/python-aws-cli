# Python AWS CLI

# EC2
```
python-aws-cli ec2 
    --describe-instances
    --monitor <instance id>
    --unmonitor <instance id>
    --start <instance id>
    --stop <instance id>
    --reboot <instance id>
```

# S3
Example using the commands:
```
python main.py s3 create andregri-bucket public-read
python main.py s3 buckets
python main.py s3 upload andregri-bucket README.md
python main.py s3 upload andregri-bucket requirements.txt
python main.py s3 empty andregri-bucket
python main.py s3 delete andregri-bucket
```