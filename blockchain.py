# needed for using SHA256 hash algorithm
import hashlib


# object representing chain links
class block:
    # constructor:
    # nr = transaction number /block number
    # previous_hash = hash value of previous block
    def __init__(self, nr, data, previous_hash):
        # instance of the block class
        self.nr = nr
        self.data = data
        self.previous_hash = previous_hash
        # hash of current block:
        # ading to nr the data and previous_hash
        # everything will be hashed together in unique hash value
        # using sha256 hash function with hexdigest containing only hexadecimal digits
        self.hash = hashlib.sha256((str(nr) + data + previous_hash).encode()).hexdigest()

        # make it human readable
        def __str__(self):
            # format() method formats the specified value(s) and insert them inside the string's placeholder
            return '{}:::{};{}'.format(self.nr, self.hash, self.data)


# object representing blockchain
class blockchain:
    # constructor:
    def __init__(self):
        # genesis Block is the name given to the first block a blockchain
        # block without previous block (fist chain link)
        # nr = 0
        # data = Genesis
        # pseudo hash value: '0'*64 because SHA256 is using hexdigest() with 64 characters
        genesisBlock = block(0, 'Genesis', '0' * 64)

        # list of blocks stating with genisis block
        self.blockList = [genesisBlock]

        # adding blocks to chain using information of block list
        def append(self, data):
            self.blockList.append()
