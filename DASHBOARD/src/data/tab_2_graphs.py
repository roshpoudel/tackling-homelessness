import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from data.loader import load_dataframe
import pkg_resources
import json
import os


file_path1 = pkg_resources.resource_filename('data', 'cleaned_data.json')

df = load_dataframe(file_path1)

file_path = os.path.abspath(__file__)
dir_path = os.path.dirname(file_path)
mapping_file_path = os.path.join(
    dir_path, '..', 'utils', 'columns_mapping.json')

with open(mapping_file_path, 'r') as f:
    columns_mapping = json.load(f)


def create_plot(col_name: str, y_axis: str) -> go.Figure:
    """
    This function creates a plotly bar chart for the given column name and y-axis type.

    Args:
    col_name (str): The name of the column to be plotted.
    y_axis (str): The type of y-axis to be used. It can be either 'count' or 'percent'.

    Returns:
    go.Figure: A plotly figure object.
    """
    tmp = col_name
    # adding column which combines race and sex
    df["Demographic Grouping"] = df[["race", "gender"]].apply("-".join, axis=1)

    fig = go.Figure()
    if col_name in columns_mapping:
        col_name = columns_mapping[col_name]

    df1 = df.groupby(['Demographic Grouping', col_name]).count()[
        'age'].reset_index(name='counts')
    df1['Total'] = df1.groupby('Demographic Grouping')[
        'counts'].transform('sum')
    df1['Percentage'] = (df1['counts'] / df1['Total']) * 100
    df1['Percentage'] = df1['Percentage'].round(2)

    if y_axis == 'count':
        fig = px.bar(df1, x="Demographic Grouping", y="counts", color=col_name,
                     title="Distribution of "+tmp+" by race and gender (count))")
    elif y_axis == 'percent':
        fig = px.bar(df1, x="Demographic Grouping", y="Percentage", color=col_name,
                     title="Distribution of "+tmp+" by race and gender (percentage)")

    fig.update_layout(bargap=0.5,
                      title_x=0.5,
                      height=600,
                      width=1300,)
    return fig
