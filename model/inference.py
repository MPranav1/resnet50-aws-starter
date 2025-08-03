import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
import io

model = models.resnet50(pretrained=True)
model.eval()

def model_fn(model_dir):
    return model

def predict_fn(input_data, model):
    image = Image.open(io.BytesIO(input_data)).convert('RGB')
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
    ])
    img_tensor = transform(image).unsqueeze(0)
    with torch.no_grad():
        output = model(img_tensor)
    return torch.argmax(output, 1).item()
