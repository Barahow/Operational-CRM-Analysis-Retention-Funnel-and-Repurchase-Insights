# Operations & CRM Performance Dashboard with Retention Analysis

End-to-end CRM analytics using simulated eCommerce and streaming data to identify retention drivers, optimize purchase funnels, and predict repurchase likelihood. Includes automated pipelines and interactive Power BI dashboards for actionable retention insights.

## Table of Contents  
1. [Descriptive Analysis Questions](#descriptive-analysis-questions)  
2. [Exploratory Analysis Questions](#exploratory-analysis-questions)  
3. [Retention Cohort Analysis](#retention-cohort-analysis)  
4. [Key Findings & Conclusion](#key-findings--conclusion)  
5. [Screenshots to Include](#screenshots-to-include)  
6. [Usage Instruction](#usage-instruction)  
7. [Future work](#future-work)

## Descriptive Analysis Questions

| #  | Question | Sub-questions |
|---|------------------------------------------------|---------------|
| 1  | Order & Fulfillment Overview | What are the daily, weekly, and monthly order volumes? What is the average fulfillment cycle time from order to delivery over time? What percentage of orders are delivered on time (OTD%)? How does return rate vary by product category and month? |
| 2  | Inventory & Returns | How do inventory levels fluctuate relative to order peaks? |
| 3  | High-Level CRM Descriptives | Overall open rate, click-through rate (CTR), and unsubscribe rate by channel. Open/CTR/unsubscribe broken out by customer segment (new vs repeat vs inactive). Open/CTR/unsubscribe by age group and region. |

## Exploratory Analysis Questions

| #  | Question | Sub-questions |
|----|------------------------------------------------|---------------|
| 1  | Subject Line A/B Performance | Do variant A vs B subject lines produce statistically significant differences in open rate? Is the effect of subject variant on open rate consistent across segments and channels or explained by confounders? |
| 2  | Timing & Frequency Effects | Does send time (hour/day) affect open/CTR? How does customer engagement fatigue, measured by cumulative opens and inactivity periods, influence unsubscribe rates and purchase likelihood? |
| 3  | Segment-Level Insights | Which customer segments (RFM quintiles, new vs repeat) respond best to promotions vs newsletters? What is the interplay between purchase frequency and email engagement? For engaged customers (opened/clicked), what is the uplift in next-30-day order rate and average order value compared with non-openers? |

## Retention Cohort Analysis

| #  | Question | Sub-questions |
|----|------------------------------------------------|---------------|
| 1  | Subject Line A/B Performance | Do variant A vs B subject lines produce statistically significant differences in open rate? Is the effect of subject variant on open rate consistent across segments and channels or explained by confounders? |
| 2  | Timing & Frequency Effects driver based on past behavior | Does send time (hour/day) affect open/CTR? How does customer engagement fatigue, measured by cumulative opens and inactivity periods, influence unsubscribe rates and purchase likelihood? |
| 3  | Segment-Level Insights | Which customer segments (RFM quintiles, new vs repeat) respond best to promotions vs newsletters? What is the interplay between purchase frequency and email engagement? For engaged customers (opened/clicked), what is the uplift in next-30-day order rate and average order value compared with non-openers? |

## Key Findings & Conclusion  
Key Findings & Conclusion

### Exploratory analysis

Subject variant B yields a consistent 0.9% higher open rate than variant A. The difference is statistically significant but small in magnitude. Channel choice explains far more variance than subject variant. Cumulative opens strongly predict both purchases and unsubscribes. Repeat customers are significantly more likely to make a purchase. Time of send shows no reliable pattern; the Sunday 00:00 signal is an artifact of noisy or synthetic timestamps, not an operational recommendation. Model fit is weak. Treat statistically significant coefficients as signals, not turnkey levers.

### Retention and cohort analysis

Six-month churn centers around 14 to 15 percent across RFM segments, with high value customers showing slightly higher churn. Early cohorts show inflated retention because of short observation windows or sparse data. Later cohorts lack a full six-month window, leading to biased low retention. Overall retention stabilizes after initial periods, but long term estimates are not reliable until the observation window and data completeness are fixed.


## Screenshots to Include

**Python Analysis**  
![Is the effect of subject variant on open rate consistent across segments and channels, or explained by confounders?](screenshots/python_Model_Significance_Order.pgn)  
*Figure: Logit Regression Results *  

![Which customer segments (RFM quintiles, new vs. repeat) respond best to promotions vs. newsletters](screenshots/python_RFM_quintiles_new vs. repeat.pgn)  
*Figure: Linear Model Regression Results  *  

![How does customer engagement fatigue-measured by cumulative opens and inactivity periods-influence unsubscribe rates and purchase likelihood?](screenshots/python_purchase_summary.pgn)  
*Figure:  Logit Regression Results *  



**Power BI Dashboard**  
![Customer Churn Overview tab](screenshots/CRM_overview_tab)  
*Figure: CRM Overview with KPIs, trends, and top Product categories*

![Customer Risk Analysis tab](screenshots/customer_risk_analysis_tab)  
*Figure: Customer risk insight with KPIs, Churn rate by RFM segments, and regions.*

![Email Marketing performance tab](screenshots/email_marketing_performance_tab)  
*Figure: Email marketing performance with KPIs, trends, and underperforming campaigns*



