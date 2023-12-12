import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.datasets import load_breast_cancer
import numpy as np

def load_dataset():
    """
    Loads a small dataset for training and evaluation.

    Returns:
    - X (numpy.ndarray): Features.
    - y (numpy.ndarray): Labels.
    """
    # Example dataset: Breast Cancer Wisconsin dataset
    data = load_breast_cancer()
    X, y = data.data, data.target
    return X, y

def train_model(X_train, y_train):
    """
    Trains a simple machine learning model (Random Forest) on the provided dataset.

    Parameters:
    - X_train (numpy.ndarray): Training features.
    - y_train (numpy.ndarray): Training labels.

    Returns:
    - model (sklearn.ensemble.RandomForestClassifier): Trained machine learning model.
    """
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    return model

def make_predictions(model, X_test):
    """
    Makes predictions using the trained machine learning model.

    Parameters:
    - model (sklearn.ensemble.RandomForestClassifier): Trained machine learning model.
    - X_test (numpy.ndarray): Test features.

    Returns:
    - predictions (numpy.ndarray): Predicted labels.
    """
    predictions = model.predict(X_test)
    return predictions

def evaluate_model(y_true, y_pred):
    """
    Evaluates the performance of the machine learning model.

    Parameters:
    - y_true (numpy.ndarray): True labels.
    - y_pred (numpy.ndarray): Predicted labels.
    """
    accuracy = accuracy_score(y_true, y_pred)
    report = classification_report(y_true, y_pred)

    print(f"Accuracy: {accuracy:.2f}")
    print("Classification Report:")
    print(report)
    

def main():
    """
    Main function to execute the machine learning integration script.
    """
    # Load dataset
    X, y = load_dataset()

    # Split dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the machine learning model
    model = train_model(X_train, y_train)

    # Make predictions on the test set
    predictions = make_predictions(model, X_test)

    # Evaluate model performance
    evaluate_model(y_test, predictions)

if __name__ == "__main__":
    main()
