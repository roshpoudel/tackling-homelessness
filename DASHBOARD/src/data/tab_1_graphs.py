import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from data.loader import load_dataframe
import pkg_resources

file_path1 = pkg_resources.resource_filename('data', 'cleaned_data.json')
file_path2 = pkg_resources.resource_filename('data', 'original_df.json')

# Load the cleaned data from the JSON file - PVA
df = load_dataframe(file_path1)
original_df = load_dataframe(file_path2)

# -------------------------------------------------------------------
# -------------------------------------------------------------------

# PIT Data
# The data that we have here comes from the 2023 PIT survey count. Since we do not have a structured dataset, we have to manually enter the data.

categories = ['Under 18', '18-24', '25-34',
              '35-44', '45-54', '55-64', '64 and over']
numbers_of_people = [66, 203, 250, 380, 356, 329, 151]
data = {
    'Age Groups': categories,
    'PIT Count': numbers_of_people
}
PIT_age = pd.DataFrame(data)

# ------------------------------------------------------------------

race = ['American Indian or Alaskan Native', 'Asian',
        'Black or African American', 'White', 'Other']
number_per_race = [11, 7, 424, 1248, 45]

# Create a dictionary with the data
data = {
    'race': race,
    'PIT Count': number_per_race
}
# Create the DataFrame
PIT_race = pd.DataFrame(data)

# ------------------------------------------------------------------

sexes = ['Female', 'Male', 'Gender that is not singularly Female or Male',
         'Questioning', 'Transgender']
number_per_category = [568, 1131, 12, 5, 18]

# Create a dictionary with the data
data = {
    'sex': sexes,
    'PIT Count': number_per_category
    }
# Create the DataFrame
PIT_sex_expanded = pd.DataFrame(data)

#Had to create a new PIT dataset to match with the PVA dataset
#other includes Transgender and Questioning.
sex = ['FEMALE','MALE','OTHER',]
number_per_sex = [568, 1131, 36]

# Create a dictionary with the data
data = {
    'sex': sex,
    'PIT Count': number_per_sex
}
# Create the DataFrame
PIT_sex = pd.DataFrame(data)

# ------------------------------------------------------------------
# ------------------------------------------------------------------


def age_pit_graph_pie() -> go.Figure:
    fig = px.pie(PIT_age, values='PIT Count', names='Age Groups', hole=0.3)
    fig.update_traces(textposition='outside', textinfo='percent+label', hovertemplate='%{label}<br>Count = %{value}')
    fig.update_layout(
        title='Distribution of Number of People by Age Group in PIT (2023)',
        title_x=0.5,
        legend_title='Age Group',
        showlegend=True,
        width=600,
        height=600
    )
    return fig


def age_pva_graph_pie() -> go.Figure:
    fig = px.pie(df['AGE_GROUP'], names='AGE_GROUP', hole=0.3)
    fig.update_traces(textposition='outside', textinfo='percent+label', hovertemplate='%{label}<br>Count = %{value}')
    fig.update_layout(
        title='Distribution of People by Age in the PVA (2023)',
        title_x=0.5,
        legend_title='Age Group',
        showlegend=True,
        width=600,
        height=600
    )
    return fig


def age_pit_vs_pva_graph_bar() -> go.Figure:
    # Merge PVA and PIT data
    value_counts_df = df['AGE_GROUP'].value_counts().reset_index()
    value_counts_df.columns = ['Age Groups', 'PVA Count']
    age_demographics = value_counts_df.merge(
        PIT_age, how='inner', on='Age Groups', sort=True)

    age_demographics_pva = age_demographics[['Age Groups', 'PVA Count']].copy()
    age_demographics_pva['Type'] = 'PVA'
    age_demographics_pva.rename(columns={'PVA Count': 'Counts'}, inplace=True)

    age_demographics_pit = age_demographics[['Age Groups', 'PIT Count']].copy()
    age_demographics_pit['Type'] = 'PIT'
    age_demographics_pit.rename(columns={'PIT Count': 'Counts'}, inplace=True)

    age_demographics = pd.concat([age_demographics_pva, age_demographics_pit])

    # Calculate percentages
    age_demographics['Total'] = age_demographics.groupby(
        'Type')['Counts'].transform('sum')
    age_demographics['Percentage'] = (
        age_demographics['Counts'] / age_demographics['Total']) * 100
    age_demographics['Percentage'] = age_demographics['Percentage'].round(2)

    # Create and show the bar plot
    fig = px.bar(age_demographics, x='Type', y='Percentage',
                 color='Age Groups', title='Distribution of Individuals by Age')
    fig.update_layout(bargap=0.5, title_x=0.5,)
    return fig

def age_pit_vs_pva_findings_graph_bar():
    # Merge PVA and PIT data
    value_counts_df = df['AGE_GROUP'].value_counts().reset_index()
    value_counts_df.columns = ['Age Groups', 'PVA Count']
    age_demographics = value_counts_df.merge(
        PIT_age, how='inner', on='Age Groups', sort=True)
    
    age_demographics_diff=age_demographics.copy()
    age_demographics_diff['PIT Total'] = age_demographics_diff['PIT Count'].sum()
    age_demographics_diff['PVA Total'] = age_demographics_diff['PVA Count'].sum()
    age_demographics_diff['PIT Percentage'] = (age_demographics_diff['PIT Count'] / age_demographics_diff['PIT Total']) * 100
    age_demographics_diff['PIT Percentage'] = age_demographics_diff['PIT Percentage'].round(2)
    age_demographics_diff['PVA Percentage'] = (age_demographics_diff['PVA Count'] / age_demographics_diff['PVA Total']) * 100
    age_demographics_diff['PVA Percentage'] = age_demographics_diff['PVA Percentage'].round(2)
    age_demographics_diff['Percent Difference'] = age_demographics_diff['PIT Percentage'] - age_demographics_diff['PVA Percentage']
    age_demographics_diff['Difference'] = age_demographics_diff['PIT Count'] - age_demographics_diff['PVA Count']
    fig = px.bar(age_demographics_diff, x="Age Groups", y="Percent Difference", title="Difference between PIT and PVA by Age Group (PIT-PVA)")
    fig.update_layout(bargap=0.5, title_x=0.5)
    return fig

def race_pit_graph_pie() -> go.Figure:
    fig = px.pie(PIT_race, values='PIT Count', names='race', hole=0.3)

    fig.update_traces(textposition='outside', textinfo='percent+label', hovertemplate='%{label}<br>Count = %{value}')

    fig.update_layout(
        title='Distribution of People by Race in the PIT (2023)',
        legend_title='Race',
        showlegend=True
    )
    return fig


def race_pva_graph_pie() -> go.Figure:
    fig = px.pie(original_df['race'], names='race', hole=0.3)
    fig.update_traces(textposition='outside', textinfo='percent+label', hovertemplate='%{label}<br>Count = %{value}')
    fig.update_layout(
        title='Distribution of Individuals by Race in the PVA (2023)',
        legend_title='Race',
        showlegend=True,
    )
    return fig


def race_pit_vs_pva_graph_bar() -> go.Figure:
    # skip this question became "other"
    original_df['race'] = original_df['race'].apply(
        lambda x: 'Other' if x == 'Skip this question' else x)

    # Merge PVA and PIT data
    value_counts_df = original_df['race'].value_counts().reset_index()
    value_counts_df.columns = ['race', 'PVA Count']
    race_demographics = value_counts_df.merge(
        PIT_race, how='inner', on='race', sort=True)

    race_demographics_pva = race_demographics[['race', 'PVA Count']].copy()
    race_demographics_pva['Type'] = 'PVA'
    race_demographics_pva.rename(columns={'PVA Count': 'Counts'}, inplace=True)

    race_demographics_pit = race_demographics[['race', 'PIT Count']].copy()
    race_demographics_pit['Type'] = 'PIT'
    race_demographics_pit.rename(columns={'PIT Count': 'Counts'}, inplace=True)

    race_demographics = pd.concat(
        [race_demographics_pva, race_demographics_pit])

    # Calculate percentages
    race_demographics['Total'] = race_demographics.groupby(
        'Type')['Counts'].transform('sum')
    race_demographics['Percentage'] = (
        race_demographics['Counts'] / race_demographics['Total']) * 100
    race_demographics['Percentage'] = race_demographics['Percentage'].round(2)

    # Create and show the bar plot
    fig = px.bar(race_demographics, x='Type', y='Percentage',
                 color='race', title='Distribution of Individuals by Race')
    fig.update_layout(bargap=0.5,)
    return fig

def race_pit_vs_pva_findings_graph_bar():
    # skip this question became "other"
    original_df['race'] = original_df['race'].apply(
        lambda x: 'Other' if x == 'Skip this question' else x)

    # Merge PVA and PIT data
    value_counts_df = original_df['race'].value_counts().reset_index()
    value_counts_df.columns = ['race', 'PVA Count']
    race_demographics = value_counts_df.merge(
        PIT_race, how='inner', on='race', sort=True)
    
    race_demographics_diff = race_demographics.copy()
    race_demographics_diff['PIT Total'] = race_demographics_diff['PIT Count'].sum()
    race_demographics_diff['PVA Total'] = race_demographics_diff['PVA Count'].sum()
    race_demographics_diff['PIT Percentage'] = (race_demographics_diff['PIT Count'] / race_demographics_diff['PIT Total']) * 100
    race_demographics_diff['PIT Percentage'] = race_demographics_diff['PIT Percentage'].round(2)
    race_demographics_diff['PVA Percentage'] = (race_demographics_diff['PVA Count'] / race_demographics_diff['PVA Total']) * 100
    race_demographics_diff['PVA Percentage'] = race_demographics_diff['PVA Percentage'].round(2)
    race_demographics_diff['Percent Difference'] = race_demographics_diff['PIT Percentage'] - race_demographics_diff['PVA Percentage']
    race_demographics_diff['Difference'] = race_demographics_diff['PIT Count'] - race_demographics_diff['PVA Count']
    fig = px.bar(race_demographics_diff, x="race", y="Percent Difference", title="Distribution of Individuals by Race")
    fig.update_layout(bargap=0.5)
    return fig

def sex_pit_graph_pie() -> go.Figure:
    fig = px.pie(PIT_sex_expanded, values='PIT Count', names='sex', hole=0.3)

    fig.update_traces(textposition='outside', textinfo='percent+label', hovertemplate='%{label}<br>Count = %{value}')

    fig.update_layout(
        title='Distribution of People by Sex in the PIT',
        legend_title='Sex',
        showlegend=True,
    )
    return fig


def sex_pva_graph_pie() -> go.Figure:
    fig = px.pie(original_df['gender'], names='gender', hole=0.3)

    fig.update_traces(textposition='outside', textinfo='percent+label', hovertemplate='%{label}<br>Count = %{value}')

    fig.update_layout(
        title='Distribution of Individuals by Sex in the PVA',
        legend_title='Sex',
        showlegend=True,
    )
    return fig

def sex_pit_vs_pva_graph_bar() -> go.Figure:
    # Merge PVA and PIT data
    value_counts_df = df['gender'].value_counts().reset_index().rename(columns={'gender':'sex'})
    value_counts_df
    value_counts_df.columns = ['sex', 'PVA Count']
    sex_demographics = value_counts_df.merge(
        PIT_sex, how='inner', on='sex', sort=True)

    sex_demographics_pva = sex_demographics[['sex', 'PVA Count']].copy()
    sex_demographics_pva['Type'] = 'PVA'
    sex_demographics_pva.rename(columns={'PVA Count': 'Counts'}, inplace=True)

    sex_demographics_pit = sex_demographics[['sex', 'PIT Count']].copy()
    sex_demographics_pit['Type'] = 'PIT'
    sex_demographics_pit.rename(columns={'PIT Count': 'Counts'}, inplace=True)

    sex_demographics = pd.concat(
        [sex_demographics_pva, sex_demographics_pit])

    # Calculate percentages
    sex_demographics['Total'] = sex_demographics.groupby(
        'Type')['Counts'].transform('sum')
    sex_demographics['Percentage'] = (
        sex_demographics['Counts'] / sex_demographics['Total']) * 100
    sex_demographics['Percentage'] = sex_demographics['Percentage'].round(2)

    # Create and show the bar plot
    fig = px.bar(sex_demographics, x='Type', y='Percentage',
                color='sex', title='Distribution of Individuals by Sex')
    fig.update_layout(bargap=0.5,)
    return fig

def sex_pit_vs_pva_findings_graph_bar():
    # Merge PVA and PIT data
    value_counts_df = df['gender'].value_counts().reset_index().rename(columns={'gender':'sex'})
    value_counts_df
    value_counts_df.columns = ['sex', 'PVA Count']
    sex_demographics = value_counts_df.merge(
        PIT_sex, how='inner', on='sex', sort=True)
    
    sex_demographics_diff=sex_demographics.copy()
    sex_demographics_diff['PIT Total'] = sex_demographics_diff['PIT Count'].sum()
    sex_demographics_diff['PVA Total'] = sex_demographics_diff['PVA Count'].sum()
    sex_demographics_diff['PIT Percentage'] = (sex_demographics_diff['PIT Count'] / sex_demographics_diff['PIT Total']) * 100
    sex_demographics_diff['PIT Percentage'] = sex_demographics_diff['PIT Percentage'].round(2)
    sex_demographics_diff['PVA Percentage'] = (sex_demographics_diff['PVA Count'] / sex_demographics_diff['PVA Total']) * 100
    sex_demographics_diff['PVA Percentage'] = sex_demographics_diff['PVA Percentage'].round(2)
    sex_demographics_diff['Percent Difference'] = sex_demographics_diff['PIT Percentage'] - sex_demographics_diff['PVA Percentage']
    sex_demographics_diff['Difference'] = sex_demographics_diff['PIT Count'] - sex_demographics_diff['PVA Count']
    fig = px.bar(sex_demographics_diff, x="sex", y="Percent Difference", title="Difference between PIT and PVA by Sex (PIT-PVA)")
    fig.update_layout(bargap=0.5)
    return fig
