import numpy as np
import pandas as pd

df = pd.read_table('C://Users//jlandesman//Downloads/input.txt',header=None)

## Add difference between min and max for each row
df.apply(lambda x: (x.max() -  x.min()), axis = 1).sum()

## Find evenly divisible numbers along each row
def divide_each(inputs):
    for j in inputs:
        locations = np.where(j % inputs == 0) ## Use numpy broadcasting to identify the correct cells
        if len(locations[0]) > 1:
            start = locations[0][0]
            end = locations[0][1]
            ## Use max/ min to make sure the largest number is in the numerator
            results_calc = max(inputs[start], inputs[end]) / min(inputs[start], inputs[end])
            break
    return(results_calc)

df.apply(lambda x: divide_each(x), axis=1).sum()
