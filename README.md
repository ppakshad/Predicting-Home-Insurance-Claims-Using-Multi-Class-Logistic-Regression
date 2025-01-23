# Predicting Home Insurance Claims Using Multi-Class Logistic Regression

## 📖 Overview
This project focuses on **predicting the frequency of home insurance claims** using **multi-class logistic regression**. The dataset contains **home insurance policyholder information**, including **demographic data, claim history, residence location, and safety features**. The dataset includes information on policyholders, the number of claims filed, demographic characteristics, geographic location, safety systems, and other relevant factors.

## Project Objectives:
Identify key factors that influence the frequency of insurance claims.
Develop a predictive model to categorize policyholders based on their claim frequency.
Evaluate different combinations of predictor variables to find the most effective model.
In this project, data preprocessing and feature engineering were performed to create a structured dataset. Various logistic regression models were trained with different predictor combinations, and their performance was evaluated using AIC (Akaike Information Criterion), BIC (Bayesian Information Criterion), accuracy, and RMSE (Root Mean Squared Error) to determine the optimal set of predictors.

The goal of this analysis is to:
- Understand the factors influencing the frequency of claims.
- Develop a predictive model for categorizing claim frequencies.
- Evaluate different predictor combinations for the best performance.

## 📊 Dataset
The dataset includes the following features:
- **policy**: Unique policy ID.
- **exposure**: Risk exposure factor.
- **num_claims**: Number of claims filed.
- **amt_claims**: Total amount of claims.
- **f_primary_age_tier**: Age tier of the policyholder.
- **f_primary_gender**: Gender of the policyholder.
- **f_marital**: Marital status.
- **f_residence_location**: Urban/Suburban residence.
- **f_fire_alarm_type**: Type of fire alarm system.
- **f_mile_fire_station**: Distance from the nearest fire station.
- **f_aoi_tier**: Estimated property value.

## ⚙️ Methodology
1. **Data Processing**:
   - Loaded data from an Excel file.
   - Created a new feature `Frequency` (num_claims / exposure).
   - Categorized policies into `Frequency Group` based on claim frequency.
   - Split data into **training (policy IDs: A, G, P)** and **testing sets**.

2. **Feature Engineering**:
   - Created all possible combinations of predictor variables.
   - Applied one-hot encoding to categorical variables.

3. **Model Training**:
   - Used **Multinomial Logistic Regression** to classify claim frequency groups.
   - Evaluated models based on:
     - **AIC (Akaike Information Criterion)**
     - **BIC (Bayesian Information Criterion)**
     - **Accuracy on test data**
     - **RMSE (Root Mean Squared Error)**

4. **Optimization & Performance**:
   - The best predictor combination (based on AIC):  
     `['f_aoi_tier', 'f_fire_alarm_type', 'f_mile_fire_station', 'f_primary_age_tier', 'f_residence_location']`
   - The best predictor combination (based on BIC):  
     `['f_fire_alarm_type', 'f_mile_fire_station', 'f_primary_age_tier']`
   - Highest accuracy achieved: **56.4%**.

## Installation & Usage
To run this project, ensure you have the required dependencies installed:

```bash
pip install pandas numpy scikit-learn statsmodels
```
Clone this repository and run the Jupyter Notebook:

```
git clone https://github.com/yourusername/home-insurance-claims.git
cd home-insurance-claims
jupyter notebook home-claim.ipynb
```
## Findings:

- The model performs moderately well in classifying claim frequencies.
- Fire alarm type and Distance to fire station were strong predictors.
- More advanced modeling techniques (e.g., XGBoost, Neural Networks) could improve accuracy.

## Note: 

This project is open-source and available under the MIT License.
