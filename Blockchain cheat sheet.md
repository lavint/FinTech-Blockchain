# Blockchain

A blockchain is a distributed "immutable" database that is not controlled by a single, central authority

* The database is synchronized across the network, with special rules in place to incentivize good actors and disincentivize bad actors

* It is immutable, which means you can only add to the database: you cannot change the history

* This provides a powerful means of creating a trusted "source of truth" in a trustless environment

* In many cases faster, more secure, and cheaper



<br>

## 5 pillars
    
1. Open

    * Anyone can access the source code and create a project from it, therefore developer access is high

    * Anyone can access the chain and participate in the ecosystem

    * Anyone can access the services the blockchain offers

2. Borderless

    * It's a network without geographical or political borders

    * Any central party does not hold control of the network

    * Since the blockchain is synchronized onto every device that helps maintain it (called nodes), it lives everywhere

    * You can use a satellite connection to connect to blockchain networks and broadcast transactions, therefore it is truly global


3. Neutral

    * The protocol does not discriminate against any user

    * Open blockchain networks are governed in a neutral fashion, with many using the blockchain itself for voting on the next network upgrades


4. Censor Resistant

    * Blockchains that are properly decentralized are highly resistant to censorship and authoritarian control

    * They are used currently around the world to avoid censorship or hyperinflation in many countries


5. Public

    * Open blockchains are separate from the state

    * It enables the separation of state and money allowing monetary freedom

    * While the current version of `Ethereum` is pseudonymous, future updates will bring a technology called "Zero-Knowledge Proofs" that will enable completely private transactions on a public network

    * This means that the balances and transaction history between accounts will be encrypted in a way that allows for verification without exposing potentially sensitive information

    * `Zcash` implements this now by default


<br>
<br>

## Common Terminology

* `Hash`: A unique one-way function that produces a digital fingerprint of data

    * You cannot reverse a hash much like you can't reverse mixing paint

    * If you were to change a single bit of the input, you would get a completely different hash, which allows data integrity

    * The most important functionality is data integrity

    * All hashes are the same length


    ```
    import hashlib

    # output sha256 hash in hexadecimal string format
    def hash(message):
        return hashlib.sha256(message).hexdigest()

    hash(b'Today is a great day')

    ```

<br>


* `Digital Signature`: A cryptographic technique used to ensure the integrity and authority of data

    * proving ownership or authenticity of data mathematically

    * If a signed message is modified, the message will be invalidated


* `Digital Wallet`: A set of keys to your funds that are on the blockchain

    * You can create, receive and send transactions

    * You can also sign messages with the digital wallet to prove ownership or authenticity of something


* `Transaction`: A signed message that authorized a movement of funds between two parties
    
    * No one can modified it once the transaction is signed off 


* `Blockchain Node`: A participant of the network that keeps a full copy of the blockchain and maintains the consensus rules of the network

    * It verifies the signature of every transaction and throws out any that do not validate

    * If you want to send a transaction, you will send it to a node (a participant in the network) to keep track of. The node then broadcast the transaction to its neighbors until a miner comes along and finalizes the transactions

    * Nodes are enforcing all of the rules of the blockchain. Thus they are a very important part of the security of the network


* `Miner/Block Producer`: A special type of node that is working to solve computations to finalize transactions

    * Miners take the pending transactions from the nodes they are connected to and put them into a block

    * Each miner races against each other to perform this process first, and the winner is rewarded by the network for its work. Then this race happens again and again for each new block in the chain.


* `Cryptography`: Use math to keep data secure

* `Encryption`: Use cryptography to keep data secret

* `PGP`: Use cryptography to email/communicate securely 

* `Data integrity`: Ensure the data stays the same

* `Data security`: Ensure the data stays secret


* `Private key`: A key that allows you to sign transactions

* `Derivation path`: The path along the tree that the key is created from, starting at the master key




<br>
<br>

## Ethereum

* It powers a huge ecosystem of decentralized applications and financial ecosystems (> $20B USD)

* You can build applications like "Smart Contracts" on top of the blockchain with Ethereum

* Every person who helps run Ethereum becomes part of the "global computer"

* Everyone shares computing power to create a platform that anyone can upload and run code on top of, allowing for a safer, immutable web, and for building powerful financial applications

* No bottlenecks in the system, since the world helps run the code

* Highly reliable systems that will run regardless of if some servers go down

* You pay the network itself to run your code instead of a single party

* In theory, you could build any application just as you would with any other general-purpose programming language

* The application can run without a central server

* The application can potentially live forever (as long as Ethereum exists)


<br>
<br>

## Data Structure

* Each block is linked to the previous by putting the last block's hash inside of it

* Once a block is accepted by the network, it takes an enormous amount of energy to "roll a transaction back" since each block from the point of that transaction forward must be mined again, which quickly becomes mathematically infeasible





<br>
<br>


# Cryptography

## Symmetric Encryption

* A single key - one key, one lock

* It's used to protect "data at rest", meaning data that is not moving across a network

* Use one key, nonce (add randomness), and encrypted message to decrypt the message back to the original text

* Security hole: The key has to be known by both parties

* It might be hard to deliver the key and nonce to the recipient securely

* Best used for storing secure data that does not need to be transferred over the internet



<br>


## Asymmetric Encryption

* Asymmetric cryptography splits up the key into a pair of keys -- a public key and a private key


* Anyone can use your public key to send you secret data, but only you can unlock the data with your private key

* You must always keep your private/secret key safe, and never ever share it

* End-to-End encryption

    * The sender encrypts data using the recipient's public key

    * Then, the recipient uses his private key to decrypt the message

    * Only the sender and receiver can decrypt the messages between them, and they do not need to share a secret key beforehand


<br>
<br>

## Digital Signatures

* A message that can be cryptographically validated for its authenticity and integrity


* Provide authenticity (ownership) and authentication (identity) at the same time


* Use the public key, message and signature hashes to verify the integrity of the message


* In combination with hashing and encryption, they can be a powerful way to ensure a message is delivered securely ,and the right message got there without modification


* A transaction is a signed message authorizing the transfer of funds, hence cannot be modified and can be verified



<br>
<br>

# Consensus Algorithms

* The math that decides what block in the chain goes next

* The purpose is to get the entire network to agree on which block gets added to the chain next

    * In a decentralized system, you cannot trust the participants in the network.

    * A decentralized system is like a database that can be written to by anyone, which means special rules must be in place to prevent the database from being 

* A good consensus algorithm makes it so expensive to cheat (rollback the chain), and you'd make more money by mining instead


<br>

Here are some popular ones:

1. `Proof of Authority`

    * Allows only specific addresses to mine/produce blocks in the network

    * A centralized and cheap algorithm mainly used to power test networks

    * Never used in production mainnet blockchains, and is only used in testnet blockchains for development and testing 

    * Fastest, great for testing and development

    * Highly centralized, least secure


<br>


2. `Proof of Work`

    * The act of converting computing power that costs real-world energy and money into a block with transactions in it

    * The block is then submitted to the network for confirmation, and the block with the most "work" put into it gets added

    * Use Mining mechanism to create new blocks

    * This is a very secure algorithm, but the most expensive in terms of resources

    * It is what Bitcoin came out with, and where the term "mining" comes from

    * Most secure, most decentralized

    * High energy/computational cost


<br>


3. `Proof of Stake`

    * "Staking" your coins means to lock them in a transaction that proves to the rest of the network that you are willing to "put your money where your mouth is" to be trusted to make blocks

    * If you cheat, you are penalized from your stake

    * Similar security as PoW without the electricity cost

    * "Nothing at stake" problem exists when the block producers have nothing to lose


<br>
<br>

# Building a Blockchain Network from scratch

* `Genesis block` contains the initial rules for the blockchain network, like consensus algorithm, pre-funded accounts, etc

* Pre-fund the account with crypto (Otherwise we will have to mine it manually which is time consuming) 

* Install [MyCrypto](https://download.mycrypto.com/) Wallet and make sure you are using `testnet` (Koven) for testing

* Get Koven Ether (No real value) on the [faucet](https://faucet.kovan.network/)


* Download a stable `Geth & Tools` Release on this [site](https://geth.ethereum.org/downloads/) and save in a folder called `Blockchain_Tools` on local drive

* On Gitbash, `cd` to the folder location. Then type the followings to create a Genesis Block

```
#1
./puppeth

#2
# Enter a network name

#3
# Enter 2 to configure new genesis

#4
# Enter 1 to create new genesis from scratch

#5
# Enter 1 to choose proof of work

#6
# Enter your public address from your Koven Ether wallet 
# (just so we have an address that we can access with a known private key)

#7
# Press Enter to skip to chain/network ID

#8
# Enter a number/chain ID that you can remember
```

<br>

Then type the followings to create 2 nodes

```
#1 (skip if you are still in puppeth console)
./puppeth

#2
# Enter 2 to Manage existing genesis

#3
# Enter 2 to Export genesis configurations

#4
# Press Enter to continue with the current directory
# This will export several .json files

#5
# Exit puppeth prompt by using Ctrl+C

#6
# Make sure you are in the Blockchain_Tools directory
# Create the first node's data directory

./geth account new --datadir node1

#7
# Copy the keys and addresses

#8
# Enter a password

#9
# Create the second node's data directory
# You typically would only have one node per machine
# but you need to create at least two nodes in your computer to create a blockchain

./geth account new --datadir node2

#10
# Enter a password for node2

#11
# Initialize and tell the nodes to use the genesis block

./geth init puppernet.json --datadir node1
./geth init puppernet.json --datadir node2

```

<br>


Then type the followings to start the Blockchain network

```
#1 (skip if you are already in Blockchain_Tools)
# cd to the Blockchain_Tools dir

#2
# Launch the first node into mining mode
# In the event that your enode address ends in an IP address
# that is not the localhost (127.0.0.1), you may add the
# --rpcaddr 127.0.0.1 flag in order to force it to do so

# --mine flag tells the node to mine new blocks
# --minerthreads flag tells geth how many CPU threads
# or "workers" to use during mining
# 1 means the difficulty is low


./geth --datadir node1 --mine --minerthreads 1



#3
# Scroll up in the terminal window and copy the entire enode:// address
# We will need this address to tell the second node where to find the first node


#4
# Open another Gitbash and navigate to the same directory

#5
# Launch the second node
# Enable RPC
# Change the default port
# Pass the enodeid of the first node you copied in quotes

# --rpc flag enables us to talk to our node, allowing us to use MyCrypto to transact on our chain
# --port flag enables us to change the port to 30304 which is different from the first node
# --bootnodes flag allows us to pass the network info to connect to other nodes in the blockchain


# OS

./geth --datadir node2 --port 30304 --rpc --bootnodes "enode://<Enode from Node1>"


# Windows

./geth --datadir node2 --port 30304 --rpc --bootnodes "enode://<Enode from Node1>" --ipcdisable

```

<br>


**If you need to start over without destroying the accounts, run the following command to clear the chain data**

```
rm -Rf node1/geth node2/geth
```

* The enode id is the only aspect that will change


<br>

Another way to start the Blockchain network with `unlock` flag
```
# On one Gitbash

./geth --datadir node1 --unlock "<Address from Node1 Keystore>" --mine --rpc --allow-insecure-unlock


# On another Gitbash

./geth --datadir node2 --unlock "<Address from Node2 Keystore>" --mine --port 30304 --bootnodes enode://<Enode from Node1> --ipcdisable

```


<br>

*Connect to MyCrypto (Optional)*

1. Change Network
2. Add Custom Node
3. In the `Netowrk` dropdown, scroll all the way to the bottom to select `Custom`
4. Enter the information and click `Save` (URL is `http://127.0.0.1:8545`)
5. Sign into the private Network with your private key that is associated to the prefunded account




<br>
<br>


# Making Transactions via Python Web3

* `Web3` is a library that gives us the ability to talk to Ethereum nodes in Python

```
import os
from web3 import Web3
from dotenv import load_dotenv
# from web3.middleware import geth_poa_middleware
from eth_account import Account

from pathlib import Path
from getpass import getpass

load_dotenv()

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

# For Proof of Authority only
# w3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Check block number
print(w3.eth.blockNumber)

# Get private key
private_key = os.getenv("PRIVATE_KEY")

# Create account one object from env variable
account_one = Account.from_key(private_key)

# Create account two object from keystore file
with open(Path("UTC--2020-07-24T22-21-30.645Z--b42562bc046f18f31ecf0a0126557bef3676d7e8")) as keyfile:
    encrypted_key = keyfile.read()
    private_key = w3.eth.account.decrypt(
        encrypted_key, getpass("Enter keystore password: ")
    )
    account_two = Account.from_key(private_key)

    
# Define a function to create new unsigned transactions
# We can use this to request a transaction, filling in all of the necessary parameters
# then all the user has to do is sign it

def create_raw_tx(account, recipient, amount):
    gasEstimate = w3.eth.estimateGas(
        {"from": account.address, "to": recipient, "value": amount}
    )
    return {
        "from": account.address,
        "to": recipient,
        "value": amount,
        "gasPrice": w3.eth.gasPrice,
        "gas": gasEstimate,
        "nonce": w3.eth.getTransactionCount(account.address),
    }


# Define a function to sign and send fund from one to another account
# The account parameter is an object
# The recipient parameter is an address from the object

def send_tx(account, recipient, amount):
    tx = create_raw_tx(account, recipient, amount)
    signed_tx = account.sign_transaction(tx)
    result = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print(result.hex())
    return result.hex()

receipt = send_tx(account_one, account_two.address, 555555555555555)


# Check transaction receipt
w3.eth.getTransactionReceipt(receipt)


# Check account balance
w3.eth.getBalance(account_one.address)


# Convert the hash to the correct format
Web3.toChecksumAddress("0xb42562bC046f18f31ECF0a0126557bef3676d7E8")

# Output: '0xb42562bC046f18f31ECF0a0126557bef3676D7e8'

```


<br>
<br>

# Blockchain Architecture

*Ethereum vs Bitcoin*

|Ethereum                                                |Bitcoin        |
|-----                                                   |-----          |
|designed for general computing                          |designed for complex payments on the natively core layer of the blockchain|
|needs complex and expensive smart contracts to do transaction  |supports multisig natively|
|requires more computational effort                      |requires less computational effort thus cheaper|
|computing focus                                         | payment focus|
|                                                        |supports multiple inputs and outputs in transactions|
|uses nonces to count transactions sent from an account  ||
|uses a single account system                            |uses a UTXO system  |



<br>
<br>

## Bitcoin infrastructure

* Able to send Bitcoins to multiple addresses in one transaction 
* Unlike Ethereum in which we have to write a smart contract (expensive) for transactions



* `bit` is a library that gives us the ability to connect to Bitcoin networks and manage keys in Python

* `WIF` stands for wallet import format which is a special format Bitcoin uses to designate the types of keys it generates.


```
from bit import wif_to_key

# Create a WIF object
key = wif_to_key("YOUR_TESTNET_BITCOIN_PRIVATE_KEY")


# Get balance
key.get_balance("btc")


# Get balance in USD equivalent
# Check out the documentation for supported currency conversion
key.balance_as("usd")


# Create a list of Bitcoin addresses to send BTC to 
addresses = ["TESTNET_BITCOIN_ADDRESS_1", "TESTNET_BITCOIN_ADDRESS_2"]

# Create an empty list
outputs = []

# Append a tuple with 3 specific items to a list
for address in addresses:
    outputs.append((address, 0.0001, "btc"))

# Send BTC and print transaction ID
print(key.send(outputs))


# Get the wallet's all transaction history
key.get_transactions()

# Check the wallet's unspent BTC
key.get_unspents()

# The confirmations field indicates how many blocks ago the UTXO arrived in this wallet
```

<br>

## Unspent Transaction Outputs (UTXOs)

* The mechanism that allows us to send to multiple addresses 

* UTXOs are the digital equivalent of "change" in a transaction
    * You pay $5 for a $3 worth product, you get $2 back
    * Bitcoin treats balances as sets of change that are owned by different private keys. 
    * To calculate your wallet's balance, you simply sum up all of the UTXOs that your private keys own

* New UTXOs are created when a transation is sent

* It allows you to do more complex accounting

* It treats the bitcoins as individuals and not a simple balance

* You can send to multiple addresses and have multiple outputs in 1 transaction

* You can also have multiple inputs, meaning you can spend from multiple addresses and multiple wallets at the same time

* Before you can do multi-input/output transactions, you have to sign your UTXOs with their designated private keys

* It is more poweful than Ethereum's accounting model because you can spend from multiple keys in one transaction, and construct much more complex transactions natively without smart contracts


* As long as you are spending different UTXOs in each transaction, you can send multiple transactions at the same time.

* It is impossible to spend from the same UTXOx in the same block

* If you were to spend the same UTXOs in both transactions, the first one to be mined would succeed, and the second would be invalidated.

<br>
<br>



# BIP (Bitcoin Improvement Proposal)


## Wallet

* A piece of software that manages your private keys and allows you to sign and send transactions

* "Hot" wallets tend to be live and ready to spend funds, and much easier to access.

* "Cold" wallets tend to store larger funds and are accessed less frequently, more like a vault.

* It divides into 2 parts:

1. `Key Manager`: Code that takes your mnemonic or private key and converts it to the proper blockchain address format (This is the low-level cryptographic library)

2. `Blockchain Node Connectors`: Code that connects to the live blockchain nodes that the wallet supports


<br>

## BIP39 Standard

* allows us to convert mnemonics to master keys

* Bitcoin Improvement Proposal

* Helps the alt coins network in addition to Bitcoin

* Allows people to remember a more human-friendly version of the key

* Comes up with the exact lists of 2048 words per language (English, Japanese, etc)

* Comes up with a formula that allows you to take a set of those words and generate private keys with them



BIP39 Seed is the "master seed" or "master key" that can be used to derive any of the rest of the keys information


<br>

## BIP32 Standard

* Allows us to generate a tree of keys from the master key/seed

* Allows us to generate many addresses from a single seed, without having to create new wallets constantly and having to track their private keys


* Allows us to generate a new address for the UTOXs in every transaction so we can spend them all simultaneously

* Allows easier accounting on the blockchain because each address represents a receipt

* Since there will be different addresses, people can't see our entire balance and transaction history

* Generating new addresses helps preserve privacy (Bitcoin is pseudonymous, not anonymous)

<br>

## BIP44 standard

* Allows us to use the same master key/seed for multiple coins/blockchains

* Still supports multiple addresses like BIP32

* Allows the rest of the crypto and blockchain community to be more interoperable

* The most universal wallet as of 2020

* This is also the standard that exchanges use to generate our crypto addresses and keep track of customer's balances and transactions

* All blockchains have an incentive to integrate with this universal standard

* We can manage keys from many blockchains using a single master seed


<br>
<br>

## Get master key and info via GUI
* Convert BIP39 Mnemonic phrase to addresses [here](https://iancoleman.io/bip39/)


<br>
<br>


## Get master key and info  via command line

*SETTING UP HD WALLET DERIVE*

1) Install php from [XAMPP](https://www.apachefriends.org/index.html)

2) Add `extension=php_gmp.dll` to the last line of `php.ini`

3) Add `C:\xampp\php` to system environment variable `PATH`

4) Navigate to [here](https://github.com/dan-da/hd-wallet-derive) and install `hd-wallet-derive`

    * Open bash.exe from `C:\Program Files\Git\bin\bash.exe`

    * In Bash, cd into the `hd-wallet-derive` folder

    ```
    git clone https://github.com/dan-da/hd-wallet-derive
    cd hd-wallet-derive
    php -r "readfile('https://getcomposer.org/installer');" | php
    php -d pcre.jit=0 composer.phar install
    ```


    * **Use CMD if Bash doesn't work**
    * **Make sure you have the lines below as your system PATH environment variables**

        ```
        C:\xampp\php
        C:\Program Files\Git\bin\
        C:\Program Files\Git\cmd\
        ```

    Check out this [site](https://github.com/dan-da/hd-wallet-derive) for more info on HD Wallet


<br>


5. For Windows Users, `cd` to the parent directory of `hd-wallet-derive` and do below because symlink is not supported by default

    ```
    # Open up Git-Bash as an administrator 
    export MSYS=winsymlinks:nativestrict
    ```


<br>


6. Make sure you are in the parent directory of `hd-wallet-derive` and run commands below to create symlink
    ```
    # Open up Git-Bash as an administrator 
    ln -s hd-wallet-derive/hd-wallet-derive.php derive
    ```


<br>


7. Print keys in terminal

    ```
    ./derive -g --mnemonic="INSERT HERE" --cols=path,address,privkey,pubkey
    ```

    Convert to json format
    ```
    ./derive -g --mnemonic="INSERT HERE" --cols=path,address,privkey,pubkey --format=json
    ```

 
    * -g flag tells the tool to go and run (required)

    * --mnemonic flag tells the tool which mnemonic to derive from

    * --cols flag tells the tool to print certain columns

    

<br>

6. Run commands below to import addresses using Python
    ```
    import subprocess

    # Windows
    command = 'php ..\..\derive -g --mnemonic="INSERT HERE" --cols=path,address,privkey,pubkey --format=json'

    # Others
    command = './derive -g --mnemonic="INSERT HERE" --cols=path,address,privkey,pubkey --format=json'

    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()

    print(output)

    ```

    Output to JSON instead of bit
    
    ```   
    import json
    keys = json.loads(output)

    print(keys)
    print(keys[0]['address'])
    ```



    * The `subprocess` module allows us to call other processes, such as CLI tools, from within Python

    * For Windows, instead of calling ./derive, we need to use the "dot-slash" format and call php manually
