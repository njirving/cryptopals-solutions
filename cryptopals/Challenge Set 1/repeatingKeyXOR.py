import codecs
import sys
import math

def repeatingKeyXOR(message, key):
    # bytes((a ^ c) for a in codecs.decode(h, 'hex')))
    encr = b''
    messageHex = str.encode(message)
    for i, a in enumerate(messageHex):
        encr += (a ^ int.from_bytes(str.encode(key[i % len(key)]), "big")).to_bytes(1,byteorder='big')
    print(encr)

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