# python_utils

## s3upload.py
```
usage: s3upload.py [-h] [-k KEY] [-s SECRET] [-d] [-v] [--version] dirs [dirs ...] bucket destination_path

Uploads a directory to an S3 bucket.

positional arguments:
  dirs                  local directories to upload
  bucket                the bucket to upload to
  destination_path      s3 directory to upload to

optional arguments:
  -h, --help            show this help message and exit
  -k KEY, --key KEY     AWS Access Key ID. Not recommended due to security risk.
  -s SECRET, --secret SECRET
                        AWS Secret Key. Definitely not recommended due to security risk.
  -d, --debug           Prints debug statements
  -v, --verbose         Becomes verbose
  --version             show program's version number and exit
```
Uploads multiple local directories to a specified location in an S3 bucket.
If key and secret arent within the paramters, it will ask securely via getpass.

Recommended Usage:
```
$ python s3upload.py [Multiple Directories, or just one] [bucket name] [bucket destination path]
```
Example
```
$ python s3upload.py ./result ./out ./logs scraping-bucket "scrapingstuff/websiteA" -k AI76U4D2F77H8I90U4SD
```
