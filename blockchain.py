# Blockchain

import hashlib

# Block class

class Block:
    def __init__(self, data, prev_hash):
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.calc_hash()

    # Calculate Hash - sha256
    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update(self.data.encode('utf-8'))
        return sha.hexdigest()

# Blockchain class
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    # First block in the blockchain 'Genesis Block'
    def create_genesis_block(self):
        return Block("Genesis Block", "0")

    # Creates new block and add in the blockchain (aka the list)
    def add_block(self, data):
        prev_block = self.chain[-1]
        new_block = Block(data, prev_block.hash )
        self.chain.append(new_block)

# Test the Blockchain
blockchain = Blockchain()

# Add data to the Blockchain
blockchain.add_block('First block')
blockchain.add_block('Second block')
blockchain.add_block('Third block')

# Show the Blockchain
print('Blockchain:')
for block in blockchain.chain:
    print('Data:', block.data)
    print('Previous hash:', block.prev_hash)
    print('Hash:', block.hash)
    print()
