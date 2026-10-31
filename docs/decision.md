# Decision Log

This file keeps track of the technical decisions made during the project. New decisions will be added as the dataset inspection and implementation progress.

## D1. Dataset selection

- **Decision:** Use the Salvador Urban Network Transportation (SUNT) dataset for the project.
- **Why:** The dataset contains public transport records that include passenger boardings and estimated vehicle load. These are relevant to the two main objectives: demand prediction and occupancy estimation.
- **Important detail:** The load values are estimates derived from fare-card data and trip chaining. They are not direct measurements of the number of passengers inside a bus.
- **Consequence:** Predictions involving occupancy will be described as estimated on-board load rather than measured occupancy.

## D2. Keep the original dataset unchanged

- **Decision:** Do not modify the original dataset files directly.
- **Why:** If cleaning or aggregation changes the source files, it becomes difficult to check whether an issue comes from the original data or from our processing steps.
- **Approach:** Any cleaning, transformation or aggregation will be performed on a separate processed copy.
- **Consequence:** The original data can be used again whenever the preprocessing pipeline needs to be changed.

## D3. Inspect the data before defining preprocessing rules

- **Decision:** Dataset inspection comes before selecting the final preprocessing steps.
- **Why:** Missing values, column formats, unusual passenger counts and timestamp inconsistencies need to be understood before deciding how to handle them.
- **Current work:** The repository contains `scripts/profile_dataset.py` for initial dataset profiling.
- **Still to decide:** The final handling of missing values, invalid records and unusual observations will depend on the profiling results.

## D4. Demand and occupancy are separate prediction targets

- **Decision:** Keep passenger demand and estimated vehicle load as separate prediction targets.
- **Why:** They describe different things. Demand concerns the number of passengers boarding during a period, whereas load represents the estimated number of passengers on board.
- **Consequence:** The two targets may require different input features and evaluation methods. Their results should not be treated as interchangeable.

## D5. Do not assume missing records mean zero demand

- **Decision:** Do not automatically replace missing dataset records with zero passenger counts.
- **Why:** A missing record does not necessarily mean that no passengers travelled. It may also mean that no stop event was recorded in the dataset.
- **Approach:** The meaning of missing records will be checked during data inspection before deciding whether they should be excluded, retained or handled separately.
- **Consequence:** Zero values and missing records will be treated as different cases.

## D6. Model selection will follow baseline evaluation

- **Decision:** Establish a baseline before selecting more complex prediction models.
- **Why:** Without a baseline, there is no clear way to judge whether a more complex model is actually improving the predictions.
- **Still to decide:** The baseline method and the models to be compared will be finalised after inspecting the dataset and defining the prediction setup.

## D7. Evaluation must respect time order

- **Decision:** The evaluation setup should preserve the chronological order of the data.
- **Why:** The project aims to predict future demand and load using past observations. Randomly mixing future and past records can give an unrealistic estimate of model performance.
- **Still to decide:** The exact training, validation and test periods will be documented once the dataset period and modelling setup are finalised.

## Pending decisions

The following choices need further work before they can be recorded as final decisions:

| Area | What needs to be decided |
|---|---|
| Prediction interval | The time period for each forecast |
| Preprocessing | Final rules for missing and invalid records |
| Feature engineering | Which historical and time-based features to use |
| Baseline | The initial forecasting method |
| Model selection | Which models to compare |
| Evaluation | Suitable metrics for demand and load |
| Occupancy levels | Whether vehicle capacity assumptions are needed |

This log will be updated when these choices are supported by implementation or experiment results. Previous decisions will be retained if a later decision changes or replaces them.