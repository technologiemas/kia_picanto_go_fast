from matplotlib import pyplot as plt  # type: ignore #
import seaborn as sns  # type: ignore #
import pandas as pd  # type: ignore #
from scipy import stats  # type: ignore #

plt.rcParams['figure.dpi'] = 300

data = {80: [4.2, 4.2],
        100: [5.2, 4.9, 5.0, 4.7],
        110: [5.2, 4.9, 5.7, 5.5],
        120: [6.6, 5.8, 6.1, 6.1, 5.7],
        130: [7.8, 8.0, 7.0, 7.2, 7.0],
        140: [8.5]}

df = pd.DataFrame()
df['verbruik'] = pd.concat([pd.Series(v, name=k) for k, v in data.items()])
df['snelheid'] = pd.concat([pd.Series([k] * len(v)) for k, v in data.items()])

# ax = sns.scatterplot(data=df, x='snelheid', y='verbruik', x_jitter=.05)
sns.lmplot(data=df, x='snelheid', y='verbruik', x_jitter=.05, order=2, ci=None)

sns.set(rc={'figure.figsize': (15, 8)})

plt.title('Petrol use as a function of speed in the Kia Picanto')
plt.xlabel('Speed (km/u)')
plt.ylabel('Petrol use (L/100km)')
plt.tight_layout()


plt.show()
# plt.savefig("petrol_use_per_speed.png")

print(stats.linregress(x=df['snelheid'], y=df['verbruik']))


# stats.optimize.curve_fit()
