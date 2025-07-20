import pandas as pd
import numpy as np
df = pd.DataFrame({"column 1": np.linspace(0,3,5), "column 2" : np.array([3, 4, np.nan, np.nan, np.nan])})
df.to_json("written.json")