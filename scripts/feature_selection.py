def select_features(df):
    """
    Removes non-predictive and redundant features.
    """
    # Dropping unique identifiers and raw text [cite: 71, 79-80]
    cols_to_drop = ['PassengerId', 'Name', 'Ticket']
    
    # Ensure columns exist before dropping
    existing_drops = [c for c in cols_to_drop if c in df.columns]
    df_final = df.drop(columns=existing_drops)
    
    return df_final