# Model Interpretation – Baseline Churn Model

## Approach
A logistic regression model was used as a baseline due to its interpretability.
Categorical variables were one-hot encoded and numerical variables were used directly.

Model coefficients were transformed into odds ratios to allow business-friendly interpretation.

## Key Churn Drivers
The strongest positive drivers of churn include:
- Month-to-month contracts
- Short customer tenure
- Electronic check as payment method
- Higher monthly charges

These factors significantly increase the probability of customer churn.

## Retention Signals
The strongest negative drivers of churn include:
- Long-term contracts (one-year and two-year)
- Longer tenure
- Lower monthly charges

These features are associated with increased customer retention.

## Business Interpretation
Customers with flexible contracts and higher monthly costs are more likely to churn.
Retention strategies should focus on:
- Incentivizing longer contracts
- Proactively engaging new customers
- Monitoring high-charge, short-tenure customers
