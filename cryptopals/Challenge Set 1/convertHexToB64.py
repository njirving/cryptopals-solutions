# input in hex: 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
# output in base64: SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

import codecs


def hexToBinaryString(hex):
    return codecs.encode(codecs.decode(hex, 'hex'), 'base64').decode()


def main():

    input = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

    print(hexToBinaryString(input))

if __name__ == "__main__":
    main()
