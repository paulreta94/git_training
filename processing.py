import pandas as pd
df = pd.DataFrame({"column 1": [1,2], "column 2" : [3, 4]})
df.to_json("written.json")