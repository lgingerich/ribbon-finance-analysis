from dotenv import load_dotenv
import os
from web3 import Web3


### IN WORK ###
# Call DegenFetcher.sol to binary search for asset prices at a desired timestamp. Chainlink price feed roundID's make it difficult to easily query historical price data
# https://github.com/andyszy/DegenFetcher



load_dotenv()
infura_api = os.environ["infura_api_mainnet"]

web3 = Web3(Web3.HTTPProvider(infura_api))
address = '0xD32Fb8BF0DecC9A80968E480694Fa60e3E91895C' # DegenFetcher.sol
abi = '[{"inputs":[{"internalType":"contract AggregatorV2V3Interface","name":"feed","type":"address"},{"internalType":"uint256","name":"targetTime","type":"uint256"},{"internalType":"uint80","name":"lhRound","type":"uint80"},{"internalType":"uint256","name":"lhTime","type":"uint256"},{"internalType":"uint80","name":"rhRound","type":"uint80"},{"internalType":"uint256","name":"rhTime","type":"uint256"}],"name":"binarySearchForTimestamp","outputs":[{"internalType":"uint80","name":"targetRound","type":"uint80"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract AggregatorV2V3Interface","name":"feed","type":"address"},{"internalType":"uint256","name":"fromTimestamp","type":"uint256"},{"internalType":"uint80","name":"daysToFetch","type":"uint80"},{"internalType":"uint256","name":"dataPointsToFetchPerDay","type":"uint256"}],"name":"fetchPriceData","outputs":[{"internalType":"int32[]","name":"","type":"int32[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"feedAddress","type":"address"},{"internalType":"uint256","name":"fromTimestamp","type":"uint256"},{"internalType":"uint80","name":"daysToFetch","type":"uint80"},{"internalType":"uint256","name":"dataPointsToFetchPerDay","type":"uint256"}],"name":"fetchPriceDataForFeed","outputs":[{"internalType":"int32[]","name":"","type":"int32[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract AggregatorV2V3Interface","name":"feed","type":"address"},{"internalType":"uint256","name":"targetTime","type":"uint256"}],"name":"getPhaseForTimestamp","outputs":[{"internalType":"uint80","name":"","type":"uint80"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint80","name":"","type":"uint80"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract AggregatorV2V3Interface","name":"feed","type":"address"},{"internalType":"uint256","name":"fromTime","type":"uint256"},{"internalType":"uint80","name":"daysToFetch","type":"uint80"}],"name":"guessSearchRoundsForTimestamp","outputs":[{"internalType":"uint80","name":"firstRoundToSearch","type":"uint80"},{"internalType":"uint80","name":"numRoundsToSearch","type":"uint80"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract AggregatorV2V3Interface","name":"feed","type":"address"},{"internalType":"uint256","name":"fromTimestamp","type":"uint256"},{"internalType":"uint80","name":"daysToFetch","type":"uint80"},{"internalType":"uint256","name":"dataPointsToFetchPerDay","type":"uint256"}],"name":"roundIdsToSearch","outputs":[{"internalType":"uint80[]","name":"","type":"uint80[]"}],"stateMutability":"view","type":"function"}]'
contract = web3.eth.contract(address=address, abi=abi)

timestamp_arr = [1631880000, 1632484800, 1633089600, 1633694400, 1634299200, 1634904000, 1635508800, 1636113600, 1636722000, 1637326800, 1637931600, 1638536400, 1639141200, 1639746000, 1640350800, 1640955600, 1641560400, 1642165200, 1642770000, 1643374800, 1643979600, 1644584400, 1645189200, 1645794000, 1646398800, 1647003600, 1647604800, 1648209600, 1648814400, 1649419200, 1650024000, 1650628800, 1651233600, 1651838400, 1652443200, 1653048000, 1653652800, 1654257600, 1654862400, 1655467200, 1656072000, 1656676800, 1657281600, 1657886400, 1658491200]
prices_arr = []

for i in range(len(timestamp_arr)):
    prices = contract.functions.fetchPriceData('0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419', timestamp_arr[i], 1, 1).call()
    prices_arr.append(prices)

print(prices_arr)



# prices = contract.functions.guessSearchRoundsForTimestamp('0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419', 1631879999, 1).call()
# print(prices[0])

# for i in range(len(timestamp_arr)):

#     while timestamp_arr[i] >= prices[0]:
        
        
# Chainlink rounds don't occur every timestamp. Need to find the round closest to, but before the vault expiration date timestamp