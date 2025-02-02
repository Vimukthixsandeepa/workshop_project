# Analyzing and Visualizing Wine Data

## Overview
This project delves into analyzing data collected from wine brands across various countries. It focuses on data preparation, visualization, and applying machine learning techniques to derive actionable insights. The project also leverages natural language processing (NLP) to classify customer reviews, providing a comprehensive understanding of consumer preferences.

## Objectives
- Analyze wine data to uncover patterns and insights.
- Build interactive visualizations and dashboards for data-driven storytelling.
- Use a HuggingFace NLP model to classify customer reviews into meaningful categories.

## Features
### Data Preparation
- **Data Loading**: Combined data from 8 CSV files into a single DataFrame.
- **Cleaning**:
  - Removed duplicates.
  - Handled null values (imputation/removal).
  - Identified and addressed outliers.
- **Feature Engineering**:
  - Extracted `Country` and `Country_region` from the region column.
  - Expanded food pairings into separate columns with TRUE/FALSE values.

### Machine Learning and NLP
- Classified 500 customer reviews for "Merry Edwards Sauvignon Blanc 2023" into four categories:
  1. Food Combinations
  2. Taste
  3. Value for Money
  4. Other
- Used HuggingFace zero-shot classification models to gain actionable insights.

### Interactive Dashboard
Built using **Plotly Dash** with the following features:
- **Charts**:
  - Bar Chart: Wine Styles by Ratings.
  - Scatter Plot: Price vs Ratings.
  - Pie Chart: Food Pairings.
  - Box Plot: Alcohol Content, Sweetness, and Acidity by Wine Style.
  - Line Chart: Average Price over Ratings.
- **Interactivity**:
  - Filters: Dynamic filtering by country, price, and wine style.
  - Hover Effects: Display additional data (e.g., winery name, food pairings).
  - Clickable Charts: Drill-down into specific categories.

## Insights
- Identified countries producing highly-rated wines at affordable prices.
- Highlighted popular food pairings for specific wine styles.
- Analyzed regional trends in alcohol content and sensory characteristics.

## Tools and Technologies
- **Programming Language**: Python
- **Libraries**:
  - Data Analysis: Pandas
  - Visualization: Plotly Dash
  - Machine Learning: HuggingFace Transformers
- **Data Source**: 8 CSV files of wine data from various countries.

## Team Members
- M. V. V. S. Millavitiya
- K. A. Nilupul Nishan
- W. A. Ishara Lakmal
- W. V. P. Imalsha Lakshan
- P. I. D. De Silva
- N. L. Muthukuda Arachchi
- I. D. K. H. Jayasinghe
- C. A. S. Malsha
- W. K. H. V. Perera
- P. T. H. Fernando

## Conclusion
This project demonstrates the potential of data-driven decision-making in the wine industry by combining data analysis, machine learning, and storytelling through interactive dashboards.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
