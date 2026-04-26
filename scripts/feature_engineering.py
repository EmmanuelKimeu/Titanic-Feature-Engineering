import pandas as pd
import numpy as np

def apply_feature_engineering(df):
    """
    Creates derived features and performs encoding.
    """
    # 1. Derived Features [cite: 47, 51-56]
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
    df['IsAlone'] = (df['FamilySize'] == 1).astype(int)
    
    # Title extraction
    df['Title'] = df['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)
    df['Title'] = df['Title'].replace(['Lady', 'Countess','Capt', 'Col', 'Don', 'Dr', 
                                       'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')
    df['Title'] = df['Title'].replace(['Mlle', 'Ms'], 'Miss')
    df['Title'] = df['Title'].replace('Mme', 'Mrs')
    
    # Fare per person and Age Groups
    df['Fare_Per_Person'] = df['Fare'] / df['FamilySize']
    df['AgeGroup'] = pd.cut(df['Age'], bins=[0, 12, 18, 60, 120], labels=['Child', 'Teen', 'Adult', 'Senior'])
    
    # 2. Feature Transformations [cite: 63-64]
    df['Fare_Log'] = np.log1p(df['Fare'])
    
    # 3. Categorical Encoding [cite: 57-58]
    df = pd.get_dummies(df, columns=['Sex', 'Embarked', 'Title', 'AgeGroup'], drop_first=True)
    
    return df