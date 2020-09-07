
__author__ = "David ES LEE"
__version__ = "0.1.0"
__license__ = "MIT"

import sys
import os
import logging
import argparse
import getpass

import boto3

def uploadDirectory(aws_access_key, aws_secret, local_directory, bucket, destination):

    client = boto3.client('s3')

    for root, dirs, files in os.walk(local_directory):
        for filename in files:

            local_path = os.path.join(root, filename)

            relative_path = os.path.relpath(local_path, local_directory)
            s3_path = os.path.join(destination, relative_path)

            logging.info(f'Searching {s3_path} in {bucket}')
            try:
                client.head_boject(Bucket=bucket, Key=s3_path)
                logging.info(f'Path found on S3! Skipping {s3_path}')
            except:
                logging.info(f'Uploading {s3_path}')
                client.upload_file(local_path, bucket, s3_path)

def main(args):

    AWS_ACCESS_KEY_ID = ''
    AWS_SECRET = ''

    if args.key is None:
        AWS_ACCESS_KEY_ID = getpass.getpass(prompt="Please input your AWS Acces Key ID: ")
    if args.secret is None:
        AWS_SECRET = getpass.getpass(prompt="Please input your AWS Secret Key: ")

    for directory in args.dirs:
        uploadDirectory(AWS_ACCESS_KEY_ID, AWS_SECRET, directory, args.bucket, args.destination_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Uploads a directory to an S3 bucket.')
    parser.add_argument(
        'dirs', nargs="+", help='local directories to upload'
    )
    parser.add_argument(
        'bucket', help='the bucket to upload to'
    )
    parser.add_argument(
        'destination_path', help='s3 directory to upload to'
    )
    parser.add_argument(
        '-k', '--key', help="AWS Access Key ID. Not recommended due to security risk."
    )
    parser.add_argument(
        '-s', '--secret', help='AWS Secret Key. Definitely not recommended due to security risk.'
    )
    parser.add_argument(
        '-d', '--debug',
        help="Prints debug statements",
        action="store_const", dest="loglevel", const=logging.DEBUG,
        default=logging.WARNING
    )
    parser.add_argument(
        '-v', '--verbose',
        help="Becomes verbose",
        action='store_const', dest='loglevel', const=logging.INFO,
    )
    parser.add_argument(
        '--version',
        action="version",
        version="%(prog)s (version {version})".format(version=__version__)
    )

    args = parser.parse_args()
    logging.basicConfig(
        level=args.loglevel,
        handlers = [
            logging.FileHandler('debug.log'),
            logging.StreamHandler()
        ]
    )

    main(args)
