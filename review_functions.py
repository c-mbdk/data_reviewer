import numpy as np
import pandas as pd
import os
import shutil

source_file_dir = 'source_file/'
lookup_file_dir = 'lookup_files/'

# extract from main source file
def extract_from_csv(file_to_process):
    df = pd.read_csv(file_to_process, sep='\s*,\s*', engine='python')
    return df

# user input = to get validated columns
def identify_validated_columns(df):
    list_of_validated_columns = []

    for col in df.columns.tolist():
        user_input = input(f"Is {col} validated in the ETL? (yes/no) ").lower()
        if user_input == "yes":
            list_of_validated_columns.append(col)
        elif user_input == "no":
            pass
        else:
            print("Only yes or no answers are accepted")
    
    return list_of_validated_columns

# user input = get key for querying lookup
def identify_key(df):
    key_to_query_lookup = None

    for col in df.columns.tolist():
        user_key_input = input(f"Is {col} the key (yes/no) ").lower()
        if user_key_input == "yes":
            key_to_query_lookup = col
            break
        elif user_key_input == "no":
            pass
        else:
            print("Only yes or no answers are accepted")

    return key_to_query_lookup

# user input - identify relevant lookups
def get_lookup_filename():
    lookup_files = os.listdir(lookup_file_dir)
    for fname in lookup_files:
        user_lookup_input = input(f"Should the data review include this lookup file: {fname}? (yes/no) ").lower()
        if user_lookup_input == "yes":
            filename = lookup_file_dir + fname
        elif user_lookup_input == "no":
            pass
        else:
            print("Only yes or no answers are accepted")

    return filename


# create lookup - customised
def create_custom_lookup(df):
    key_column = df.columns[0]
    print(key_column)
    dict_df = df.set_index(key_column).T.to_dict('list')
    return dict_df

# review source file against lookup
def review_against_lookup(df, lookup_key, lookup_dict):
    lookup_observations = []
    for value in df[lookup_key]:
        if pd.isnull(value):
          for num in np.where(df[lookup_key].isnull())[0].tolist():
            lookup_observations.append(f"Row {num+1}: Null value in {lookup_key} cannot match with the lookup file.")
        else:
            if int(value) not in lookup_dict.keys():
                lookup_observations.append(f'This value {int(value)} is not present in the lookup')
    return lookup_observations

# handling null values in validated columns - for each validated column in the source file, identify the rows with null values
def identify_null_values(df, validated_columns: list):
    results = []
    for col in validated_columns:
        for num in np.where(df[col].isnull())[0].tolist():
            results.append(f"Row {num+1}: Null value in {col}")
    return results
