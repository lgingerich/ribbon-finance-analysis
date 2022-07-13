import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker

# Load WETH-C Ribbon Vault Data
df_options = pd.read_csv('WETH-C_Options_Data.csv')
df_options['Deposits_USD'] = df_options['Number of Contracts Sold (ETH)'] * df_options['Historical $Price/Eth Nearest Expiry']

# plot Vault Deposits (ETH)
fig, ax = plt.subplots()
ln1 = ax.plot(df_options['Expiry'], df_options['Number of Contracts Sold (ETH)'], label='Vault Deposits (ETH)', color='C0', marker='o')
ax.set_xlabel('Date')
ax.set_ylabel('Deposits (ETH)')
ax.set_title('ETH Call RibbonThetaVault - Vault Deposits')
            
# plot Vault Deposits (USD)
ax2 = ax.twinx()
ln2 = ax2.plot(df_options['Expiry'], df_options['Deposits_USD'], label='Vault Deposits (USD)', color='C1', marker='o')
ax2.set_ylabel('Deposits (USD)')
plt.xticks(['17-Sep-21', '1-Oct-21', '15-Oct-21', '29-Oct-21', '12-Nov-21', '26-Nov-21', '10-Dec-21', '24-Dec-21', '7-Jan-22', '21-Jan-22', '4-Feb-22', '18-Feb-22', '4-Mar-22', '18-Mar-22', '1-Apr-22', '15-Apr-22', '29-Apr-22', '13-May-22', '27-May-22', '10-Jun-22', '24-Jun-22', '8-Jul-22'], rotation=20)
ax.get_yaxis().set_major_formatter(ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
ax2.get_yaxis().set_major_formatter(ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
fig.autofmt_xdate()
ln = ln1 + ln2
labs = [l.get_label() for l in ln]
ax.legend(ln, labs, loc=0)
ax.grid()
manager = plt.get_current_fig_manager()
manager.resize(*manager.window.maxsize())
plt.show()
fig.savefig('Figures/VaultDeposits_fig.png')