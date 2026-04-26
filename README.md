# Titanic Survival Analysis - Feature Engineering Pipeline

## 1. Brief Description
This project focuses on the end-to-end preprocessing of the Titanic dataset. It covers data cleaning, the creation of new predictive features, and feature selection using machine learning importance rankings. The goal is to transform raw data into a model-ready format to predict passenger survival.

## 2. Project Structure
- `data/`: Contains raw datasets and the final `train_cleaned.csv`.
- `notebooks/`: Includes the Jupyter Notebook used for visual exploration and justification of data transformations.
- `scripts/`: Contains modular Python files (`.py`) for automated data processing.
- `requirements.txt`: Lists all necessary Python libraries.

## 3. Instructions to Run
### Setup
1. Clone this repository to your local machine.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

### 4. Data Cleaning Decisions
Missing Values: Age and Fare were filled with their respective medians to maintain distribution. Embarked was filled with the mode. Cabin was dropped due to excessive missingness (>75%).

Outliers: Applied a cap at the 95th percentile for Age and Fare to prevent extreme outliers from biasing the model.

Consistency: Checked for and removed duplicate rows to ensure data integrity.

### 5. Key Observations & Findings
Social Status: The extracted Title feature proved highly predictive; passengers with titles like "Mrs" or "Miss" showed significantly higher survival rates than "Mr".

Family Structure: Traveling in a small family (size 2-4) provided a survival advantage, whereas traveling alone or in very large families decreased survival probability.

Normalization: The Fare variable was heavily right-skewed. A Log Transformation successfully normalized the distribution, which is critical for many ML algorithms.

Top Predictors: Using a Random Forest importance ranking, Sex, Title, and Fare_Log were identified as the most significant features for survival prediction.
