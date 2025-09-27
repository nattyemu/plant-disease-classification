
# Plant Disease Classification

## 🌿 Project Overview

This project presents a comprehensive, full-stack deep learning solution for classifying plant diseases. Using a computer vision model trained on a dataset of leaf images, the system can distinguish between "Healthy" and "Diseased" plants. The solution is built for practical, real-world application, featuring a backend API for inference and a mobile application for easy use in the field.

The primary goal is to provide a fast and accessible tool for farmers and agricultural workers to perform quick plant health triage, helping to mitigate crop loss and support sustainable agriculture.

-----

## ✨ Features

- **Deep Learning Model:** Multiple ResNet architectures tested with comprehensive improvement analysis.
- **Complete Training Pipeline:** A well-documented Jupyter notebook that covers data preprocessing, model training, and evaluation.
- **Three Improvement Levels:** Systematic experimentation with data augmentation, optimizer changes, and architecture upgrades.
- **Full-Stack Deployment:** An efficient **FastAPI** backend that serves the trained model for predictions.
- **Mobile Application:** A user-friendly **Flutter** app that allows users to capture or upload images for real-time classification.
- **Reproducibility:** Detailed documentation on the project structure, dataset, and run instructions.

-----

## 📂 Project Structure

The repository is organized to ensure clarity and ease of use.

```
plant-disease-classification/
├── data/                 # Dataset (Healthy/ + Disease/)
├── notebooks/
│   └── main.ipynb       # Complete training pipeline
├── results/             # Evaluation metrics & plots
├── server.py            # FastAPI server for inference
├── plant_disease_classifier_app/  # Flutter mobile app
├── requirements.txt     # Python dependencies
├── RUN.md              # Detailed run instructions
└── DATA_CARD.md        # Dataset documentation
```

-----

## 📊 Dataset

The model was trained on a dataset comprising 892 RGB images of plant leaves. The dataset is balanced, with two primary classes: "Healthy" and "Disease." It was split into stratified sets for training, validation, and testing.

| Split | Number of Images |
|---|---|
| Train | 623 |
| Validation | 133 |
| Test | 136 |

**Note:** This repository contains a sample dataset (50 images per class). The full dataset is available externally.

-----

## 📈 Model Development & Results

### Three Improvement Levels Tested:

1. **Improvement Level 0**: ResNet-18 baseline with standard training
2. **Improvement Level 1**: ResNet-50 with enhanced training (AdamW, cosine annealing)
3. **Improvement Level 2**: ResNet-101 with advanced training (one-cycle LR)

### Performance Results:

| Model | Test Accuracy | Validation Accuracy |
|-------|---------------|---------------------|
| ResNet-18 (Baseline) | **98.53%** | 97.74% |
| ResNet-50 | 97.79% | 98.50% |
| ResNet-101 | 58.09% | 54.14% |

**Best Model: ResNet-18 Baseline** achieved the highest performance with 98.53% test accuracy.

### Final Classification Report (ResNet-18)

```
              precision    recall  f1-score   support

     Disease       0.97      1.00      0.99        66
     Healthy       1.00      0.97      0.99        70

    accuracy                           0.99       136
   macro avg       0.99      0.99      0.99       136
weighted avg       0.99      0.99      0.99       136
```

### Unseen Data Testing:
- **8/8 images correctly classified** (100% accuracy on external test images)

-----

## 🚀 Getting Started

To get the project up and running, follow these steps:

### 1. Project Setup

First, set up a dedicated virtual environment and install the required Python libraries.

```bash
# Create virtual environment
python -m venv venv

# Activate environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies from requirements.txt
pip install -r requirements.txt
```

### 2. Run the Training Pipeline
First get the data form The public dataset used can be found at: [https://www.kaggle.com/datasets/dittakavinikhita/plant-disease-prediction-disease-and-healthy?resource=download](https://www.kaggle.com/datasets/dittakavinikhita/plant-disease-prediction-disease-and-healthy?resource=download) and overide the `data/Healthy/` and `data/Disease/` folder. I include the sample dataset and unseed images for push the data folder structuer and  test the model in data folder.
After setting up the environment, navigate to the `notebooks` directory and run the `main.ipynb` Jupyter notebook. This will perform all data preprocessing, model training, evaluation, and save the final model and results.

```bash
cd notebooks
jupyter notebook
```

### 3. Start the FastAPI Server

Once the training is complete, start the FastAPI server from the project's root directory. This will host the prediction API for the mobile application.

```bash
python server.py
```

### 4. Run the Flutter App

Finally, navigate to the `plant_disease_classifier_app/` directory and launch the Flutter application on your mobile device or emulator. The app will connect to the running FastAPI server for predictions.

```bash
cd plant_disease_classifier_app/
flutter run
```

-----

## 🚧 Limitations & Future Work

The primary limitation of this project is the exclusive use of a public dataset. Future work will focus on:

- Collecting **local, self-collected field data** to improve the model's robustness and generalization.
- Implementing on-device inference using frameworks like TFLite for faster predictions and offline functionality.
- Expanding the number of classes to identify specific diseases.
- Addressing the performance degradation observed with more complex architectures (ResNet-101).

-----

## 📄 License

This project is intended for educational and research purposes. Please refer to the dataset sources and original licenses for any external data used.

