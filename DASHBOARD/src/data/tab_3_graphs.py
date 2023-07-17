import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from data.loader import load_dataframe
import pkg_resources
import json
import os

file_path1 = pkg_resources.resource_filename('data', 'cleaned_data.json')

df = load_dataframe(file_path1)

file_path = os.path.join(os.path.dirname(__file__), '..', 'utils', 'columns_mapping.json')
with open(file_path, 'r') as f:
    columns_mapping = json.load(f)


df["Demographic Grouping"] = df[["race", "gender"]].apply("-".join, axis=1)
scores = ['household_type_score', 'living_situation_score', 'health_scale_score',
       'LOT_homeless_score', 'risks_and_barriers_score', 'pva_priority_score']

def overall_scores_distribution() -> go.Figure:
    fig = px.box(df, x= 'Demographic Grouping',y = "pva_priority_score")
    return fig

class lot_homeless_graphs:

    df_lot=df.groupby(['Demographic Grouping', 'lot_homeless']).count()['age'].reset_index(name='counts')
    df_lot['Total'] = df_lot.groupby('Demographic Grouping')['counts'].transform('sum')
    df_lot['Percentage'] = (df_lot['counts'] / df_lot['Total']) * 100
    df_lot['Percentage'] = df_lot['Percentage'].round(2)

    @staticmethod
    def lot_homeless_graph1() -> go.Figure:
        fig = px.box(df, x= 'Demographic Grouping',y = "LOT_homeless_score")
        return fig

    @classmethod
    def lot_homeless_graph2(cls) -> go.Figure:
        value_to_filter = '8 or more years'
        lot_8 = cls.df_lot.loc[cls.df_lot['lot_homeless'] == value_to_filter]

        fig = px.bar(lot_8, x="Demographic Grouping", y="Percentage", title="Distribution of 8+ years in LOT Homeless by race and gender")
        fig.update_layout(bargap=0.5, title_x=0.5)
        fig.update_traces(marker_color='green')
        return fig

    @classmethod
    def lot_homeless_graph3(cls) -> go.Figure:
        value_to_filter1 = 'up to twelve months'
        lot_12 = cls.df_lot.loc[cls.df_lot['lot_homeless'] == value_to_filter1]

        fig = px.bar(lot_12, x="Demographic Grouping", y="Percentage", title="Distribution of under 12 months in LOT Homeless by race and gender")
        fig.update_layout(bargap=0.5, title_x=0.5)
        fig.update_traces(marker_color='#9467bd')
        return fig
    
    @staticmethod
    def lot_homeless_graph4() -> go.Figure:
        df_lot_score=df.groupby(['Demographic Grouping','LOT_homeless_score']).count()['age'].reset_index(name='counts')
        df_lot_score['Total'] = df_lot_score.groupby('Demographic Grouping')['counts'].transform('sum')
        df_lot_score['Percentage'] = (df_lot_score['counts'] / df_lot_score['Total']) * 100
        df_lot_score['Percentage'] = df_lot_score['Percentage'].round(2)
        value_to_filter = 1
        df_filtered = df_lot_score[df_lot_score['LOT_homeless_score'].eq(value_to_filter)]

        fig = px.bar(df_filtered, x="Demographic Grouping", y="Percentage", title="Distribution of score 1 in LOT Homeless by race and gender")
        fig.update_layout(bargap=0.5, title_x=0.5)
        fig.update_traces(marker_color='#1f77b4')
        return fig

class health_scale_graphs():

    df_health=df.groupby(['Demographic Grouping', 'health_scale']).count()['age'].reset_index(name='counts')
    df_health['Total'] = df_health.groupby('Demographic Grouping')['counts'].transform('sum')
    df_health['Percentage'] = (df_health['counts'] / df_health['Total']) * 100
    df_health['Percentage'] = df_health['Percentage'].round(2)

    @staticmethod
    def health_scale_graph1() -> go.Figure:
        fig = px.box(df, x= 'Demographic Grouping',y = "health_scale_score")
        return fig
    
    @classmethod
    def health_scale_graph2(cls) -> go.Figure:
        value_to_filter1 = 'Poor / Score 500'
        df_health_poor = cls.df_health.loc[cls.df_health['health_scale'] == value_to_filter1]
        fig = px.bar(df_health_poor, x="Demographic Grouping", y="Percentage", color='health_scale', title= "Distribution of Reported Poor Health by race and gender")
        fig.update_layout(bargap=0.5, title_x=0.5)
        fig.update_traces(marker_color='#1f77b4')
        return fig
    
class risks_and_barriers_graphs():

    @staticmethod
    def helper(col_name: str) -> pd.DataFrame:
        df_risks=df.groupby(['Demographic Grouping', col_name]).count()['age'].reset_index(name='counts')
        df_risks['Total'] = df_risks.groupby('Demographic Grouping')['counts'].transform('sum')
        df_risks['Percentage'] = (df_risks['counts'] / df_risks['Total']) * 100
        df_risks['Percentage'] = df_risks['Percentage'].round(2)
        return df_risks


    @staticmethod
    def risks_and_barriers_graph1() -> go.Figure:
        fig = px.box(df, x= 'Demographic Grouping',y = "risks_and_barriers_score")
        return fig
    
    @classmethod
    def risks_and_barriers_graph2(cls) -> go.Figure:
        col_name = 'discrimination?'
        df_d = cls.helper(col_name)
        index_names = df_d[ df_d['discrimination?'] == 'No'].index
        df_d.drop(index_names, inplace = True)
        index_names = df_d[ df_d['discrimination?'] == 'Skip'].index
        df_d.drop(index_names, inplace = True)

        fig = px.bar(df_d, x="Demographic Grouping", y="Percentage", color=col_name, title="Distribution of "+f'{col_name}'+" by race and gender")
        fig.update_traces(marker_color='steelblue')
        fig.update_layout(bargap=0.5, title_x=0.5)
        return fig

    @classmethod
    def risks_and_barriers_graph3(cls) -> go.Figure:
        df_dv = cls.helper('dv_parter_family?')
        df_dv1 = cls.helper('fleeing_dv?')
        index_names = df_dv[ df_dv['dv_parter_family?'] == 'No'].index
        df_dv.drop(index_names, inplace = True)
        index_names = df_dv[ df_dv['dv_parter_family?'] == 'Skip'].index
        df_dv.drop(index_names, inplace = True)

        index_names = df_dv1[ df_dv1['fleeing_dv?'] == 'No' ].index
        df_dv1.drop(index_names, inplace = True)
        df_dv1.drop([9])

        domestic_df = df_dv1.merge(df_dv, how = 'inner', on = 'Demographic Grouping')

        domestic_df["Experienced Domestic Violence"] = domestic_df['counts_x'] + domestic_df["counts_y"]
        domestic_df["Percent Experienced DV"] = domestic_df['Percentage_x'] + domestic_df["Percentage_y"]

        fig = px.bar(domestic_df, x="Demographic Grouping", y="Percent Experienced DV", title="Experienced Domestic Violence")
        fig.update_layout(bargap=0.5, title_x=0.5)
        fig.update_traces(marker_color='peachpuff')
        return fig
    
    @staticmethod
    def risks_and_barriers_graph4() -> go.Figure:
        # Category to count
        category_to_count = 'Skip'

        # Define the subset of columns to count occurrences
        risksbarriers = ['high_bp_household?','evicted?',
            'discrimination?', 'debt?', 'criminal_record?',
            'dv_parter_family?']

        # Count occurrences of the category in each cell for the subset of columns
        category_count_df = df[risksbarriers].applymap(lambda cell: cell == category_to_count)

        # Count occurrences of the category in each column
        column_counts = category_count_df.sum()

        # Calculate percentage of category occurrences in each column
        total_rows = len(df)
        column_percentages = (column_counts / total_rows) * 100

        # Create a final DataFrame with column names, counts, and percentages
        skip_df = pd.DataFrame({'Question': column_counts.index, 'Count': column_counts.values, 'Percentage': column_percentages.values})

        fig = px.bar(skip_df, x="Question", y="Percentage", title="Skips in Risks and Barriers")
        fig.update_layout(bargap=0.5, title_x=0.5)
        fig.update_traces(marker_color='darkslateblue')
        return fig
    

class household_type_graphs:
    
    @staticmethod
    def household_type_graph1() -> go.Figure:
        fig = px.box(df, x= 'Demographic Grouping',y = "household_type_score")
        return fig
    
    @staticmethod
    def household_type_graph2() -> go.Figure:
        df_dv1 = risks_and_barriers_graphs.helper('fleeing_dv?')
        index_names = df_dv1[ df_dv1['fleeing_dv?'] == 'No' ].index
        df_dv1.drop(index_names, inplace = True)

        fig = px.bar(df_dv1, x="Demographic Grouping", y="counts", color="fleeing_dv?", title="Fleeing Domestic Violence")
        fig.update_layout(bargap=0.5, title_x=0.5)
        return fig
    
    @staticmethod
    def household_type_graph3() -> go.Figure:
        household_scores_count = df['household_type_score'].value_counts().reset_index()
        household_scores_count.columns = ['Household Type Score', 'Count']
        household_scores_count.drop([0,1,2,3,4,6,8], inplace=True)
        fig = px.bar(household_scores_count, x= 'Household Type Score',y = 'Count', title='Count of scores indicating an individual is fleeing domestic violence')
        return fig
    
    @staticmethod
    def household_type_graph4() -> go.Figure:
        colm_name = 'household_type_score'
        df_house_score = risks_and_barriers_graphs.helper(colm_name)
        fig = px.bar(df_house_score, x="Demographic Grouping", y="counts", color=colm_name, title="Distribution of Household Type Score by race and gender")
        fig.update_layout(bargap=0.5, title_x=0.5)
        return fig
    
    @staticmethod
    def household_type_graph5() -> go.Figure:
        colm_name = 'household_type_score'
        df_house_score = risks_and_barriers_graphs.helper(colm_name)
        fig = px.bar(df_house_score, x="Demographic Grouping", y="Percentage", color=colm_name, title="Distribution of Household Type Score by race and gender")
        fig.update_layout(bargap=0.5, title_x=0.5)
        return fig
    
    @staticmethod
    def household_type_graph6() -> go.Figure:
        colm_name = 'household_size'
        df_housesize = risks_and_barriers_graphs.helper(colm_name)
        fig = px.bar(df_housesize, x="Demographic Grouping", y="counts", color=colm_name, title="Distribution of Household Size by race and gender")
        fig.update_layout(bargap=0.5, title_x=0.5)
        return fig
    
    @staticmethod
    def household_type_graph7() -> go.Figure:
        colm_name = 'household_size'
        df_housesize = risks_and_barriers_graphs.helper(colm_name)
        fig = px.bar(df_housesize, x="Demographic Grouping", y="Percentage", color=colm_name, title="Distribution of Household Size by race and gender")
        fig.update_layout(bargap=0.5, title_x=0.5)
        return fig

    
class living_situation_graphs():

    @staticmethod
    def living_situation_graph1() -> go.Figure:
        fig = px.box(df, x= 'Demographic Grouping',y = "living_situation_score")
        return fig
    
    @staticmethod
    def living_situation_graph2() -> go.Figure:
        colm_name = 'living_situation'
        df_ls = risks_and_barriers_graphs.helper(colm_name)
        index_names = df_ls[df_ls['living_situation'] == 'Prison / jail'].index
        df_ls.drop(index_names, inplace = True)
        index_names = df_ls[df_ls['living_situation'] == 'Doubled up / couch surfing'].index
        df_ls.drop(index_names, inplace = True)
        index_names = df_ls[df_ls['living_situation'] == 'Hotel or temporary rental requiring ongoing payment'].index
        df_ls.drop(index_names, inplace = True)
        index_names = df_ls[df_ls['living_situation'] == 'Own home, including rental and family housing'].index
        df_ls.drop(index_names, inplace = True)
        index_names = df_ls[df_ls['living_situation'] == 'Medical or behavioral health inpatient care'].index
        df_ls.drop(index_names, inplace = True)

        fig = px.bar(df_ls, x="Demographic Grouping", y="Percentage", color=colm_name, title="Distribution of Literal Homelessness by race and gender", color_discrete_sequence=["blue", "goldenrod", "magenta"])
        fig.update_layout(bargap=0.5, title_x=0.5)
        return fig
    
    @staticmethod
    def living_situation_graph3() -> go.Figure:
        colm_name = 'living_situation_score'
        df_ls_score = risks_and_barriers_graphs.helper(colm_name)
        index_names = df_ls_score[df_ls_score['living_situation_score'] < 5].index
        df_ls_score.drop(index_names, inplace = True)
        fig = px.bar(df_ls_score, x="Demographic Grouping", y="Percentage", color=colm_name, title="Distribution of Literal Homelessness Scoring by race and gender", color_discrete_sequence=["blue", "goldenrod", "magenta"])
        fig.update_layout(bargap=0.5)
        return fig