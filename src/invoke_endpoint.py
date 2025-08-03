#!/usr/bin/env python3
"""
Send an image to the SageMaker endpoint and print the prediction.
"""
import argparse, boto3, json, base64

def main(endpoint, image_path, region):
    smr = boto3.client("sagemaker-runtime", region_name=region)
    with open(image_path, "rb") as f:
        payload = f.read()
    resp = smr.invoke_endpoint(
        EndpointName=endpoint,
        ContentType="application/x-image",
        Body=payload
    )
    result = resp["Body"].read()
    print(json.loads(result.decode()))

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--endpoint", required=True)
    p.add_argument("--image", required=True)
    p.add_argument("--region", default="ap-south-1")
    args = p.parse_args()
    main(args.endpoint, args.image, args.region)
