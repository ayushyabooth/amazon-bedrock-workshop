import json
import os
import sys

import boto3
import botocore

module_path = ".."
sys.path.append(os.path.abspath(module_path))
from utils import bedrock, print_ww


# ---- ⚠️ Un-comment and edit the below lines as needed for your AWS setup ⚠️ ----

os.environ["AWS_DEFAULT_REGION"] = "us-east-1" # E.g. "us-east-1"
# os.environ["AWS_PROFILE"] = "<YOUR_PROFILE>"
# os.environ["BEDROCK_ASSUME_ROLE"] = "<YOUR_ROLE_ARN>" # E.g. "arn:aws:..."


boto3_bedrock = bedrock.get_bedrock_client(
  assumed_role=os.environ.get("BEDROCK_ASSUME_ROLE", None),
  region=os.environ.get("AWS_DEFAULT_REGION", None),
  runtime=False
)

#### Validate the connection

# Since the `list_foundation_models()` method is not yet available, we can use the following workaround to list the available foundation models:

response = boto3_bedrock.describe_foundation_models()

foundation_models = []
for model in response["FoundationModels"]:
    foundation_models.append(model["FoundationModelArn"])

print("Available foundation models:")
for model in foundation_models:
    print(model)