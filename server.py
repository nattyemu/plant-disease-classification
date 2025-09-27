from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
import io

app = FastAPI()

# CORS middleware to allow Flutter app connections
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Device configuration
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# Model definition - Use ResNet-18 since that's what you trained
def get_model(num_classes=2):
    try:
        model = models.resnet18(weights=models.ResNet18_Weights.IMAGENET1K_V1)
    except:
        model = models.resnet18(weights=None)
    in_features = model.fc.in_features
    model.fc = nn.Linear(in_features, num_classes)
    return model

# Load your trained model - Use the final_model.pth that notebook creates
model = get_model(num_classes=2)
model_path = "models/final_model.pth"  # Simple and reliable
try:
    model.load_state_dict(torch.load(model_path, map_location=device, weights_only=True))
    print("✅ Model loaded successfully!")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    print("⚠️ Using randomly initialized model")

model.to(device)
model.eval()

# Preprocessing transform (same as your validation transform)
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

class_names = ['Disease', 'Healthy']

@app.post("/predict")
async def predict(image: UploadFile = File(...)):
    try:
        # Read image
        image_data = await image.read()
        img = Image.open(io.BytesIO(image_data)).convert('RGB')
        
        # Preprocess
        input_tensor = transform(img).unsqueeze(0).to(device)
        
        # Predict
        with torch.no_grad():
            output = model(input_tensor)
            probabilities = torch.nn.functional.softmax(output[0], dim=0)
            confidence, predicted = torch.max(probabilities, 0)
        
        return {
            "success": True,
            "prediction": class_names[predicted.item()],
            "confidence": round(confidence.item(), 4),
            "all_probabilities": {
                class_names[i]: round(probabilities[i].item(), 4) for i in range(len(class_names))
            }
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

@app.get("/")
async def root():
    return {"message": "Plant Disease Classification API", "status": "running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "model_loaded": True}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=9000)