import pandas as pd
import numpy as np
import statistics as stat
import matplotlib.pyplot as plt
df = pd.read_csv('https://www.dropbox.com/scl/fi/i0nr10rvvcmcsru6js5d4/netflix_titles.csv?rlkey=gqfe9zyavpdj8iy4sxuyt8oxz&st=t39v94qx&dl=1')
df.head()


print(df['release_year'].describe())
print(np.mean(df['release_year']))
print(np.median(df['release_year']))
print(stat.mode(df['release_year']))
print(np.std(df["release_year"]))
print(np.quantile(df['release_year'], [0, 0.25, 0.5, 0.75, 1]))
q1 = np.quantile(df['release_year'], 0.25)
q3 = np.quantile(df['release_year'], 0.75)
iqr = q3-q1
print(iqr)
print(df['release_year'].max())
print(df['release_year'].min())
print(df['release_year'].max() - df['release_year'].min())
df['release_year'].hist()
plt.show()
plt.boxplot(df['release_year'])
plt.show()