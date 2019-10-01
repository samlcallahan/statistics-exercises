import numpy as np
import pandas as pd

dice_sample = pd.DataFrame(np.random.randint(1,7,(1000000,2)))
p_doubles = (dice_sample[0] == dice_sample[1]).mean()

coins = pd.DataFrame(np.random.randint(0,2,(1000000,8)))
p_three_heads = (coins.sum(1) == 3).mean()
p_over_three = (coins.sum(1) > 3).mean()

billboards = np.random.random((1000000,2))
p_two_data_science = (billboards <= .25).prod(1).mean()

poptarts = np.random.normal(3, 1.5,(1000000,5))
p_friday = (poptarts.sum(1) <= 16).mean()

men = np.random.normal(178, 8, 1000000)
women = np.random.normal(170, 6, 1000000)
p_woman_taller = (women > men).mean()

p_fail = 1 / 250
p_fifty = (np.random.random((1000000,50)) > p_fail).prod(1).mean()
p_hundred = (np.random.random((1000000,100)) > p_fail).prod(1).mean()
p_150_failure = 1 - (np.random.random((1000000,150)) > p_fail).prod(1).mean()
p_450 = (np.random.random((1000000,450)) > p_fail).prod(1).mean()

p_3days = (np.random.random((1000000,3)) > .7).prod(1).mean()
p_week = (np.random.random((1000000,7)) <= .7).prod(1).mean()

bday_23 = np.random.randint(0,365,(1000000,23))
bday_23 = pd.DataFrame(bday_sample_23)
p_shared_23 = bday_23.apply(lambda x: len(set(x)) != len(x),axis=1).mean()
bday_20 = pd.DataFrame(np.random.randint(0,365,(1000000,20)))
p_shared_20 = bday_20.apply(lambda x: len(set(x)) != len(x),axis=1).mean()
bday_40 = pd.DataFrame(np.random.randint(0,365,(1000000,40)))
p_shared_40 = bday_40.apply(lambda x: len(set(x)) != len(x),axis=1).mean()