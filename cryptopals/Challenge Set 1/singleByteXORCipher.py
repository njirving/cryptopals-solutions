import codecs
import string
import sys

#1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736

freqDict = {
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610,
    'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513,
    'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 'u': 0.0225134,
    'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
}

def singleCharXOR(h, c):
    return (bytes((a ^ c) for a in codecs.decode(h, 'hex'))).decode().lower()

def getScore(s):
    score = 0
    for c in s:
        score += freqDict.get(c,0)
    return score

def cipherSolve(h):
    out = ""
    maxScore = 0
    char = 0
    for i in range(0,128):
        try:
            st = singleCharXOR(h, i)
            score = getScore(st)
            if score > maxScore:
                out = st
                maxScore = score
                char = chr(i)
        except:
            pass
    return out, char

def main():
    if len(sys.argv) == 2:
        h = sys.argv[1]
        print(cipherSolve(h))
    else:
        print("Usage: singleByteXORCipher.py [hex cipher]")

if __name__ == "__main__":
    main()