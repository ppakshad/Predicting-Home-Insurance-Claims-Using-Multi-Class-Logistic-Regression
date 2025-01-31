# -*- coding: utf-8 -*-
"""home-claim.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Geg4qh1zaCoWyrx6Zj9D01cBka9nomk4
"""

import pandas as pd
df = pd.read_excel('./Homeowner_Claim_History.xlsx', sheet_name='HOCLAIMDATA')

df.head()

df['Frequency'] = df['num_claims'] / df['exposure']
def group_frequency(frequency):
    if frequency == 0:
        return 0
    elif 0 < frequency <= 1:
        return 1
    elif 1 < frequency <= 2:
        return 2
    elif 2 < frequency <= 3:
        return 3
    else:
        return 4

df['Frequency Group'] = df['Frequency'].apply(group_frequency)
df = df.dropna(subset=['Frequency Group'])

train_df = df[df['policy'].str.startswith(('A', 'G', 'P'))]
test_df = df[~df['policy'].str.startswith(('A', 'G', 'P'))]

train_df.head()

test_df.head()

from itertools import combinations

predictors = ['f_aoi_tier', 'f_fire_alarm_type', 'f_marital', 'f_mile_fire_station', 'f_age_tier', 'f_primary_gender', 'f_residence_location']
all_predictor_combinations = []

for r in range(1, len(predictors) + 1):
    combinations_r = combinations(predictors, r)
    all_predictor_combinations.extend(combinations_r)

len(all_predictor_combinations)

all_predictor_combinations

"""# a

"""

train_group_counts = train_df['Frequency Group'].value_counts()

train_group_counts

test_group_counts = test_df['Frequency Group'].value_counts()

test_group_counts

