from io import BytesIO
from unittest import TestCase

from helper import (
    bits_to_target,
    hash256,
    int_to_little_endian,
    little_endian_to_int,
)


# tag::source1[]
class Block:

    def __init__(self, version, prev_block, merkle_root, timestamp, bits, nonce):
        self.version = version
        self.prev_block = prev_block
        self.merkle_root = merkle_root
        self.timestamp = timestamp
        self.bits = bits
        self.nonce = nonce

    # end::source1[]

    @classmethod
    def parse(cls, s):
        '''Takes a byte stream and parses a block. Returns a Block object'''
        # s.read(n) will read n bytes from the stream
        # version - 4 bytes, little endian, interpret as int
        # prev_block - 32 bytes, little endian (use [::-1] to reverse)
        # merkle_root - 32 bytes, little endian (use [::-1] to reverse)
        # timestamp - 4 bytes, little endian, interpret as int
        # bits - 4 bytes
        # nonce - 4 bytes
        # initialize class
        raise NotImplementedError

    def serialize(self):
        '''Returns the 80 byte block header'''
        # version - 4 bytes, little endian
        # prev_block - 32 bytes, little endian
        # merkle_root - 32 bytes, little endian
        # timestamp - 4 bytes, little endian
        # bits - 4 bytes
        # nonce - 4 bytes
        raise NotImplementedError

    def hash(self):
        '''Returns the hash256 interpreted little endian of the block'''
        # serialize
        # hash256
        # reverse
        raise NotImplementedError

    def bip9(self):
        '''Returns whether this block is signaling readiness for BIP9'''
        # BIP9 is signalled if the top 3 bits are 001
        # remember version is 32 bytes so right shift 29 (>> 29) and see if
        # that is 001
        raise NotImplementedError

    def bip91(self):
        '''Returns whether this block is signaling readiness for BIP91'''
        # BIP91 is signalled if the 5th bit from the right is 1
        # shift 4 bits to the right and see if the last bit is 1
        raise NotImplementedError

    def bip141(self):
        '''Returns whether this block is signaling readiness for BIP141'''
        # BIP91 is signalled if the 2nd bit from the right is 1
        # shift 1 bit to the right and see if the last bit is 1
        raise NotImplementedError

    def target(self):
        '''Returns the proof-of-work target based on the bits'''
        return bits_to_target(self.bits)

    #####METODO DIFFICULTY######


    def difficulty(self):
        lowest = 0xffff * 256**(0x1d-3)
        return lowest /self.target()

        #>>> from block import Block
        #>>> Block.difficulty('093c0118')
        #890630919304.1241
        #>>> 

        
