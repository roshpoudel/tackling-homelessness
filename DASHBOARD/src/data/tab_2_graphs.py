import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from data.loader import load_dataframe
import pkg_resources
import json


file_path1 = pkg_resources.resource_filename('data', 'original_df.json')

df = load_dataframe(file_path1)

with open('/Users/roshan/Documents/DLProjectWork/Fighting-Homelessness-2023/DASHBOARD/src/utils/columns_mapping.json', 'r') as f:
    columns_mapping = json.load(f)


def create_plot(col_name: str) -> go.Figure:
    tmp = col_name
    #adding column which combines race and sex
    df["Demographic Grouping"] = df[["race", "gender"]].apply("-".join, axis=1)

    fig = go.Figure()
    if col_name in columns_mapping.keys():
        col_name = columns_mapping[col_name]

    print(col_name)
    df1=df.groupby(['Demographic Grouping', col_name]).count()['age'].reset_index(name='counts')
    fig.add_trace(px.bar(df1, x="Demographic Grouping", y="counts", color=col_name, title="Distribution of "+col_name+" by race and gender").data[0])
    fig.update_layout(bargap=0.5, title=f"Distribution of responses to {tmp} by race and gender")
    return fig

create_plot("LOT Homeless")

