import codecs
import sys

hex = "1c0111001f010100061a024b53535009181c"
xor = "686974207468652062756c6c277320657965"

def fixedXOR(hex, xor):
    return codecs.encode(bytes((a ^ b) for a, b in zip(codecs.decode(hex, 'hex'), codecs.decode(xor, 'hex'))), 'hex').decode()

def main():
    if len(sys.argv) == 3:
        fixedXOR(sys.argv[1], sys.argv[2])
    else:
        print("Usage: fixedXOR.py [hex string] [xor string]")

if __name__ == "__main__":
    main()