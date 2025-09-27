````md
# Plant Disease Classification — Run & Deployment Guide

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
````

### 2\. Run the Training Pipeline

After setting up the environment, navigate to the `notebooks` directory and run the `main.ipynb` Jupyter notebook. This will perform all data preprocessing, model training, evaluation, and save the final model and results.

```bash
cd notebooks
jupyter notebook
```

### 3\. Start the FastAPI Server

Once the training is complete, start the FastAPI server from the project's root directory. This will host the prediction API for the mobile application.

```bash
python server.py
```

### 4\. Run the Flutter App

Finally, navigate to the `plant_disease_classifier_app/` directory and launch the Flutter application on your mobile device or emulator. The app will connect to the running FastAPI server for predictions.

```bash
cd plant_disease_classifier_app/
flutter pub get
flutter run
```

```

```
