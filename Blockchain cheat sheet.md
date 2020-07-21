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


* `Digital Signature`: Use cryptography to prove things stay the same

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


* Download a stable `Geth & Tools` Release on this [site](https://geth.ethereum.org/downloads/) and save on local drive

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
# Enter your public key for your Koven Ether wallet

#7
# Press Enter to skip to chain/network ID

#8
# Enter a number that you can remember
```

<br>

Then type the followings to create 2 nodes

```
#1
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
# but you need to create at least two nodes in your computer
# to create a blockchain

./geth account new --datadir node2


#10
# Initialize and tell the nodes to use the genesis block
./geth init puppernet.json --datadir node1
./geth init puppernet.json --datadir node2

```

<br>


Then type the followings to start the Blockchain

```
#1
# cd to the Blockchain_Tools dir

#2
# Launch the first node into mining mode
# In the event that your enode address ends in an IP address
# that is not the localhost (127.0.0.1), you may add the
# --rpcaddr 127.0.0.1 flag in order to force it to do so

# The --mine flag tells the node to mine new blocks
# The --minerthreads flag tells geth how many CPU threads
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

./geth --datadir node2 --port 30304 --rpc --bootnodes "enode://CopyFromFirstNode"


# Windows

./geth --datadir node2 --port 30304 --rpc --bootnodes "enode://CopyFromFirstNode" --ipcdisable

```

<br>


**If you need to start over without destroying the accounts, run the following command to clear the chain data**

```
rm -Rf node1/geth node2/geth
```

* The enodeid is the only aspect that will change