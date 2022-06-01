import codecs
import sys
import math

def repeatingKeyXOR(message, key):
    # bytes((a ^ c) for a in codecs.decode(h, 'hex')))
    encr = b''
    for i, a in enumerate(message):
       encr +=  bytes(x ^ y for x, y in (codecs.encode(bytes(a, encoding='utf-8'), 'hex'), codecs.encode(bytes(key[i % len(key)], encoding='utf-8'), 'hex'))) 
    print(encr.decode())

def main():
    print(repeatingKeyXOR("Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal", "ICE"))
    '''
    if sys.argv == 3:
        print(repeatingKeyXOR(sys.argv[1], sys.argv[2]))
    else:
        print("Usage: repeatingKeyXOR.py [message] [key]")
    '''

if __name__ == "__main__":
    main()