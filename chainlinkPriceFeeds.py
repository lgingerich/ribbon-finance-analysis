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


# Set up contract instance
contract = web3.eth.contract(address=address, abi=abi)
# prices = contract.functions.getPhaseForTimestamp('0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419', 1630454400).call()
prices = contract.functions.fetchPriceData('0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419', 1630454400, 5, 1).call()
print(prices)