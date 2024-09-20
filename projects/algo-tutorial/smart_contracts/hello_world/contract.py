from algopy import ARC4Contract, String, Bytes
from algopy.arc4 import abimethod
from algopy.op import Box, concat


class HelloWorld(ARC4Contract):
    
    @abimethod
    def hello(self, name: String) -> String:
        phrase = concat(Bytes(b"Hello, "), name.bytes)
        Box.put(Bytes(b"phraseKey"), phrase)

        return "Hello, " + name
