# Dataset Documentation

## 1. Dataset Source

This project uses the **Salvador Urban Network Transportation (SUNT)** dataset. It contains public transport journey records collected in Salvador, Brazil.

The dataset was developed by researchers from LabIA, Federal University of Bahia. It provides information about passenger boarding, alighting, vehicle trips, routes and travel times.

The source details are given below.

| Item | Details |
|---|---|
| Dataset | Salvador Urban Network Transportation (SUNT) |
| Authors | Ferreira, Souza, Rios, Fernandes, Nery, Gama, Bifet and Rios |
| Organization | LabIA, Federal University of Bahia |
| Research Paper | Scientific Data, Volume 12, Article 1320 (2025) |
| Paper DOI | https://doi.org/10.1038/s41597-025-05674-6 |
| Dataset DOI | https://doi.org/10.17632/85fdtx3kr5.1 |
| Dataset Repository | https://github.com/LabIA-UFBA/SUNT |
| File Format | Parquet |
| Dataset Version | Mendeley Data, Version 1 |

The original files are available in the SUNT GitHub repository. They are stored as daily Parquet files, following a naming pattern such as:

`od-YYYY-MM-DD.parquet`

## 2. Dataset Licence

The SUNT dataset is released under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** licence.

This allows us to use and modify the dataset, provided that we give credit to the original authors, include the licence information and mention the changes made to the data.

The research paper has a separate licence (CC BY-NC-ND 4.0). We use it as a reference for understanding the dataset and its collection process.

Licence: https://creativecommons.org/licenses/by/4.0/

## 3. What Does the Original Data Contain?

The original dataset is based on individual vehicle stop events. Each row represents a vehicle stopping at a particular location during a trip.

A record contains details such as the route, direction, stop, vehicle, trip and timestamp.

Some important columns are:

| Column | Description |
|---|---|
| `n-boardings` | Number of passengers boarding the vehicle at a stop. |
| `n-alighting` | Estimated number of passengers getting off the vehicle. |
| `lag_loading` | Estimated passenger load before the vehicle arrives at a stop. |
| `balance` | Passenger load after alighting. |
| `loading` | Passenger load after boarding. |

The original documentation uses underscores in some column descriptions, while the actual files use hyphens. In our processing code, these names can be changed to underscores for easier handling.

### How Passenger Loading Works

Consider a bus that arrives at a stop with 20 passengers.

- 5 passengers get off.
- 10 new passengers get on.

The passenger load after these activities becomes:

20 - 5 + 10 = 25 passengers.

This is the basic idea behind the loading information available in the dataset.

## 4. How Is the Data Collected?

SUNT uses contactless fare-card validations along with vehicle GPS information to build its passenger journey records.

When a passenger uses a fare card to board a bus, the validation is recorded. The researchers match this information with vehicle GPS data to identify the trip.

However, passenger boarding is not the only information needed to understand how many people are inside a vehicle. The dataset also needs information about passengers getting off.

Salvador does not have exit validators, so alighting information is estimated using a technique called **trip chaining**.

In simple terms, the method looks at a passenger's next boarding location to estimate where the passenger may have left the previous vehicle. The research uses a walking-distance limit of 1.1 km for this process.

Because of this, alighting and vehicle loading values should be treated as estimates rather than directly measured passenger counts.

## 5. Important Data Limitations

There are a few limitations in the original dataset that need to be considered during model development.

### 5.1 Estimated Alightings

Passenger alightings are inferred using trip information rather than directly recorded at the exit. This can introduce errors in the estimated passenger load.

### 5.2 Passengers Without Fare Cards

Passengers aged 65 and above can travel free without using a fare card. Their journeys are not fully represented in the automatic fare collection records.

As a result, the recorded passenger demand may be lower than the actual demand.

### 5.3 Unusual Boarding Values

Sometimes, mobile fare-card systems may register multiple validations together. This can produce unusually high boarding counts for a single stop event.

Such records need to be identified because they can affect the estimated passenger load and crowding analysis.

### 5.4 Vehicle Capacity

The original dataset does not provide vehicle capacity.

Therefore, passenger load alone cannot tell us whether a vehicle is crowded. We need external capacity information or clearly documented assumptions to estimate crowding levels.

### 5.5 Missing Records

A missing record does not necessarily mean that zero passengers travelled.

It may mean that the journey was not recorded or that no vehicle activity was available for that particular period.

We need to distinguish between an actual zero passenger count and missing information during preprocessing.

## 6. Preparing the Data for Our Project

The original SUNT data is stored at the stop-event level. For our prediction task, we need to organize the information in a way that makes passenger demand easier to study over time.

One possible approach is to group the records using:

- Route
- Direction
- Date
- Hour

Passenger boarding and alighting counts can then be combined for each group.

This will help us compare passenger activity across different routes and time periods.

The exact aggregation rules and final processed file structure will be documented alongside the data processing implementation.

## 7. Information Used for Prediction

The dataset contains several types of information that may be useful for forecasting.

| Information | How it can help |
|---|---|
| Previous passenger counts | Helps identify changes in passenger demand. |
| Route details | Helps compare travel patterns across routes. |
| Direction | Separates journeys travelling in different directions. |
| Date | Helps study daily and weekly patterns. |
| Time of travel | Helps identify busy and less busy hours. |
| Estimated passenger load | Helps study vehicle occupancy. |
| Previous travel patterns | Provides useful information for future predictions. |

The final features will depend on the columns available after data processing.

## 8. Processed Dataset

After the original data is inspected and processed, we plan to create an organized dataset for model training and evaluation.

The expected information includes:

| Field | Description |
|---|---|
| `service_date` | Date associated with the transport activity. |
| `route` | Route on which the activity took place. |
| `direction` | Direction of the journey. |
| `ts_hour` | Hour in which the activity was recorded. |
| `boardings` | Total passenger boardings during that period. |
| `alightings` | Total estimated passenger alightings. |
| `n_trips` | Number of distinct trips. |
| `load_max` | Highest estimated passenger load recorded. |
| `load_trip_peak_mean` | Average of the highest estimated load for each trip in that period. |

These fields describe the type of information useful for the prediction task. The final schema will be confirmed after implementing the processing pipeline.

## 9. Data Quality Checks

Before using the processed data, we need to check whether it is reliable enough for model training.

The following checks will be considered:

- Missing values in important columns.
- Duplicate records.
- Negative passenger counts or load values.
- Incorrect date and time information.
- Unusually high boarding counts.
- Trips with incomplete or inconsistent stop information.
- Missing route-hour records.

These checks will help identify problems that could affect the prediction results.

We will also record how each issue is handled instead of silently changing or removing data.

## 10. Changes Made to the Original Data

The original SUNT dataset will be kept separate from the processed data.

During preprocessing, we may make changes such as:

- Renaming columns to make them easier to use in Python.
- Selecting the records required for our prediction task.
- Grouping stop events by route, direction and time.
- Creating additional features from historical passenger information.
- Handling missing and unusual records.

All important changes will be documented so that the processed data can be understood and reproduced.

The original passenger values should not be changed without a clear reason, and any exclusions or transformations must be recorded.

## 11. Conclusion

The SUNT dataset provides historical information about public transport journeys, passenger boarding and estimated passenger loads.

This information gives us a starting point for studying how passenger demand changes across routes and times.

However, the dataset also has limitations, particularly in estimated alightings, missing passenger information and unavailable vehicle capacity details.

These points need to be considered while preparing the data and evaluating the prediction models. A proper understanding of the dataset will help us make more reliable use of the available information.