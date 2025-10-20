# Data Analysis Instruction Template
Guide AI to perform structured data analysis and generate insights.

## Metadata
---
version: 1.0
author: [Your Name]
created: YYYY-MM-DD
analysis_type: [exploratory | diagnostic | predictive | prescriptive]
target_model: [OpenAI GPT-4o, Claude Sonnet, etc.]
---

## Purpose
[What question are you trying to answer? What decision will this analysis inform?]

## Dataset Information
- **Source**: [File name, database, API, etc.]
- **Format**: [CSV, JSON, Excel, SQL, etc.]
- **Size**: [Rows × Columns, file size]
- **Date Range**: [Time period covered]
- **Key Fields**: {{FIELD_1}}, {{FIELD_2}}, {{FIELD_3}}

## Data Sample
```
[Paste first 5-10 rows or representative sample]
```

## Analysis Objectives
1. [Primary question: e.g., "What factors correlate with customer churn?"]
2. [Secondary question: e.g., "Which segments show highest retention?"]
3. [Additional objectives]

## Required Analyses
- [ ] **Descriptive Statistics**: Mean, median, mode, standard deviation
- [ ] **Data Quality**: Missing values, outliers, duplicates
- [ ] **Distributions**: Histograms, frequency tables
- [ ] **Correlations**: Relationships between variables
- [ ] **Segmentation**: Group comparisons, cohort analysis
- [ ] **Trends**: Time series patterns, seasonality
- [ ] **Anomalies**: Unusual patterns or outliers

## Constraints & Assumptions
- [Statistical significance threshold: e.g., p < 0.05]
- [Known data limitations or biases]
- [Business rules or domain constraints]
- [Privacy/compliance requirements]

## Output Requirements
- **Format**: Markdown report with embedded code blocks
- **Structure**:
  1. Executive Summary (3-5 key findings)
  2. Data Quality Assessment
  3. Detailed Analysis (with visualizations described)
  4. Statistical Tests & Results
  5. Insights & Recommendations
  6. Methodology & Assumptions
- **Style**: Professional, data-driven, non-technical language for summary
- **Visualizations**: Describe charts needed (you'll create separately)

## Variables
| Variable | Description | Example |
|----------|-------------|---------|
| {{METRIC}} | [Primary KPI] | Revenue, Conversion Rate |
| {{DIMENSION}} | [Grouping variable] | Region, Product Category |
| {{DATE_RANGE}} | [Analysis period] | 2024-01-01 to 2024-12-31 |

## Success Criteria
- [How will you know the analysis is complete and useful?]
- Example: "Provides actionable recommendations with statistical backing"
- Example: "Identifies top 3 drivers of {{METRIC}} with confidence intervals"
