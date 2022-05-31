import codecs
import sys

#test values
hex = "1c0111001f010100061a024b53535009181c"
xor = "686974207468652062756c6c277320657965"

#xor function
def fixedXOR(hex, xor):
    return codecs.encode(bytes((a ^ b) for a, b in zip(codecs.decode(hex, 'hex'), codecs.decode(xor, 'hex'))), 'hex').decode()

#main block
def main():
    if len(sys.argv) == 3:
        print(fixedXOR(sys.argv[1], sys.argv[2]))
    else:
        print("Usage: fixedXOR.py [hex string] [xor string]")

if __name__ == "__main__":
    main()