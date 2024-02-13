## Problem Statement:
Create a pipeline which predicts the h-index(or score) of the student based on
the features provided to you in the dataset. The train and test data have been
provided in the dataset folder. Please be sure to make an inclusive pipeline which
consists the following:
- Model trained on the training dataset and the predictions for the test
dataset in a .csv file.
- Create a simple interface to use the model using streamlit/gradio.
Trained for 5 epochs, overfits data

### About the dataset:
Consists a dataset with 10,000 entries and the following features:

`Hours Studied`, `Previous Scores`, `Extracurricular Activities`, `Sleep Hours`, `Sample Question Papers Practiced`, `Performance Index`


## Model 1:
A `preprocessing_model` first normalises the data and adjusts to the mean and variance of the training set

This model was trained for 5 epochs over the entire dataset. Overfits to the training dataset.
x


### Model Architecture:
    Inputs -> Dense(64) -> Output

## Model 2:
Trained for 5 epochs, avoids overfitting by the use of Dropout layers
### Model Architecture:
    Inputs -> Dense(32) -> Dropout(0.5) -> Dense(64) -> Dropout(0.4) -> Output


## Other:
`predictions_v1.csv` and `predictions_v2.csv` are the predictions of Model 1 and Model 2 on the test data.

Run the `model_deployment.py` file to use the streamlit interface of the model