Titanic Survival Analysis - Feature Engineering

Project Objective
[cite_start]This project aims to build a predictive pipeline for the Titanic dataset by performing rigorous data cleaning, feature engineering, and feature selection to identify the strongest predictors of survival[cite: 3].

Project Structure
- **data/**: Contains raw (`train.csv`, `test.csv`) and processed data (`train_cleaned.csv`).
- **notebooks/**: `Titanic_Feature_Engineering.ipynb` for data exploration and visualization.
- [cite_start]**scripts/**: Modular Python scripts for data cleaning, engineering, and selection [cite: 9-21].


  [cite_start]Data Cleaning Decisions [cite: 25]
- **Missing Values**: Imputed `Age` and `Fare` with medians; `Embarked` with the mode. [cite_start]`Cabin` was dropped due to >70% missing data [cite: 33-35].
- [cite_start]**Outliers**: Numerical features (`Fare`, `Age`) were capped at the 95th percentile to minimize the impact of extreme values [cite: 36-38].
- [cite_start]**Consistency**: Removed duplicate entries and ensured categorical naming was uniform [cite: 39-42].


  [cite_start]Feature Engineering [cite: 24]
- [cite_start]**Derived Features**: Created `FamilySize`, `IsAlone`, `Fare_Per_Person`, and extracted `Title` from names [cite: 51-56].
- [cite_start]**Transformations**: Applied Log Transformation to `Fare` to normalize its distribution[cite: 64].
- [cite_start]**Encoding**: One-Hot Encoding applied to nominal features: `Sex`, `Embarked`, `Title`, and `AgeGroup` [cite: 57-58].


  [cite_start]Key Findings [cite: 26]
- [cite_start]Social status (indicated by **Title**) and **Gender** were the strongest predictors of survival[cite: 73].
- Passengers traveling in small families had a higher survival rate compared to those traveling alone.