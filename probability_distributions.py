from scipy import stats
import seaborn as sns

cars = stats.poisson(2)
sns.distplot(cars.rvs(10000))
p_no_cars = cars.cdf(0)
p_at_least_3 = cars.sf(2)
p_at_least_1 = cars.sf(0)

grades = stats.norm(3, .3)
top_5 = grades.isf(.05)
third_dec_top = grades.isf(.7)
third_dec_bot = grades.ppf(.2)

clicks = stats.binom(4326, .02)
at_least_97 = clicks.sf(97)

in_first_60 = stats.binom(60, .01).sf(0)

n_visitors = .9 * 22 * 3
clean_up = stats.binom(n_visitors, .03)
p_day_clean = clean_up.sf(0)
p_2_unclean = clean_up.cdf(0) ** 2
p_week_unclean = clean_up.cdf(0) ** 5

starting_line = stats.norm(15, 3)
max_people = (60 - 15 - 10) // 2
p_15_min_left = starting_line.cdf(max_people)