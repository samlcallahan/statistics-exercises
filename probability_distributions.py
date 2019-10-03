from scipy import stats
import seaborn as sns
import numpy as np
import pandas as pd
from env import user, host, password

cars = stats.poisson(2)
sns.distplot(cars.rvs(10000))
p_no_cars = cars.cdf(0)
p_at_least_3 = cars.sf(2)
p_at_least_1 = cars.sf(0)

cars_x = np.random.poisson(2,1000000)
cars_x.value_counts()
p_no_cars_x = (cars_x == 0).mean()
p_at_least_3_x = (cars_x >= 3).mean()
p_at_least_1_x = (cars_x >= 1).mean()

grades = stats.norm(3, .3)
top_5 = grades.isf(.05)
third_dec_top = grades.isf(.7)
third_dec_bot = grades.ppf(.2)

grades_x = .3 * np.random.randn(1000000) + 3
top_5_x = np.percentile(grades_x, 95)
third_dec_top_x = np.percentile(grades_x,30)
third_dec_bot_x = np.percentile(grades_x,20)

clicks = stats.binom(4326, .02)
at_least_97 = clicks.sf(96)

clicks_x = np.random.binomial(4326, .02, 1000000)
at_least_97_x = (clicks_x >= 97).mean()

in_first_60 = stats.binom(60, .01).sf(0)

in_first_60_x = (np.random.binomial(60, .01, 1000000) >= 1).mean()

n_visitors = round(.9 * 22 * 3)
clean_up = stats.binom(n_visitors, .03)
p_day_clean = clean_up.sf(0)
p_2_unclean = clean_up.cdf(0) ** 2
p_week_unclean = clean_up.cdf(0) ** 5

clean_up_x = np.random.binomial(n_visitors, .03, 1000000)
p_day_clean_x = (clean_up_x >= 1).mean()
clean_up_x_2 = np.random.binomial(n_visitors, .03, 1000000)
p_2_unclean_x = ((clean_up_x == 0) * (clean_up_x_2 == 0)).mean()
clean_up_x_4 = np.random.binomial(n_visitors, .03, 1000000)
clean_up_x_3 = np.random.binomial(n_visitors, .03, 1000000)
clean_up_x_5 = np.random.binomial(n_visitors, .03, 1000000)
p_week_unclean_x = ((clean_up_x == 0) * (clean_up_x_2 == 0) * (clean_up_x_3 == 0) * (clean_up_x_4 == 0) * (clean_up_x_5 == 0)).mean()

starting_line = stats.norm(15, 3)
max_people = (60 - 15 - 10) // 2
p_15_min_left = starting_line.cdf(max_people)

starting_line_x = 3 * np.random.randn(1000000) + 15
p_15_min_left_x = (starting_line_x <= max_people).mean()

def get_db_url(username, hostname, password, db_name):
    return f'mysql+pymysql://{username}:{password}@{hostname}/{db_name}'

query = '''
    select * from salaries
    where to_date like '9999%%';
'''

url = get_db_url(user,host,password,'employees')

salaries = pd.read_sql(query,url)
mean = salaries['salary'].mean()
std = salaries['salary'].std
salary_dist = stats.norm(mean,std)
p_under_60k = salary_dist.cdf(60_000)
p_over_95k = salary_dist.sf(95_000)
p_between_65k_and_80k = salary_dist.cdf(80_000) - salary_dist.cdf(65_000)
top_5_percent = salary_dist.isf(.05)

p_under_60k_x = (salaries['salary'] < 60_000).mean()
p_over_95k_x = (salaries['salary'] >= 95_000).mean()
p_between_65k_and_80k_x = ((salaries['salary'] <= 80_000) & (salaries['salary'] > 65_000)).mean()
top_5_percent_x = np.percentile(salaries['salary'], 95)

test_change