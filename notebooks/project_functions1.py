# Import required libraries
import pandas as pd

# #SINGLE FUNCTION METHODS
def drop_columns(dataframe):
    # Takes only a few columns from the raw data and makes it into a new file
    dropped_column_df =  dataframe.copy().drop(columns=['Timestamp', 'Gender', 'Country', 'state', 'self_employed', 'family_history', 'work_interfere', 'no_employees', 'remote_work', 'tech_company', 'benefits', 'care_options', 'wellness_program', 'seek_help', 'anonymity', 'leave', 'mental_health_consequence', 'phys_health_consequence', 'mental_health_interview', 'phys_health_interview', 'mental_vs_physical', 'obs_consequence', 'comments'],axis=1).dropna(axis=0)
    return dropped_column_df
def drop_rows(dataframe, row_index):
    dropped_df = dataframe.drop(row_index)
    return dropped_df
def filter_ages(dataframe):
    # Find all ages above 100
    filtered_high_df = dataframe[dataframe['Age'] >= 100].index
    # Find all ages below 18
    filtered_low_df = dataframe[dataframe['Age'] <= 18].index
    high_dropped_df = drop_rows(dataframe, filtered_high_df)
    low_dropped_df = drop_rows(high_dropped_df, filtered_low_df)
    return low_dropped_df

# #CHAIN METHOD
def load_and_process(dataframe):
    df = pd.DataFrame(dataframe)
    # chain 1
    def df1(dataframe):
        dfa = drop_columns(dataframe)
        return dfa
    # chain 2
    def df2(dataframe):
        dfa = df1(dataframe)
        dfb = filter_ages(dfa)
        return dfb
    # call method chain
    proj_df = df2(df)
    return proj_df