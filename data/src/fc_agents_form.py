import pandas as pd
import matplotlib.pyplot as plt

points = [3, 3, 1, 0, 3, 3, 2, 3]

df = pd.DataFrame({"points":points}, index = range(1, len(points) + 1))
df["moving_avg"] = df["points"].rolling(window=3).mean()
df["exp_avg"] = df["points"].ewm(span=3, adjust=False).mean()

print(df.round(2))
plt.plot(df.index, df["points"], marker='o', label="Очки по матчах")
plt.plot(df.index, df["moving_avg"], marker='x', label="Ковзне середнє (3 матчі)")
plt.plot(df.index, df["exp_avg"], marker='s', label="експонента")
plt.xlabel("Матч")
plt.ylabel("Очки")
plt.legend()
plt.grid(True)
plt.show()
