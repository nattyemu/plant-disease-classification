# Data Card — Plant Disease Classification

## 1. Overview

**Project name:** Plant Disease Classification (Healthy vs Disease)  
**Primary task:** Binary image classification (Healthy / Disease)  
**Primary metrics:** Accuracy and F1-score (macro); AP/PR for disease class (secondary)  
**Dataset source:** Public images only (892 total), organized into `data/Healthy/` and `data/Disease/`.

## 2. Who / What / Where / Why

**Who collected the data:** This dataset was sourced from public online repositories. No self-collected images were used due to personal circumstances.  
**What is in each image:** Each image is an RGB photograph of a plant leaf, showing either signs of disease (e.g., spots, lesions) or healthy tissue.
**Where/how collected:** Downloaded from open/public datasets, curated manually for duplicates/quality. Sources and licenses are listed in `DATA_SOURCES.md`.  
**Why:** To create a lightweight research/educational prototype for quick plant leaf health triage.

## 3. Dataset composition & splits

**Total images:** 892

**Classes and counts:**

- Healthy: 458 images
- Disease: 434 images

**Stratified splits:**

- Train (70%): 623 images
- Validation (15%): 133 images
- Test (15%): 136 images

## 4. Labeling & provenance

**Method:** Folder-based labels (`ImageFolder`). Manual check for mislabels and duplicates.  
**Provenance & licenses:** The dataset contains no personally identifying or sensitive content. The public dataset used can be found at: [https://www.kaggle.com/datasets/dittakavinikhita/plant-disease-prediction-disease-and-healthy?resource=download](https://www.kaggle.com/datasets/dittakavinikhita/plant-disease-prediction-disease-and-healthy?resource=download).

## 5. Data collection protocol

- Minimum resolution: Images were kept at or above 720p resolution whenever possible.
- Quality control: Low-quality images that were blurred, overly compressed, or duplicated were removed from the dataset.
- Sampling: aimed for variation in background, lighting, and angle.
- Layout: `data/Healthy/` and `data/Disease/` folders with preserved filenames.

## 6. Known limitations & biases

- **No self-collected images:** The project requirement for a minimum of 40% self-collected data was not met due to unforeseen family circumstances. This means the dataset may not fully represent the conditions of a real-world field environment.
- **Geographic bias:** The public datasets used are likely from limited geographic regions and research labs, which may affect the model's ability to generalize to different plant species or disease variants found in other parts of the world.
- **Device bias:** Most images are of lab quality and may not accurately reflect the quality and characteristics of images taken with a typical smartphone camera in the field.
- **Class balance:** Reasonably balanced (458 vs 434).
- **Ethical note:** Prototype only — not a certified diagnostic tool.

## 7. Data format & storage

- Format: All images are stored as JPG files.
- Storage: The images are organized into `data/Healthy/` and `data/Disease/`folders.
- Metadata: No additional metadata beyond filenames is available.

## 8. Suggested evaluation

For a complete and robust evaluation, the final model should be tested on images collected directly from a real field environment using a standard smartphone to assess its true performance and generalization capabilities.

## 9. Checklist

- [x] Data stored in `data/`
- [x] Train/Val/Test = 70/15/15 (623 / 133 / 136)
- [x] Confusion matrix saved in `results/confusion_matrix.png`
- [x] Justification for lack of self-collected images (this Data Card & paper)

---

**Note:**  
Due to unforeseen family circumstances that arose during the project timeline, self-collection of data was not possible, and therefore, the dataset is public-only. The project's current focus is on pipeline reproducibility, deployment (FastAPI + Flutter), and thorough documentation. Future work should include local field data collection and testing under deployment conditions once these personal issues have been resolved.
