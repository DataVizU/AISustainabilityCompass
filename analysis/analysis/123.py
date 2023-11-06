import pandas as pd

data = pd.read_csv("data/region/readiness.csv")

res = {}

for region in data["地区"].unique():
    d = data[data["地区"] == region].values[0]
    res[region] = {
        "economy": d[1],
        "government": d[2],
        "infrastructure": d[3],
        "people": d[4],
        "environment": d[5],
        "risk": d[6],
        "all": d[7],
    }

print(res)
print(str(res).replace("'", '"'))
