import pandas as pd
import matplotlib.pyplot as plt

# Load WETH-C Ribbon Vault Data
df_options = pd.read_csv('WETH-C_Options_Data.csv')

# plot
fig, ax = plt.subplots()
ax.plot(df_options['Expiry'], df_options['Strike Price'], label='Strike Price', color='C0', marker='o')
ax.plot(df_options['Expiry'], df_options['Historical $Price/Eth Nearest Expiry'], label='Price at Expiry', color='C1', marker='o')
plt.xticks(['17-Sep-21', '1-Oct-21', '15-Oct-21', '29-Oct-21', '12-Nov-21', '26-Nov-21', '10-Dec-21', '24-Dec-21', '7-Jan-22', '21-Jan-22', '4-Feb-22', '18-Feb-22', '4-Mar-22', '18-Mar-22', '1-Apr-22', '15-Apr-22', '29-Apr-22', '13-May-22', '27-May-22', '10-Jun-22', '24-Jun-22', '8-Jul-22'], rotation=20)
ax.set(xlabel='Date', ylabel='Ethereum Price (USD)', title='ETH Call RibbonThetaVault - Price Comparison')
fig.autofmt_xdate()
ax.legend()
ax.grid()
manager = plt.get_current_fig_manager()
manager.resize(*manager.window.maxsize())
plt.show()
fig.savefig('Figures/PriceComparison_fig.png')