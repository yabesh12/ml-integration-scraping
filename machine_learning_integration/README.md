# Machine Learning Integration Script

## Purpose
This Python script demonstrates the integration of a simple machine learning model into a Python application. The chosen model is a Random Forest classifier, and the dataset used for training and evaluation is the Breast Cancer Wisconsin dataset.

## Chosen Model
The machine learning model selected for this integration is the Random Forest classifier. Random Forest is an ensemble learning method that operates by constructing a multitude of decision trees during training and outputs the class that is the mode of the classes (classification) of the individual trees.

## Dataset
The Breast Cancer Wisconsin dataset is used for training and evaluating the machine learning model. This dataset contains features computed from a digitized image of a fine needle aspirate (FNA) of a breast mass. The goal is to predict whether a breast tumor is malignant or benign.

## Steps

### 1. Load Dataset
The script starts by loading the Breast Cancer Wisconsin dataset using scikit-learn's `load_breast_cancer` function.

### 2. Split Dataset
The dataset is then split into training and testing sets using the `train_test_split` function from scikit-learn.

### 3. Train Model
The Random Forest model is trained on the training set using the `RandomForestClassifier` from scikit-learn.

### 4. Make Predictions
The trained model is used to make predictions on the test set.

### 5. Evaluate Performance
The script evaluates the performance of the machine learning model using accuracy and a classification report. The classification report provides precision, recall, and F1-score for each class (malignant and benign).

## How to Run the Script
To run the script, ensure you have Python and the required dependencies installed. You can run the script using the following command:

### 1. Install Dependencies
Before running the script, make sure to install the required dependencies. You can install them using the following command:

```bash
pip install scikit-learn pandas