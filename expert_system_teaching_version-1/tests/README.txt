Test Case 1 — Premium Ultrabook (High Confidence)
Input: ['budget_high', 'portable', 'long_battery']

Expected:
> Recommendation: premium_ultrabook
> Explanation: derived from rule 'Premium Ultrabook' (confidence 0.95)
> Why: Facts [budget_high, portable, long_battery] were satisfied
> How: This led to [recommend:premium_ultrabook]
> Fired rules: Premium Ultrabook

Test Case 2 — Gaming High End (Strong Confidence)
Input: ['budget_high', 'gaming']

Expected:
> Recommendation: high_end_gaming_laptop
> Explanation: derived from rule 'High-end Gaming' (confidence 0.95)
> Why: Facts [gaming, budget_high] were satisfied
> How: This led to [recommend:high_end_gaming_laptop]
> Fired rules: High-end Gaming

Test Case 3 — Student Light Office (Budget Ultrabook)
Input: ['budget_low', 'office_only', 'portable']

Expected:
> Recommendation: budget_ultrabook
> Explanation: derived from rule 'Budget Ultrabook' (confidence 0.85)
> Why: Facts [budget_low, office_only, portable] were satisfied
> How: This led to [recommend:budget_ultrabook]
> Fired rules: Budget Ultrabook