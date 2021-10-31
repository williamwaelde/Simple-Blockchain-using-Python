# needed for using SHA256 hash algorithm
import hashlib


# object representing chain links
class Block:
    # constructor:
    # nr = transaction number /block number
    # previous_hash = hash value of previous block
    def __init__(self, nr, data, previous_hash):
        # instance of the block class
        self.nr = nr
        self.data = data
        self.previous_hash = previous_hash
        # hash of current block:
        # adding to nr the data and previous_hash
        # everything will be hashed together in unique hash value
        # using sha256 hash function with hexdigest containing only hexadecimal digits
        self.hash = hashlib.sha256((str(nr) + data + previous_hash).encode()).hexdigest()

    # improve readability
    def __str__(self):
        # format() method formats the specified value(s) and insert them inside the string's placeholder
        return '{}:::{};{}'.format(self.nr, self.hash, self.data)


# object representing blockchain
class Blockchain:
    # constructor:
    def __init__(self):
        # genesis Block is the name given to the first block a blockchain
        # block without previous block (fist chain link)
        # nr = 0
        # data = Genesis
        # pseudo hash value: '0'*64 because SHA256 is using hexdigest() with 64 characters
        genesisBlock = Block(0, 'Genesis', '0'*64)

        # list of blocks stating with genisis block
        self.blocks = [genesisBlock]

    # adding blocks to chain using information of block list
    def append(self, data):
        self.blocks.append(
            Block(
                # current number of blocks from blockList
                # first real transaction starting number 1
                len(self.blocks),
                data,
                # hash value of previous block
                # -1 because current block is lat in list and previous is last -1
                self.blocks[len(self.blocks)-1].hash
            )
        )


    # improve readability
    def __str__(self):
        res = ''
        for block in self.blocks:
            # implicit calling string method of block class
            res += '{}\n'.format(block)
            return res

# testing blockchain
bc = Blockchain()

#alice sending bob 0.002 bitcoin
bc.append('Alice sendet Bob <0.002 BTC>')

bc.append('<Fred> sendet <Jack> <0.087 BTC>')

bc.append('<Donald> sendet <Vladimir> <1.2 BTC>')

bc.append('<Max> sendet <Jessica> <0.6 BTC>')

#print blockchain
for x in range(len(bc.blocks)):
    print (bc.blocks[x])


