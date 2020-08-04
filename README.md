# Multi-Blockchain Wallet in Python

![bitcoin-python](bitcoin-python.jpg)

Use `hd-wallet-derive` and Python to manage billions of addresses across 300+ coins and send transactions using Ethereum and Bitcoin Testnet

* `hd-wallet-derive` supports not only BIP32, BIP39, and BIP44, but also supports non-standard derivation paths for the most popular wallets out there today!

* Ethereum keys are the same format on any network, so the Ethereum keys should work with your custom networks or testnets.


<br>


## Dependencies

- PHP (version 7+) must be installed on your operating system 

- You will need to clone the [hd-wallet-derive](https://github.com/dan-da/hd-wallet-derive) tool

- [bit](https://ofek.github.io/bit/) Python Bitcoin library

- [web3.py](https://github.com/ethereum/web3.py) Python Ethereum library

Check out [BlockChain cheat sheet](Blockchain%20Cheat%20Sheet) for detail


<br>


## Project setup

- Create a project directory called `wallet` and `cd` into it

- Set up HD wallet derive using `*SETTING UP HD WALLET DERIVE*` section in [BlockChain cheat sheet](Blockchain%20Cheat%20Sheet) 


- Create a file called `wallet.py` -- this will be your universal wallet script.

<br>


## Setup constants

- In a separate file, `constants.py`, set the following constants:
  - `BTC = 'btc'`
  - `ETH = 'eth'`
  - `BTCTEST = 'btc-test'`

  In Git Bash, you can use this line `echo -e "BTC = 'btc'\nETH = 'eth'\nBTCTEST = 'btc-test'" >> constants.py`  

- In `wallet.py`, import all constants: `from constants import *`

- Use these anytime you reference these strings, both in function calls, and in setting object keys.


<br>


## Generate a Mnemonic

- Generate a new 12 word mnemonic using `hd-wallet-derive` or by using [this tool](https://iancoleman.io/bip39/).

- Set this mnemonic as an environment variable, and include the one you generated as a fallback using:
  `mnemonic = os.getenv('MNEMONIC', 'insert mnemonic here')`


<br>

## Deriving the wallet keys

- Use the `subprocess` library to call the `./derive` script from Python. Make sure to properly wait for the process

- The following flags must be passed into the shell command as variables:
  - Mnemonic (`--mnemonic`) must be set from an environment variable, or default to a test mnemonic
  - Coin (`--coin`)
  - Numderive (`--numderive`) to set number of child keys generated

- Set the `--format=json` flag, then parse the output into a JSON object using `json.loads(output)`

- Wrap all of this into one function, called `derive_wallets`

- Create an object called `coins` that derives `ETH` and `BTCTEST` wallets with this function

- You should now be able to select child accounts (and thus, private keys) by calling `coins[COINTYPE][INDEX]['privkey']`


<br>

## Linking the transaction signing libraries

Now, you can use `bit` and `web3.py` to leverage the keys you've got in the `coins` object. You will create three more functions:


<br>

- `priv_key_to_account` -- this will convert the `privkey` string in a child key to an account object
  that `bit` or `web3.py` can use to transact.
  This function needs the following parameters:

  - `coin` -- the coin type (defined in `constants.py`).
  - `priv_key` -- the `privkey` string will be passed through here.

  You will need to check the coin, then return one of the following functions based on the library:

  - For `ETH`, return `Account.privateKeyToAccount(priv_key)`
  - For `BTCTEST`, return `PrivateKeyTestnet(priv_key)`


<br>

- `create_tx` -- this will create the raw, unsigned transaction that contains all metadata needed to transact.
  This function needs the following parameters:

  - `coin` -- the coin type (defined in `constants.py`).
  - `account` -- the account object from `priv_key_to_account`.
  - `to` -- the recipient address.
  - `amount` -- the amount of the coin to send.

  You will need to check the coin, then return one of the following functions based on the library:

  - For `ETH`, return an object containing `to`, `from`, `value`, `gas`, `gasPrice`, `nonce`, and `chainID`.
    Make sure to calculate all of these values properly using `web3.py`!
  - For `BTCTEST`, return `PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTC)])`


<br>


- `send_tx` -- this will call `create_tx`, sign the transaction, then send it to the designated network.
  This function needs the following parameters:

  - `coin` -- the coin type (defined in `constants.py`).
  - `account` -- the account object from `priv_key_to_account`.
  - `to` -- the recipient address.
  - `amount` -- the amount of the coin to send.

  You may notice these are the exact same parameters as `create_tx`. `send_tx` will call `create_tx`, so it needs
  all of this information available.

  You will need to check the coin, then create a `raw_tx` object by calling `create_tx`. Then, you will need to sign
  the `raw_tx` using `bit` or `web3.py` (hint: the account objects have a sign transaction function within).

  Once you've signed the transaction, you will need to send it to the designated blockchain network.

  - For `ETH`, return `w3.eth.sendRawTransaction(signed.rawTransaction)`
  - For `BTCTEST`, return `NetworkAPI.broadcast_tx_testnet(signed)`


<br>

## Send transactions

Now, you should be able to fund these wallets using testnet faucets. Open up a new terminal window inside of `wallet`,
then run `python`. Within the Python shell, run `from wallet import *` -- you can now access the functions interactively.
You'll need to set the account with  `priv_key_to_account` and use `send_tx` to send transactions.

#### Bitcoin Testnet transaction

- Fund a `BTCTEST` address using [this testnet faucet](https://testnet-faucet.mempool.co/).

- Use a [block explorer](https://tbtc.bitaps.com/) to watch transactions on the address.

- Send a transaction to another testnet address (either one of your own, or the faucet's).


<br>


## Local PoA Ethereum transaction

- Add one of the `ETH` addresses to the pre-allocated accounts in your `networkname.json`.

- Delete the `geth` folder in each node, then re-initialize using `geth --datadir nodeX init networkname.json`.
  This will create a new chain, and will pre-fund the new account.

- [Add the following middleware](https://web3py.readthedocs.io/en/stable/middleware.html#geth-style-proof-of-authority)
  to `web3.py` to support the PoA algorithm:

```
from web3.middleware import geth_poa_middleware

w3.middleware_onion.inject(geth_poa_middleware, layer=0)
```

- Due to a bug in `web3.py`, you will need to send a transaction or two with MyCrypto first, since the
  `w3.eth.generateGasPrice()` function does not work with an empty chain. You can use one of the `ETH` address `privkey`,
  or one of the `node` keystore files.

- Send a transaction from the pre-funded address within the wallet to another, then copy the `txid` into
  MyCrypto's TX Status


<br>


## Challenge Mode

- Add support for `BTC`.

- Add support for `LTC` using the sister library, [`lit`](https://github.com/blockterms/lit).

- Add a function to track transaction status by `txid`.
