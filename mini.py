from scipy import stats


# Use a scipy statistical distribution to answer the questions below:
die_distribution = stats.randint(1, 7)

# What is the probability of rolling a 1?
p_under_1 = die_distribution.cdf(1)

# There's a 1 in 2 chance that I'll roll higher than what number?
n_1_in_2_over = die_distribution.isf(.5)

# What is the probability of rolling less than or equal to 2?
p_under_2 = die_distribution.cdf(2)

# There's a 5 in 6 chance that my roll will be less than or equal to what number?
n_5_in_6_under = die_distribution.ppf(5/6)

# There's a 1 in 2 chance that my roll will be less than or equal to what number?
n_1_in_2_under = die_distribution.ppf(.5)

# What is the probability of rolling less than or equal to 6?
p_under_6 = die_distribution.cdf(6)

# There's a 1 in 3 chance that I'll roll higher than what number?
n_1_in_3_over = die_distribution.isf(1/3)

# What is the probability of rolling higher than a 1?
p_over_1_over = die_distributionl.sf(1)

# There's a 2 in 3 chance that my roll will be less than or equal to what number?
n_2_in_3_under = die_distribution.ppf(2/3)

# There's a 2 in 3 chance that I'll roll higher than what number?
n_2_in_3_over = die_distribution.isf(2/3)

# There's a 1 in 3 chance that my roll will be less than or equal to what number?
n_1_in_3_under = die_distribution.ppf(1/3)

# There's a 1 in 6 chance that I'll roll higher than what number?
n_1_in_6_over = die_distribution.isf(1/6)