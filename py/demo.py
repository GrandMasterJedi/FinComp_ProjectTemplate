
# Demo plot

from funcs import *
import pandas as pd
import matplotlib.pyplot as plt


df1 = pd.read_csv("data/example_prices.csv", index_col=0)

ret1 = cont_return(df1)
Sigma1 = ret1.cov()
mu1 = np.mean(ret1)
vol1 = np.std(ret1)
var1 = np.var(ret1)

# Create Mean-Volatility plot
retA = 253*mu1
volA = (253**0.5)*vol1
plt.scatter(volA, retA)
plt.xlabel('Risk (Annual)')
plt.ylabel('Expected Returns (Annual)')
plt.grid()
for label, x, y in zip(ret1.columns, volA, retA):
    plt.annotate(
        label,
        xy = (x, y), xytext = (20, -20),
        textcoords = 'offset points', ha = 'right', va = 'bottom',
        bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
        arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))

plt.savefig('img/RiskReturn_example.png', format='png')
print("Figure successfully created!")
