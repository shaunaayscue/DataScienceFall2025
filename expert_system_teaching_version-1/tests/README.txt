Test Case 1 — Premium Ultrabook
Input: ['portable', 'long_battery', 'budget_high']

Expected:
> Recommendation: premium_ultrabook
> Explanation: derived from rule 'Premium Ultrabook' (confidence 0.95)
> Why: Facts [budget_high, portable, long_battery] were satisfied
> How: This led to [recommend:premium_ultrabook]
> Fired rules: Premium Ultrabook

Test Case 2 — Gaming High End
Input: ['budget_high', 'gaming']

Expected:
> Recommendation: high_end_gaming_laptop
> Explanation: derived from rule 'High-end Gaming' (confidence 0.95)
> Why: Facts [gaming, budget_high] were satisfied
> How: This led to [recommend:high_end_gaming_laptop]
> Fired rules: High-end Gaming

Test Case 3 — Budget Ultrabook
Input: ['portable', 'budget_low', 'office_only']

Expected:
> Recommendation: budget_ultrabook
> Explanation: derived from rule 'Budget Ultrabook' (confidence 0.85)
> Why: Facts [budget_low, office_only, portable] were satisfied
> How: This led to [recommend:budget_ultrabook]
> Fired rules: Budget Ultrabook
