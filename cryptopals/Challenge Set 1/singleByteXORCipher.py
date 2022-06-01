import codecs
import sys

#1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736


freqDict = {'a':0.082, 'b':0.015, 'c':0.028, 'd':0.043, 'e':0.13, 'f':0.022, 'g':0.02, 
    'h':0.061, 'i':0.07, 'j':0.0015, 'k':0.0077, 'l':0.04, 'm':0.024, 'n':0.067, 'o':0.075, 
    'p':0.019, 'q':0.00095, 'r':0.06, 's':0.063, 't':0.091, 'u':0.028,'v':0.0098, 'w':0.021,
    'x':0.0015, 'y':0.02, 'z':0.00074 }

def singleCharXOR(h, c):
    return (bytes((a ^ c) for a in codecs.decode(h, 'hex'))).decode().lower()

def main():
    h = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    for i in range(0,255):
        print(singleCharXOR(h, i))

if __name__ == "__main__":
    main()