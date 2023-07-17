import math
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots


class Plotter:
    """
    Base class for creating plotter objects.

    Parameters:
        df (DataFrame): The input DataFrame to plot.
        num_cols (int): Number of columns for the subplot grid.
    """

    def __init__(self, df, num_cols=3):
        """
        Initializes a Plotter object.

        Args:
            df (DataFrame): The input DataFrame to plot.
            num_cols (int): Number of columns for the subplot grid.
        """
        self.df = df
        self.num_cols = num_cols
        self.num_plots = len(df.columns) if df is not None else 0
        self.num_rows = math.ceil(self.num_plots / self.num_cols)

    # Function to truncate column names
    @staticmethod
    def truncate_string(text, max_length):
        return text[:max_length - 3] + "..." if len(text) > max_length else text

    def plot_plots(self):
        """
        Plots the subplots of the DataFrame columns.
        """
        if self.num_plots == 0:
            print("No data to plot.")
            return

        # Create a list to store column names with more than one unique value
        valid_columns = []

        # Check if the column has more than one unique value
        for column in self.df.columns:
            if self.df[column].nunique() > 1:
                valid_columns.append(column)

        # Create the subplots grid
        fig = make_subplots(rows=self.num_rows,
                            cols=self.num_cols, subplot_titles=valid_columns)

        # Loop through each valid column
        for i, column in enumerate(valid_columns):
            numeric_column_list = self.df._get_numeric_data().columns
            if column in numeric_column_list:
                self.kdeplot(column, fig, i + 1)
            else:
                self.histplot(column, fig, i + 1)

        # Update subplot layout settings
        fig.update_layout(
            showlegend=False,
            height=400 * self.num_rows,
            width=800,
            title_font=dict(size=12),
            font=dict(size=8),  # Decrease the font size
            hovermode='x unified',
            # title_text="Plotter in Plotly",  # Set the main title
            margin=dict(t=100, b=10)  # Adjust the top and bottom margins
        )

        # Update axis layout settings
        fig.update_xaxes(showticklabels=False)
        fig.update_yaxes(showticklabels=True)

        # Truncate and adjust subplot titles
        max_title_length = 20  # Maximum number of characters for each title
        for i, subplot_title in enumerate(fig.layout.annotations):
            # Set the full title as hover text
            subplot_title.hovertext = subplot_title.text

            # Truncate the title if needed
            truncated_title = self.truncate_string(
                subplot_title.text, max_title_length)
            fig.layout.annotations[i].text = truncated_title

        return fig

    def histplot(self, column, fig, subplot_index, order_='ascending'):
        """
        Plots a histogram for a single column.

        Args:
            column (str): The name of the column to plot.
            fig (plotly.graph_objs.Figure): The Plotly figure object.
            subplot_index (int): The index of the subplot.
        """
        # Create the histogram trace
        hist_trace = go.Histogram(x=self.df[column], name=column)

        # Add the trace to the subplot
        fig.add_trace(hist_trace, row=(subplot_index - 1) //
                      self.num_cols + 1, col=(subplot_index - 1) % self.num_cols + 1)

    def kdeplot(self, column, fig, subplot_index):
        """
        Plots a kernel density estimation plot for a single column.

        Args:
            column (str): The name of the column to plot.
            fig (plotly.graph_objs.Figure): The Plotly figure object.
            subplot_index (int): The index of the subplot.
        """
        # Create the KDE plot trace as a violin plot
        kde_trace = go.Violin(
            y=self.df[column],
            name=column,
            box_visible=True,
            meanline_visible=True,
            fillcolor='lightseagreen',
            line_color='darkgreen'
        )

        # Add the trace to the subplot
        fig.add_trace(kde_trace, row=(subplot_index - 1) //
                      self.num_cols + 1, col=(subplot_index - 1) % self.num_cols + 1)

# Create a sample DataFrame
#plotter = Plotter(df, num_cols=3)
# plotter.plot_plots().show()
