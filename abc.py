import pandas as pd
from streamz import Stream
import random
from streamz.dataframe import DataFrame
stream = Stream()
while True:
    example = pd.DataFrame([{'name': random.uniform(1,10), 'amount': random.uniform(10,20)}])
    sdf = DataFrame(stream, example=example)
    print(sdf)
#sdf[sdf.name == 'Alice'].amount.sum()