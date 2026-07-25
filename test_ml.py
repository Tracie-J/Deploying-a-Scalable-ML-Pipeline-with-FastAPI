import pytest
# TODO: add necessary import
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from ml.model import train_model, compute_model_metrics

# TODO: implement the first test. Change the function name and input as needed
def test_train_model_returns_random_forest():
    """
    Verify that train_model returns a RandomForestClassifier.
    """
    # Your code here
    # create fake training dataset
    X_train = pd.DataFrame({
        "feature1": [0, 1, 0, 1],
        "feature2": [1, 0, 1, 0]
    })
    y_train = [0, 1, 0, 1]

    model = train_model(X_train, y_train)

    assert isinstance(model, RandomForestClassifier)


# TODO: implement the second test. Change the function name and input as needed
def test_compute_model_metrics_returns_floats():
    """
    Verify that compute_model_metrics returns numeric metric values
    """
    # Your code here
    y = [0, 1, 1, 0]
    preds = [0, 1, 0, 0]

    precision, recall, fbeta = compute_model_metrics(y, preds)

    assert isinstance(precision, float)
    assert isinstance(recall, float)
    assert isinstance(fbeta, float)


# TODO: implement the third test. Change the function name and input as needed
def test_compute_model_metrics_range():
    """
    Verify that the computed metrics are between 0 and 1.
    """
    # Your code here
    y = [0, 1, 1, 0]
    preds = [0, 1, 0, 0]

    precision, recall, fbeta = compute_model_metrics(y, preds)

    assert 0 <= precision <= 1
    assert 0 <= recall <= 1
    assert 0 <= fbeta <= 1
