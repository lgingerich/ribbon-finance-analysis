import pandas as pd
import matplotlib.pyplot as plt

# Load WETH-C Ribbon Vault Data
df_options = pd.read_csv('WETH-C_Options_Data.csv')

# Add column to dataframe to store premium earnings data
df_options['Balance'] = [0.00] * len(df_options['Option'])

# Ribbon Finance Fees
# 2% annualized management fee, charged on the assets managed by the vault
#   2% APY (compounded weekly) = 1.98% APR
# 10% weekly performance fee, charged on the premiums earned
# Fees are not charged if the weekly strategy is unprofitable

# Start with balance of 1 ETH
balance = 1.00

for i in range(len(df_options)):
    # Options expired OTM -> options are worthless, vault depositors collect premium
    if df_options.iloc[i]['Strike Price'] > df_options.iloc[i]['Historical $Price/Eth Nearest Expiry']:
        weekly_management_fee = (1 - (1.98/52)/100)
        weekly_performance_fee = (1 - 10/100)
        base = df_options.iloc[i]['Number of Contracts Sold (ETH)'] * weekly_management_fee
        premium = df_options.iloc[i]['Premium (ETH)'] * weekly_performance_fee
        total = base + premium
        percent_change = ((total - base)/base)
        balance = balance * (1 + percent_change)
        df_options.at[i,'Balance'] = balance
    # Options expired ITM -> potential for losses if premium does not cover amount needed to settle
    else:
        price_delta = df_options.at[i,'Historical $Price/Eth Nearest Expiry'] - df_options.at[i,'Strike Price']
        amount_to_settle = df_options.at[i,'Number of Contracts Sold (ETH)'] * price_delta
        original_usd = df_options.at[i,'Number of Contracts Sold (ETH)'] * df_options.at[i,'Strike Price']
        final_usd = df_options.at[i,'Number of Contracts Sold (ETH)'] * df_options.at[i,'Historical $Price/Eth Nearest Expiry']
        premium_usd = df_options.iloc[i]['Premium (ETH)'] * df_options.at[i,'Historical $Price/Eth Nearest Expiry']
        diff_usd = premium_usd - amount_to_settle
        diff_eth = diff_usd / df_options.at[i,'Historical $Price/Eth Nearest Expiry']
        perc_diff_usd = diff_usd / original_usd * 100
        perc_diff_eth = diff_eth / df_options.at[i,'Number of Contracts Sold (ETH)'] * 100
        
        # Options expired ITM, but premium covered amount needed to settle
        if perc_diff_eth > 0:
            weekly_management_fee = (1 - (1.98/52)/100)
            weekly_performance_fee = (1 - 10/100)
            base = df_options.iloc[i]['Number of Contracts Sold (ETH)'] * weekly_management_fee
            premium_remaining = diff_eth * weekly_performance_fee
            total = base + premium_remaining
            percent_change = ((total - base)/base)
            balance = balance * (1 + percent_change)
            df_options.at[i,'Balance'] = balance
        # Options expired ITM, premium DID NOT cover amount needed to settle. No fees if vault is not profitable
        else:
            percent_change = perc_diff_eth
            balance = balance * (1 + percent_change)
            df_options.at[i,'Balance'] = balance


percent_earning = (df_options.iloc[-1]['Balance'] - df_options.iloc[0]['Balance'])
print('Vault Earnings =', percent_earning*100, '%')
    
# plot
fig, ax = plt.subplots()
ax.plot(df_options['Expiry'], df_options['Balance'], color='C0', marker='o')
ax.set(xlabel='Date', ylabel='Balance (ETH)', title='ETH Call RibbonThetaVault - Profitability')
plt.xticks(['17-Sep-21', '1-Oct-21', '15-Oct-21', '29-Oct-21', '12-Nov-21', '26-Nov-21', '10-Dec-21', '24-Dec-21', '7-Jan-22', '21-Jan-22', '4-Feb-22', '18-Feb-22', '4-Mar-22', '18-Mar-22', '1-Apr-22', '15-Apr-22', '29-Apr-22', '13-May-22', '27-May-22', '10-Jun-22', '24-Jun-22', '8-Jul-22'], rotation=20)
fig.autofmt_xdate()
ax.grid()
manager = plt.get_current_fig_manager()
manager.resize(*manager.window.maxsize())
plt.show()
fig.savefig('Figures/Profitability_fig.png')