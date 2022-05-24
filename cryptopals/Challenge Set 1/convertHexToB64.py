# input in hex: 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
# output in base64: SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t


def hexToBinaryString(hex):
    binString = ""

    l = len(hex)
    
    for x in range(0, l):
        binString+=(hex[-1-x])

    print(binString)


def main():

    input = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

    hexToBinaryString(input)

if __name__ == "__main__":
    main()
