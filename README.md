# Datalab 2023 - Fighting Homelessness

This repository contains the code for the dashboard that we developed for the Chattanooga Regional Homeless Coalition (CRHC), which is a lead agency of Southeast Tennessee's Continuum of Care. Our team of 21 fellows from 8 different schools around the country worked with CRHC during Datalab-2023, a "Data Science for Social Good" program at University of the South, Sewanee, TN. With mentorship from industry professionals and researchers from Stanford and UofSouth, we aimed to help CRHC make their intake survey/assessment more trauma-informed, equitable, and effective in providing essential services to unsheltered individuals in the area. This dashboard was built using Plotly Dash and provides insights into the PVA and PIT, as well as our findings. 

## Installation

This dashboard is primarily built on Plotly Dash framework, which is a Python web application framework for building interactive web-based dashboards. It uses other Python libraries like pandas, json, os, and math for data manipulation and analysis. First you need to install python in your computer. You can follow the instructions from here: 

> https://www.python.org/downloads/


To run this program in Dash, you need to install the required libraries by running the following command in your terminal:

```pip install dash dash-bootstrap-components pandas plotly matplotlib seaborn```

Also, if you are on a conda environment, there's a yaml file in '/environment/conda.yaml'. To create a conda environment using this file, follow these steps:

1. Open a terminal window and navigate to the directory where the `conda.yaml` file is located.
2. Run the following command to create a new conda environment with the name `myenv`:

    ```conda env create -f conda.yaml -n myenv```

    This will create a new conda environment with all the required dependencies installed.
3. Activate the new environment by running the following command:

    ```conda activate myenv```

    You should now be able to run the dashboard using the new conda environment.

Note: If you want to remove the environment, you can run the following command:  ```conda env remove -n myenv```
    

## Usage

## Viewing the Dashboard

To view the insights about the PVA and PIT and the findings, follow these steps:

1. Clone or download the repository to your local machine by running the following command on your terminal:

```git clone https://github.com/sewaneedata/Fighting-Homelessness-2023```

2. Navigate to the `src` directory in your terminal.
3. Run the following command to start the dashboard:

    ```python main.py```

4. Open your web browser and go to `http://localhost:8050/` to view the dashboard.

You should now be able to view the insights and findings in the dashboard. Since the data is not publicly available, **unauthorized users** will not be able to view the dashboard as it would require the datasets for the graphs to show up.

## Issues and Support

For issues and support, please contact:
    datalab@sewanee.edu

For code-related issues, please contact:
    pouder0@sewanee.edu

