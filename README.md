# Operations & CRM Performance Dashboard with Retention Analysis

End-to-end CRM analytics using simulated eCommerce and streaming data to identify retention drivers, optimize purchase funnels, and predict repurchase likelihood. Includes automated pipelines, real-time scoring APIs with Spring Boot, and interactive Power BI dashboards for actionable retention insights.


 
## Table of Contents  
1. [Descriptive Analysis Questions](#descriptive-analysis-questions)  
2. [Exploratory Analysis Questions](#exploratory-analysis-questions)  
3. [Retention Cohort Analysis](#predictive-modeling-questions)  
4. [Key Findings & Conclusion](#key-findings--conclusion)  
5. [Screenshots to Include](#screenshots-to-include)  
6. [Usage Instruction](#usage-instruction)
7. [Future work](#future-work)

   
## Descriptive Analysis Questions
| #  | Question   
|---|------------------------------------------------
| 1  | Order & Fulfillment Overview  
-  What are the daily, weekly, and monthly order volumes?
-  Q2: What is the average fulfillment cycle time (order → delivery) over time?
-  Q3: What percentage of orders are delivered on time (OTD %)?
-  Q4: How does return rate vary by product category and month?
| 2  | Inventory & Returns
- Q5: How do inventory levels fluctuate relative to order peaks?                                                        
| 3  | High-Level CRM Descriptives
- Q6: Overall open rate, click-through rate (CTR), and unsubscribe rate by channel.
- Q7: Open/CTR/unsubscribe broken out by customer segment (new vs. repeat vs. inactive).
- Q8: Open/CTR/unsubscribe by age group and region.                                                                        




## Exploratory Analysis Questions  

| #  | Question                                                                                                                                              
|----|------------------------------------------------
| 1  |  Subject Line A/B Performance 
* Q1: Do variant A vs B subject lines produce statistically significant differences in open rate?
* Q2:  Is the effect of subject variant on open rate consistent across segments and channels, or explained by confounders
| 2  | Timing & Frequency Effects
* Q3: Does send time (hour/day) affect open/CTR?
* Q4: How does customer engagement fatigue—measured by cumulative opens and inactivity periods—influence unsubscribe rates and purchase likelihood?                                                                                           
| 3  | Segment-Level Insights
* Q5: Which customer segments (RFM quintiles, new vs. repeat) respond best to promotions vs. newsletters?
* Q6: What is the interplay between purchase frequency and email engagement?
* Q7: For engaged customers (opened/clicked), what is the uplift in next-30-day order rate and average order value vs. non-openers?                                                                    
## Retention Cohort Analysis
| #  | Question                                                                                                                                             |----|-------------------------------------------------------------------------------------------------------------------
| 1  | Subject Line A/B Performance
* Q1: Do variant A vs B subject lines produce statistically significant differences in open rate?
* Q2:  Is the effect of subject variant on open rate consistent across segments and channels, or explained by confounders
| 2  | Timing & Frequency Effects driver based on past behavior
* Q3: Does send time (hour/day) affect open/CTR?                     * Q4: How does customer engagement fatigue—measured by cumulative opens and inactivity periods—influence unsubscribe rates and purchase likelihood?    
| 3  | Segment-Level Insights
* Q5: Which customer segments (RFM quintiles, new vs. repeat) respond best to promotions vs. newsletters?
* Q6: What is the interplay between purchase frequency and email engagement?
* Q7: For engaged customers (opened/clicked), what is the uplift in next-30-day order rate and average order value vs. non-openers?
