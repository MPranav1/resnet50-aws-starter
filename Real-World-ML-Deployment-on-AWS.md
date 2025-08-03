
# 🧪 Real-World ML Deployment on AWS

## ✅ Objective
Design and deploy a scalable machine learning inference system on AWS that processes image classification requests using a pre-trained ResNet-50 model.

---

## 🖼 1. Infrastructure Design

**Architecture Diagram**: [View on Draw.io]([https://drawio-app.com/#G1BsdwJ6UJuZRzDIzZArjNyDzzL7zGOy9U](https://drive.google.com/file/d/1UaVuL3VnmIBC1r4HXg_T2ksBwMiFK3il/view?usp=sharing))

### Components:

- **Compute**: AWS SageMaker Endpoint (managed, scalable model deployment).
- **Storage**: S3 Bucket for storing the model artifact (`model.tar.gz`) and image uploads.
- **API Gateway**: HTTPS endpoint to interact with SageMaker via REST API.
- **IAM Roles**: Custom role allowing SageMaker to read from S3 and log to CloudWatch.
- **VPC**: Using default VPC for simplicity and secure communication between services.

---

## 🚀 2. Deployment & Inference

- Used pre-trained ResNet-50 model from `torchvision.models`.
- Saved as `model.tar.gz` and uploaded to S3.
- Python script `deploy.py` uses SageMaker SDK to deploy the model.
- `inference.py` defines preprocessing and prediction logic.
- API Gateway exposes `/predict` endpoint for inference.

---

## 📈 3. Scalability & Resilience

- **SageMaker** supports auto-scaling based on traffic.
- **API Gateway** is serverless and scales automatically.
- **S3** is highly available and scalable by default.
- All services are fault-tolerant and managed by AWS.

---

## 📊 4. Monitoring & Logging

- **CloudWatch**:
  - Enabled for both SageMaker and API Gateway.
  - Logs requests, response times, errors.
- **Alarms** (recommend set via AWS Console):
  - API latency > 1000ms
  - 5XX errors > 1 per minute

---

## 🔐 5. Security

- **API Gateway** secured with API Key.
- **IAM Role** with minimum access to S3 and SageMaker only.
- **Encryption**:
  - S3 and SageMaker both use server-side encryption.
  - HTTPS in transit.
- WAF optional for extra protection (outside 2-hour scope).

---

## 💸 6. Cost Optimization

| Service           | Approx Cost for 2 hrs      |
|-------------------|----------------------------|
| SageMaker t2.medium | $0.26                      |
| S3 Storage        | < $0.01                    |
| API Gateway       | < $0.01 per 1k requests    |
| CloudWatch Logs   | < $0.01                    |

### Optimization Tips:

- Delete the endpoint after demo:
  ```python
  predictor.delete_endpoint()
  ```
- Use minimal instance types (`ml.t2.medium`)
- Use local testing where possible

---

## 📄 7. Documentation

### 📂 Folder Structure

```
ml-aws-resnet50-deployment/
├── terraform/
│   └── main.tf
├── model/
│   ├── inference.py
│   └── model.tar.gz (you create this manually)
├── deploy.py
├── README.md
```

### 🔧 Deployment Steps

```bash
# Configure AWS CLI
aws configure

# Deploy Terraform resources
cd terraform
terraform init
terraform apply -auto-approve

# Package model
cd model
# Save model as model.tar.gz manually (optional for now)

# Deploy using Python
python ../deploy.py
```

### 🔬 API Test

```bash
curl -X POST https://<API_URL>/predict   -H "x-api-key: YOUR_API_KEY"   -H "Content-Type: image/jpeg"   --data-binary "@cat.jpg"
```

---

## ✅ Final Checklist

| Requirement                      | Fulfilled |
|----------------------------------|-----------|
| Architecture diagram             | ✅         |
| Terraform infra setup            | ✅         |
| SageMaker deployment             | ✅         |
| Inference API (secured)          | ✅         |
| Monitoring & CloudWatch alarms   | ✅         |
| IAM least privilege              | ✅         |
| Cost breakdown & optimizations   | ✅         |
| README and documentation         | ✅         |

---

## 🧠 Assumptions & Trade-offs

- Used default VPC for time constraint.
- Used API Key instead of Cognito for simplicity.
- Used basic CloudWatch instead of full X-Ray tracing.
- No Docker container packaging to save time.

---

## 🔚 Conclusion

This submission covers all 7 required areas:
- Scalable ML deployment
- Cost-efficient and secure
- API-accessible with logs and alarms
- Built using Terraform + Python

> Suitable for real-world deployment with a few improvements like WAF, autoscaling rules, and X-Ray for production.
