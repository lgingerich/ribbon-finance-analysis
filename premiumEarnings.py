import pandas as pd
import matplotlib.pyplot as plt

# Load WETH-C Ribbon Vault Data
df_options = pd.read_csv('WETH-C_Options_Data.csv')

# Add column to dataframe to store premium earnings data
df_options['Premium Earnings (%)'] = [0.00] * len(df_options['Option'])

# Calculate premium earnings data
for i in range(len(df_options)):
    base = df_options.iloc[i]['Number of Contracts Sold (ETH)']
    premium = df_options.iloc[i]['Premium (ETH)']
    total = base + premium
    percent_change = ((total - base)/base) * 100
    df_options.at[i,'Premium Earnings (%)'] = percent_change
    
average_earning = df_options['Premium Earnings (%)'].mean()
print('Average Premium Earnings =', average_earning, '%')

# plot
fig, ax = plt.subplots()
ax.plot(df_options['Expiry'], df_options['Premium Earnings (%)'], color='C0', marker='o')
ax.set(xlabel='Date', ylabel='Week-over-Week Earnings (% ETH Change)', title='ETH Call RibbonThetaVault - Premium Earnings')
plt.xticks(['17-Sep-21', '1-Oct-21', '15-Oct-21', '29-Oct-21', '12-Nov-21', '26-Nov-21', '10-Dec-21', '24-Dec-21', '7-Jan-22', '21-Jan-22', '4-Feb-22', '18-Feb-22', '4-Mar-22', '18-Mar-22', '1-Apr-22', '15-Apr-22', '29-Apr-22', '13-May-22', '27-May-22', '10-Jun-22', '24-Jun-22', '8-Jul-22'], rotation=20)
fig.autofmt_xdate()
ax.grid()
manager = plt.get_current_fig_manager()
manager.resize(*manager.window.maxsize())
plt.show()
fig.savefig('Figures/PremiumEarnings_fig.png')