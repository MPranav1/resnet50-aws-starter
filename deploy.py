import boto3
import sagemaker
from sagemaker.pytorch import PyTorchModel

# Initialize session
session = sagemaker.Session()
role = 'arn:aws:iam::<your-account-id>:role/sagemaker-execution-role'  # Replace with output of terraform

model = PyTorchModel(
    model_data='s3://resnet-model-bucket-12345/model.tar.gz',
    role=role,
    entry_point='inference.py',
    framework_version='1.12.0',
    py_version='py38'
)

predictor = model.deploy(
    initial_instance_count=1,
    instance_type='ml.t2.medium',
    endpoint_name='resnet50-endpoint'
)
