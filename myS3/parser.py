import myS3.cmd

def add_s3_parser(subparsers):
    # create the parser for the "s3" command
    s3_parser = subparsers.add_parser('s3', help='s3 command help')
    s3_subparser = s3_parser.add_subparsers()

    ## create the parser for the "s3" sub-commands
    listBuckets_parser = s3_subparser.add_parser('buckets', help='list buckets')
    listBuckets_parser.set_defaults(func=myS3.cmd.list_buckets)

    createBucket_parser = s3_subparser.add_parser('create', help='create bucket')
    createBucket_parser.add_argument('name', action='store', type=str, help='bucket name')
    createBucket_parser.add_argument('acl', action='store', type=str, help="bucket acl ('private'|'public-read'|'public-read-write'|'authenticated-read')")
    createBucket_parser.add_argument('region', action='store', type=str, help='aws region')
    createBucket_parser.set_defaults(func=myS3.cmd.create_bucket)

    uploadObject_parser = s3_subparser.add_parser('upload', help='upload an object')
    uploadObject_parser.add_argument('name', action='store', type=str, help='bucket name')
    uploadObject_parser.add_argument('path_to_file', action='store', type=str, help='path to file to upload')
    uploadObject_parser.set_defaults(func=myS3.cmd.upload_object)

    emptyBucket_parser = s3_subparser.add_parser('empty', help='empty bucket')
    emptyBucket_parser.add_argument('name', action='store', type=str, help='bucket name')
    emptyBucket_parser.set_defaults(func=myS3.cmd.empty_bucket)

    deleteBucket_parser = s3_subparser.add_parser('delete', help='delete bucket')
    deleteBucket_parser.add_argument('name', action='store', type=str, help='bucket name')
    deleteBucket_parser.set_defaults(func=myS3.cmd.delete_bucket)