import pandas as pd
from datetime import datetime
import json


class PVADataCleaner:
    def __init__(self, filepath, sheetname):
        self.filepath = filepath
        self.sheetname = sheetname

    def replace_columns(self, df, old_colm, new_colm, new_values: list):
        df.rename(columns={old_colm: new_colm}, inplace=True)
        df[new_colm] = new_values

    def white_BIPOC(self, row):
        race = row['race']
        if race == 'White':
            return 'White'
        else:
            return 'BIPOC'

    def male_female_other(self, row):
        gender = row['gender']
        if gender == 'Skip this question' or gender == 'GENDER NON-CONFORMING':
            return 'OTHER'
        else:
            return gender

    def age_map(self, age):
        if age < 1:
            return None
        elif age < 18:
            return 'Under 18'
        elif age < 25:
            return '18-24'
        elif age < 35:
            return '25-34'
        elif age < 45:
            return '35-44'
        elif age < 55:
            return '45-54'
        elif age < 65:
            return '55-64'
        else:
            return '64 and over'

    def clean_data(self):
        # Load data
        df = pd.read_excel(self.filepath, sheet_name=self.sheetname)
        # dropping columns that have all null entries
        df.dropna(axis=1, how="all", inplace=True)

        unnecessary_columns = ['Location Latitude', 'Location Longitude', 'HMIS ID', 'Start Date', 'End Date', 'Response Type', 'IP Address', 'Progress', 'Duration (in seconds)', 'Finished', 'Recorded Date', 'Response ID', 'Distribution Channel', 'User Language', 'Consent', 'Case manager completing Place Value assessment - Selected Choice',
                               'Case manager completing Place Value assessment - Other - Text', 'Case Manager Email Address', 'Homeless before med', 'Living Situation Details', 'Homeless before corrections', 'Confirm', 'Embedded Household Score', 'Score', 'Scored Score', 'Final Score']
        # drop unnecessary columns
        df.drop(unnecessary_columns, axis=1, inplace=True)

        # Converting the DOB Date of Birth columns to Age
        date_of_birth_list = df['DOB']
        current_date = datetime.now()
        age_list = []
        # Calculate age for each date of birth
        for dob in date_of_birth_list:
            dob = str(dob)
            # Convert the date of birth string to a datetime object
            dob_date = datetime.strptime(dob, '%Y-%m-%d %H:%M:%S')
            age = (current_date - dob_date).days // 365
            age_list.append(age)

        self.replace_columns(df, 'DOB', 'Age', age_list)

        # We notice that, for the gender column, the dataset has two skip options. Therefore, we are merging the two options into one below.
        gender_col_entries = df['How do you identify your gender?']
        two_skips_merged = []
        for val in gender_col_entries:
            if val == 'skip':
                val = 'Skip this question'
            two_skips_merged.append(val)

        df['How do you identify your gender?'] = two_skips_merged

        # Converting long column names to short names
        with open('columns_mapping.json') as f:
            columns_mapping = json.load(f)
        # Rename the columns
        df.rename(columns=columns_mapping, inplace=True)

        # Replace the values in the columns
        df['race'] = df.apply(self.white_BIPOC, axis=1)
        df['gender'] = df.apply(self.male_female_other, axis=1)
        df['AGE_GROUP'] = df['age'].apply(self.age_map)

        return df


filepath = '/Users/roshan/Downloads/PVADATA.xlsx'
sheetname = 'Raw Data_06.26.23'

cleaner = PVADataCleaner(filepath, sheetname)
cleaned_data = cleaner.clean_data()
cleaned_data.to_json('../data/cleaned_data.json', orient='records')
