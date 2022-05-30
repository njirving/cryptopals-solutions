#include <iostream>
#include <fstream>

// input in hex: 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
// output in base64: SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

std::string input = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d";


int charToInt(char c) {
    
    if(c >= '0' && c <= '9')
        return c - '0';
    if(c >= 'A' && c <= 'F')
        return c - 'A' + 10;
    if(c >= 'a' && c <= 'f')
        return c - 'a' + 10;
    
    throw std::invalid_argument("Invalid input");
}


int hexToRaw(std::string hex) {
    
}

std::string convertHexToB64(int hex) {
    
}

int main(int argc, char** argv) {
    std::cout << "test" << std::endl;
}