#!/usr/bin/env python3
"""
Download pre-trained ResNet-50, tar it as model.tar.gz,
and upload to the specified S3 bucket.
"""
import argparse, tarfile, boto3, tempfile, os, torch, torchvision

def main(bucket: str, key: str):
    model = torchvision.models.resnet50(weights="IMAGENET1K_V2")
    with tempfile.TemporaryDirectory() as tmp:
        model_path = os.path.join(tmp, "model.pth")
        torch.save(model, model_path)
        tar_path = os.path.join(tmp, "model.tar.gz")
        with tarfile.open(tar_path, "w:gz") as tar:
            tar.add(model_path, arcname="model.pth")
        s3 = boto3.client("s3")
        s3.upload_file(tar_path, bucket, key)
        print(f"Uploaded s3://{bucket}/{key}")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--bucket", required=True)
    p.add_argument("--key", default="model.tar.gz")
    args = p.parse_args()
    main(args.bucket, args.key)
