# lambda_function file

import json
import boto3
import base64


s3 = boto3.client('s3')

def lambda_handler(event, context):
    """A function to serialize target data from S3"""

    # Get the s3 address from the Step Function event input
    key = "test/bicycle_s_000513.png"
    bucket = "sagemaker-us-east-1-325570208486"
    image_data = ""

    # Download the data from s3 to /tmp/image.png
    # s3.download_file(Bucket=bucket, Key=key, Filename=image_data)
    # s3 = boto3.client('s3')
    # input_bucket = s3_input_uri.split('/')[0]
    # input_object = '/'.join(s3_input_uri.split('/')[1:])
    # file_name = '/tmp/' + os.path.basename(input_object)
    s3.download_file(bucket, key, image_data)


    # We read the data from a file
    with open("/tmp/image.png", "rb") as f:
        image_data = base64.b64encode(f.read())

    # Pass the data back to the Step Function
    print("Event:", event.keys())
    return {
        'statusCode': 200,
        'body': {
            "image_data": image_data,
            "s3_bucket": bucket,
            "s3_key": key,
            "inferences": []
        }
    }
   

    
