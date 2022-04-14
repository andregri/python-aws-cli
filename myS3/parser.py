import myS3.cmd

def add_s3_parser(subparsers):
    # create the parser for the "s3" command
    s3_parser = subparsers.add_parser('s3', help='s3 command help')
    s3_subparser = s3_parser.add_subparsers()

    ## create the parser for the "s3" sub-commands
    s3_listBuckets_parser = s3_subparser.add_parser('buckets', help='list buckets')
    s3_listBuckets_parser.set_defaults(func=myS3.cmd.list_buckets)

    s3_createBucket_parser = s3_subparser.add_parser('create', help='create a bucket')
    s3_createBucket_parser.add_argument('bucket_name', action='store', type=str)
    s3_createBucket_parser.set_defaults(func=myS3.cmd.create_bucket)