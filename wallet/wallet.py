from constants import BTC, BTCTEST, ETH
import os
import subprocess
import json
from pprint import pprint
from dotenv import load_dotenv

from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_account import Account

from pathlib import Path
from getpass import getpass

from bit import PrivateKeyTestnet
from bit.network import NetworkAPI


mnemonic = os.getenv('MNEMONIC', 'genuine leaf unique toilet cement pupil amateur clever fall shoot shield wrestle syrup forget grass')

# Windows
def derive_wallets(mnemonic=mnemonic, coin=BTC, depth=3):
    command = f'php derive -g --mnemonic="{mnemonic}" --coin={coin} --numderive={depth} --cols=path,address,privkey,pubkey --format=json'

    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    
    return json.loads(output)

coins = {BTCTEST: derive_wallets(coin=BTCTEST),
        ETH:derive_wallets(coin=ETH)}


def priv_key_to_account(coin, priv_key):
    if coin == ETH:
        return Account.privateKeyToAccount(priv_key)
    elif coin == BTCTEST:
        return PrivateKeyTestnet(priv_key)

    
def create_tx(coin, account, to, amount):
    if coin == ETH:
        gasEstimate = w3.eth.estimateGas(
        {"from": account.address, "to": to, "value": amount}
        )
        return {
            "from": account.address,
            "to": to,
            "value": amount,
            "gasPrice": w3.eth.gasPrice,
            "gas": gasEstimate,
            "nonce": w3.eth.getTransactionCount(account.address),
            "chainId": web3.eth.chainId
        }
    
    elif coin == BTCTEST:
        return PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTC)])
    
    
    
def send_tx(coin, account, to, amount):   
    if coin == ETH:
        raw_tx = create_tx(coin, account, to, amount)
        signed_tx = account.sign_transaction(raw_tx)
        return w3.eth.sendRawTransaction(signed_tx.rawTransaction).hex()

    elif coin == BTCTEST:
        raw_tx = create_tx(coin, account, to, amount)
        signed_tx = account.sign_transaction(raw_tx)
        return NetworkAPI.broadcast_tx_testnet(signed_tx)


        
# send_tx(account_one, account_two.address, 555555555555555)
        
    
btctest_send_account_priv = coins[BTCTEST][0]['privkey']
btctest_to_account_address = coins[BTCTEST][1]['address']

from bit import wif_to_key
key1 = wif_to_key(btctest_send_account_priv)
key1.get_balance("btc")


send_tx(BTCTEST, priv_key_to_account(BTCTEST, btctest_send_account_priv), btctest_to_account_address, 0.0003)



eth_send_account = coins[ETH][0]['privkey']
eth_to_account = coins[ETH][1]['address']


