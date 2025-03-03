import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash, owner):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash
        self.owner = owner

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, "0", int(time.time()), "Genesis Block", self.calculate_hash(0, "0", int(time.time()), "Genesis Block"), "ervin210")
        self.chain.append(genesis_block)

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data, owner):
        previous_block = self.get_latest_block()
        new_block = Block(len(self.chain), previous_block.hash, int(time.time()), data, self.calculate_hash(len(self.chain), previous_block.hash, int(time.time()), data), owner)
        self.chain.append(new_block)

    def calculate_hash(self, index, previous_hash, timestamp, data):
        return hashlib.sha256(f"{index}{previous_hash}{timestamp}{data}".encode()).hexdigest()

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != self.calculate_hash(current_block.index, current_block.previous_hash, current_block.timestamp, current_block.data):
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True
import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash, owner):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash
        self.owner = owner

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, "0", int(time.time()), "Genesis Block", self.calculate_hash(0, "0", int(time.time()), "Genesis Block"), "ervin210")
        self.chain.append(genesis_block)

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data, owner):
        previous_block = self.get_latest_block()
        new_block = Block(len(self.chain), previous_block.hash, int(time.time()), data, self.calculate_hash(len(self.chain), previous_hash, int(time.time()), data), owner)
        self.chain.append(new_block)

    def calculate_hash(self, index, previous_hash, timestamp, data):
        return hashlib.sha256(f"{index}{previous_hash}{timestamp}{data}".encode()).hexdigest()

    def is_chain_valid(self
