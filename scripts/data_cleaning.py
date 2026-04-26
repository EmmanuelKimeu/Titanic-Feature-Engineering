import pandas as pd

def clean_data(df):
    """
    Handles missing values, outliers, and data consistency.
    """
    # Missing Value Handling [cite: 29]
    df['Age'] = df['Age'].fillna(df['Age'].median())
    df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
    df['Fare'] = df['Fare'].fillna(df['Fare'].median())
    
    if 'Cabin' in df.columns:
        df.drop(columns=['Cabin'], inplace=True)
        
    # Outlier Handling: Capping at 95th percentile [cite: 36-38]
    df['Fare'] = df['Fare'].clip(upper=df['Fare'].quantile(0.95))
    df['Age'] = df['Age'].clip(upper=df['Age'].quantile(0.95))
    
    # Data Consistency & Duplicates [cite: 39-42]
    df.drop_duplicates(inplace=True)
    
    return df