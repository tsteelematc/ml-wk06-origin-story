import pandas as pd

# load your CSV
df = pd.read_csv("animals.csv")

# split mm:ss into minutes + seconds
df["minutes"] = df["race_time"].str.split(":").str[0].astype(int)
df["seconds"] = df["race_time"].str.split(":").str[1].astype(int)

# convert to total seconds
df["total_seconds"] = df["minutes"] * 60 + df["seconds"]

# group and average
g = (
    df.groupby(["meat_eater", "legs", "tail"])
      .agg(
          animal_count=("animal", "count"),
          avg_seconds=("total_seconds", "mean")
      )
      .reset_index()
)

# convert avg seconds back to mm:ss
g["avg_minutes"] = (g["avg_seconds"] // 60).astype(int)
g["avg_secs"] = (g["avg_seconds"] % 60).astype(int)

g["avg_race_time_mmss"] = (
    g["avg_minutes"].astype(str).str.zfill(2)
    + ":" +
    g["avg_secs"].astype(str).str.zfill(2)
)

# final cleaned output
result = g[["meat_eater", "legs", "tail", "animal_count", "avg_race_time_mmss"]]

print(result)
