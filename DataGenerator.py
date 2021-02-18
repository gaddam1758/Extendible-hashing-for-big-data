##Dataset generator

import pandas as pd
import numpy as np
import random
import string


def DataGenerator(file_name,size):
    df = pd.DataFrame()

    ##Transaction ID
    df['TransactionID'] = range(0,size)

    ##Transaction Sale amount between 1 to 50000
    df['SaleAmount'] = np.random.random_integers(low = 1, high = 50000, size = size)

    ##Customer name 3 char string
    letters = string.ascii_letters
    x = []
    for i in range(size):
        x.append(''.join(random.choice(letters) for i in range(3)))
    df['Name'] = x

    ##category uniformly distributed between 1 to 1500
    df['Category'] = np.random.random_integers(low = 1, high = 1500, size = size)

    df.to_csv(file_name,index=False)





