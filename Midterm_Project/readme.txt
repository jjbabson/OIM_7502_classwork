U.S. Air Quality Explorer – Altair Demo

Author: Jose Juan Gonzalez
Library: Altair

Dataset: EPA Daily AQI by County (2025)

Overview

This project demonstrates the use of the Altair library to explore and visualize air quality (AQI) data across the United States. The dataset contains daily AQI readings by county, allowing us to analyze trends, identify highly polluted areas, and explore correlations with the number of monitoring sites.

The notebook showcases:

Data cleaning and preparation for visualization
Summary metrics for quick insights
Histograms and boxplots for AQI distribution
Bar charts of the most and least polluted counties
Scatterplots with regression lines to explore correlations
Choropleth maps to visualize AQI by state and county

Key Features

Data Cleaning & Preparation
Standardizes column names using .str.lower(), .str.strip(), and .str.replace().
Ensures compatibility with Python and Altair for smooth plotting.
Sampling for Large Datasets
	Altair has a row limit of ~5000; the notebook uses .sample(4999, random_state=42) to avoid errors.
	Sampling ensures reproducibility and quick rendering.

Visualizations

Histogram: Shows the distribution of AQI across counties, with adjustable binning and Y-axis scaling.
Boxplot: Displays AQI by category, with custom ordering from “Hazardous” to “Good” and capped Y-axis for readability.
Bar Charts: Highlights top 15 most polluted and bottom 15 least polluted counties.
Scatterplot: Correlation between the number of sites reporting and AQI, with regression line and color by AQI category.
Choropleth Maps: State-level and county-level maps with color scales representing average AQI.

Interactivity

Tooltips display detailed information for each data point.
Sorting, ordering, and color encoding allow quick visual insights.

Variations / Extensions

The notebook includes ideas for modifications, such as:
Showing the least polluted counties instead of the most polluted.
Adjusting Y-axis limits and sampling thresholds for readability.
Using polynomial or robust regression in scatterplots.
Filtering by individual states using interactive dropdowns (via ipywidgets).
These demonstrate the flexibility of Altair for exploratory data analysis.

Getting Started with Altair

For more information on Altair:

Overview: Altair Getting Started
Gallery / Examples: Altair Example Gallery
Altair is a declarative visualization library for Python, meaning you describe what you want to see, and it handles the rendering automatically. It’s excellent for clean, interactive, and reproducible visualizations.

How to Run

Install required packages:

pip install pandas altair vega_datasets


Open the notebook in Jupyter.

Run cells sequentially to see all charts and metrics.
Tip: If you encounter performance issues with large datasets, adjust the sample size in the notebook.

Acknowledgements

Data source: EPA Air Quality Data

Visualization library: Altair