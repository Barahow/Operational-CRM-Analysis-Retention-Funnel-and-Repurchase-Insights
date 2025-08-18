# Operations & CRM Performance Dashboard with Retention Analysis

End-to-end CRM analytics using historical eCommerce and email marketing data to analyze customer behavior, identify retention drivers, measure churn, and evaluate email engagement. Includes automated Python analysis pipelines, logistic and linear modeling, and interactive Power BI dashboards for actionable retention and cohort insights.

## Table of Contents
1. [Descriptive Analysis Questions](#descriptive-analysis-questions)  
2. [Exploratory Analysis Questions](#exploratory-analysis-questions)  
3. [Retention Cohort Analysis](#retention-cohort-analysis)  
4. [Results and Analysis Summary](#results-and-analysis-summary)  
5. [Key Findings & Conclusion](#key-findings--conclusion)  
6. [Screenshots to Include](#screenshots-to-include)  
7. [Usage Instruction](#usage-instruction)  
8. [Future work](#future-work)

## Descriptive Analysis Questions

| # | Question | Sub-questions |
|---|----------|---------------|
| 1 | Order & Fulfillment Overview | What are daily, weekly, and monthly order volumes? What is the average fulfillment cycle time from order to delivery over time? What percentage of orders are delivered on time (OTD%)? How does return rate vary by product category and month? |
| 2 | Inventory & Returns | How do inventory levels fluctuate relative to order peaks? |
| 3 | High-Level CRM Descriptives | Overall open rate, click-through rate (CTR), and unsubscribe rate by channel. Open/CTR/unsubscribe by customer segment (new vs repeat vs inactive). Open/CTR/unsubscribe by age group and region. |

## Exploratory Analysis Questions

| # | Question | Sub-questions |
|---|----------|---------------|
| 1 | Subject Line A/B Performance | Do variant A and variant B subject lines produce statistically significant differences in open rate? Is the effect consistent across segments and channels or explained by confounders? |
| 2 | Timing & Frequency Effects | Does send time (hour/day) affect open or CTR? How does customer engagement fatigue, measured by cumulative opens and inactivity periods, influence unsubscribe rates and purchase likelihood? |
| 3 | Segment-Level Insights | Which segments (RFM quintiles, new vs repeat) respond best to promotions versus newsletters? What is the interplay between purchase frequency and email engagement? For engaged customers, what is the uplift in next-30-day order rate and average order value compared with non-openers? |

## Retention Cohort Analysis

| # | Question | Sub-questions |
|---|----------|---------------|
| 1 | Subject Line A/B Performance | Do A/B subject variants change open rates within cohorts? Are effects persistent across cohort ages? |
| 2 | Timing & Frequency Effects (behavioral drivers) | Does send time affect open/CTR within cohorts? How does engagement fatigue influence cohort-level unsubscribe and repurchase behavior? |
| 3 | Segment-Level Insights | Which cohorts and RFM segments show the strongest retention and LTV signals? What treatment rules should govern promotional cadence per segment? |

## Results and Analysis Summary

### Churn Analysis by RFM Segment
Churn rates using a six-month retention cutoff:
- Low-Value Customers: churn ~13.9%. Lower engagement and purchase frequency.
- Mid-Value Customers: churn ~14.7%. Moderate activity and retention.
- High-Value Customers: churn ~15.1%. High spend does not guarantee retention.

Observation: Differences are small but measurable. All segments show non-trivial churn and will benefit from targeted retention.

### Cohort Retention Analysis Summary
- Early cohorts (starting July 2024) show high retention, likely due to initial engagement or limited data volume.  
- One-month and three-month retention remain relatively stable across cohorts.  
- Six-month retention declines sharply for later cohorts because of incomplete observation windows.  
- Recent cohorts lack a full six-month window, producing artificially low six-month retention.  
- Retention stabilizes after initial growth, but long-term estimates require complete data and proper censoring.

### Subject Line A/B Performance (Python analysis)
- Two-proportion z-test: Z = -32.86, p-value approximately 0. Effect size (A - B) = -0.00937. Variant B open rate is ~0.9 percentage points higher than A. 95% CI = (-0.00993, -0.00881).  
- Channel effects exceed subject effects. Promotional, loyalty, and transactional channels give the largest open-rate lift. Variant B increases open likelihood with a smaller effect than top channels.  
- Segment and interaction effects are mostly insignificant. Newsletter and survey channels show weak impact.

Conclusion: Statistically significant difference between A and B. Effect size small. Report both statistical and practical significance.

### Logistic regression: unsubscribe summary
- days_since_last_purchase_cum_scaled: strong negative coefficient, p < 0.001. Longer inactivity correlates with lower unsubscribe probability.  
- cumulative_opens_scaled: strong positive coefficient, p < 0.001. More cumulative opens increase unsubscribe risk.  
- Segment type (new vs repeat) not significant.

Conclusion: Engagement fatigue is real. Frequent openers have higher unsubscribe risk. Use cumulative opens for targeting with retention guardrails.

### Logistic regression: purchase summary
- cumulative_opens_scaled: positive strong effect, coef = 0.9183, p < 0.001. More opens increase purchase probability.  
- repeat customers: positive significant effect, coef = 0.8306, p = 0.004.  
- days_since_last_purchase_cum_scaled: positive but not significant, p = 0.159.

Conclusion: Cumulative engagement is a strong purchase predictor. Repeat status increases purchase probability. Purchase recency shows no clear effect here.

### Q6: Purchase Frequency and Email Engagement
- Significant differences in average revenue across purchase frequency groups. Email click behavior varies by frequency.  
- Higher purchase frequency correlates with higher revenue and higher engagement.  
- This is associational. Causal or temporal models required to establish causation.

### Q7: Impact of Email Engagement on Next-30-Day Orders and AOV
- Next-30-day order rate: engaged customers 1.44% vs non-engaged 0.79%. Uplift 0.65 percentage points.  
- Average order value: engaged customers £35.60 vs non-engaged £36.03. Engaged customers purchase more often but at slightly lower AOV, likely due to promotions.

## Key Findings & Conclusion

### Exploratory analysis
- Variant B yields ~0.9 percentage point higher open rate than A. Statistically significant, small magnitude.  
- Channel explains more variance than subject variant. Prioritize channel strategy.  
- Cumulative opens predict purchases and unsubscribes. Use as targeting signal with unsubscribe mitigation.  
- Repeat customers are more likely to purchase.  
- Time-of-send signals are noisy. Do not operationalize the Sunday 00:00 result.  
- Model fit is weak. Treat coefficients as directional signals, not prescriptive rules.

### Retention and cohort analysis
- Six-month churn ~14 to 15 percent across RFM segments. High-value customers show marginally higher churn.  
- Early cohorts show inflated retention due to short windows. Later cohorts lack full six-month windows and show biased low retention.  
- Fix censoring and timestamp quality before converting findings into automated campaigns. Rebuild cohorts with consistent observation windows. Consider survival analysis for time-to-churn.

## Screenshots to Include

**Python Analysis**  
![Logit regression significance](screenshots/python_Model_Significance_Order.png)  
*Figure: Logit regression results*

![RFM quintiles: new vs repeat](screenshots/python_RFM_quintiles_new%20vs.%20repeat.png)  
*Figure: RFM quintile comparison*

![Purchase and unsubscribe model summary](screenshots/python_purchase_summary.png)  
*Figure: Logistic regression summaries*

**Power BI Dashboard**  
![CRM Overview tab](screenshots/CRM_overview_tab.png)  
*Figure: CRM overview with KPIs and trends*

![Customer Risk Analysis tab](screenshots/customer_risk_analysis_tab.png)  
*Figure: Churn rate by RFM and region*

![Email Marketing performance tab](screenshots/email_marketing_performance_tab.png)  
*Figure: Email marketing KPIs and underperforming campaigns*

## Usage Instruction
1. Clone repository.  
2. Place source data in `data/` or configure the pipeline to the simulated streaming source.  
3. Run `python notebooks/prepare_data.py` to generate analysis-ready tables.  
4. Execute notebooks in `notebooks/` for Python analysis and model training.  
5. Export processed datasets to `powerbi/` and open the `.pbix` files in Power BI Desktop.  
6. For production scoring, deploy the Spring Boot scoring API in `api/` and configure dashboards to query the API endpoints.

## Future work
- Implement survival and uplift models for treatment targeting.  
- Add robust timestamp validation and right-censoring handling.  
- Add experiment power calculations and automated A/B test reporting.  
- Implement campaign-level cost and margin analysis to assess ROI on retention activities.


