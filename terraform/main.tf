provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "model_bucket" {
  bucket = "resnet-model-bucket-12345"
  force_destroy = true
}

resource "aws_iam_role" "sagemaker_execution_role" {
  name = "sagemaker-execution-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Principal = { Service = "sagemaker.amazonaws.com" }
      Action = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_role_policy_attachment" "attach_s3_policy" {
  role       = aws_iam_role.sagemaker_execution_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonS3FullAccess"
}
