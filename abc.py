import pandas as pd
import random
from streamz import Stream
from streamz.dataframe import DataFrame
stream = Stream()
while True:
    example = pd.DataFrame([{'name': random.uniform(1,10), 'amount': random.uniform(10,20)}])
    sdf = DataFrame(stream, example=example)
    print(sdf)
#sdf[sdf.name == 'Alice'].amount.sum()