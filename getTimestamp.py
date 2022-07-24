from datetime import datetime, timedelta, time

# Ribbon Weekly Options expire at 8am UTC every Friday
# Settlement prices use Chainlink price feeds

########## ETH Covered Call Vault ##########
# Contract Address: 0x25751853Eab4D0eB3652B5eB6ecB102A2789644B
# Contract Creation Datetime: 2021-09-11 01:54:21 UTC
eth_c_creation_date = datetime(2021, 9, 11)
current_date = datetime.utcnow()
eth_c_date_range = []
timestamp_arr = []

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

# Build array of every Friday at 8am UTC from Vault creation date to current date and convert to timestamps
eth_c_date_new = eth_c_start_range

while eth_c_date_new <= current_date:
    eth_c_date_range.append(eth_c_date_new.strftime('%Y-%m-%d %H:%M:%S'))    
    eth_c_date_new = eth_c_date_new + timedelta(days=7)
    
for i in range(len(eth_c_date_range)):
    element = datetime.strptime(eth_c_date_range[i],'%Y-%m-%d %H:%M:%S')
    timestamp = datetime.timestamp(element)
    timestamp_arr.append(timestamp)

# Convert str to int
timestamp_arr = [int(x) for x in timestamp_arr]
print(timestamp_arr)