# Project Plan

## Project Objective

The aim of this project is to predict public transport demand and estimate vehicle occupancy using historical transport data and machine learning.

The work starts with understanding the available dataset, identifying useful information and defining how demand and occupancy will be predicted.

## Work to Be Done

### 1. Dataset Understanding

- Study the dataset structure, columns and available records.
- Check for missing values, duplicate records and unusual entries.
- Understand how passenger boardings and vehicle load are represented.
- Identify the fields that can be used for prediction.

### 2. Data Preparation

- Decide how missing and invalid records should be handled.
- Convert timestamps and other fields into suitable formats.
- Prepare the data at an appropriate time interval for forecasting.
- Create useful features from historical passenger counts and time information.

### 3. Model Development

- Establish a simple baseline to get an initial reference result.
- Select suitable forecasting models for demand and occupancy prediction.
- Train the models using historical data.
- Make sure that input features only contain information available at prediction time.

### 4. Model Evaluation

- Separate training, validation and test data chronologically.
- Select suitable evaluation metrics for both prediction targets.
- Compare model performance against the baseline.
- Analyse prediction errors and identify periods where the models perform poorly.

### 5. Occupancy Estimation

- Study how vehicle load is represented in the dataset.
- Use the available load information as the basis for occupancy estimation.
- Document the assumptions used in interpreting load values.
- Identify cases where the estimates may be unreliable.

### 6. Reproducibility and Documentation

- Document the environment setup and commands required to run the project.
- Record dataset sources and preprocessing steps.
- Maintain an experiment log with actual results and observations.
- Document important technical decisions and changes made during development.

## Expected Outcome

The project aims to develop a reproducible prediction workflow for public transport demand and estimated vehicle load. The final results will include model evaluation, comparison with a baseline and a discussion of the limitations of the predictions.