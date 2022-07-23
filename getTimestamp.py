from datetime import datetime, date, timedelta, time
import pandas as pd
import ciso8601

### IN WORK ###
# Get timestamp's for all applicable option vault expiration dates


# Ribbon Weekly Options expire at 8am UTC every Friday
# Settlement prices use Chainlink price feeds

########## ETH Covered Call Vault ##########
# Contract Address: 0x25751853Eab4D0eB3652B5eB6ecB102A2789644B
# Contract Creation Datetime: 2021-09-11 01:54:21 UTC
eth_c_creation_date = datetime(2021, 9, 11)

# Start date range on the first Friday after contract deployment
# Monday = 0, Sunday = 6
if eth_c_creation_date.weekday() == 0:
    eth_c_start_range = eth_c_creation_date + timedelta(days=4)
elif eth_c_creation_date.weekday() == 1:
    eth_c_start_range = eth_c_creation_date + timedelta(days=3)
elif eth_c_creation_date.weekday() == 2:
    eth_c_start_range = eth_c_creation_date + timedelta(days=2)
elif eth_c_creation_date.weekday() == 3:
    eth_c_start_range = eth_c_creation_date + timedelta(days=1)
elif eth_c_creation_date.weekday() == 4:
    eth_c_start_range = eth_c_creation_date + timedelta(days=0)
elif eth_c_creation_date.weekday() == 5:
    eth_c_start_range = eth_c_creation_date + timedelta(days=6)
elif eth_c_creation_date.weekday() == 6:
    eth_c_start_range = eth_c_creation_date + timedelta(days=5)

eth_c_start_range = datetime.combine(eth_c_start_range, time(8, 0, 0))
print('Start Range = ', eth_c_start_range)
current_date = datetime.utcnow()


# Option 1: Manually build datetime array and convert to timestamp
eth_c_date_range = [eth_c_start_range.strftime('%Y-%m-%d %H:%M:%S')]
print('Init Date Range = ', eth_c_date_range)
eth_c_date_new = eth_c_creation_date

step = eth_c_start_range

if eth_c_date_new <= current_date:
    
    eth_c_date_new = step + timedelta(days=7)
    # eth_c_date_new = eth_c_date_new.strftime('%Y-%m-%d %H:%M:%S')
    # print(eth_c_date_new.type())
    # print(type(eth_c_date_new))
    # eth_c_date_range.strftime('%Y-%m-%d %H:%M:%S')
    # print(eth_c_date_new)
    eth_c_date_range.append(eth_c_date_new.strftime('%Y-%m-%d %H:%M:%S'))
    step = step 
    
    print('Date New = ', eth_c_date_new)
    print('Current Date = ', current_date)

print(eth_c_date_range)





# Option 2: Use pd.date_range to build datetime -> Causes problems with type when converting to timestamps
eth_c_date_range = pd.date_range(start=eth_c_start_range, end=current_date, freq='W')
print(eth_c_date_range)

# ts = ciso8601.parse_datetime(new)
# print(ts)



# new = eth_c_date_range.strftime('%Y-%m-%d %H:%M:%S')
# print(new)
# # print(eth_c_date_range.index.strftime('%Y-%m-%d %H:%M:%S'))

# new = pd.Series(eth_c_date_range.format())
# print(new)
# new = new.to_string()

# eth_c_date_range = datetime.strptime(new, '%Y-%m-%d %H:%M:%S').replace(tzinfo=datetime.timezone.utc).timestamp()
# print(eth_c_date_range)