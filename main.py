def eserom_code(input):

    if input == "10":
        return "A"
    elif input == "0111":
        return "B"
    elif input == "0101":
        return "C"
    elif input == "011":
        return "D"
    elif input == "1":
        return "E"
    elif input == "1101":
        return "F"
    elif input == "001":
        return "G"
    elif input == "1111":
        return "H"
    elif input == "11":
        return "I"
    elif input == "1000":
        return "J"
    elif input == "010":
        return "K"
    elif input == "1011":
        return "L"
    elif input == "00":
        return "M"
    elif input == "01":
        return "N"
    elif input == "000":
        return "O"
    elif input == "1001":
        return "P"
    elif input == "0010":
        return "Q"
    elif input == "101":
        return "R"
    elif input == "111":
        return "S"
    elif input == "0":
        return "T"
    elif input == "110":
        return "U"
    elif input == "1110":
        return "V"
    elif input == "100":
        return "W"
    elif input == "0110":
        return "X"
    elif input == "0100":
        return "Y"
    elif input == "0011":
        return "Z"
    elif input == "10000":
        return 1
    elif input == "11000":
        return 2
    elif input == "11100":
        return 3
    elif input == "11110":
        return 4
    elif input == "11111":
        return 5
    elif input == "01111":
        return 6
    elif input == "00111":
        return 7
    elif input == "00011":
        return 8
    elif input == "00001":
        return 9
    elif input == "00000":
        return 0


code = "1111 1 1011 1011 000  100 000 101 1011 011"
words = code.split("  ")
plaintext = []
for word in words:
    letters = word.split(" ")
    for letter in letters:
        plaintext.append(eserom_code(letter))
    plaintext.append(" ")
print("".join(plaintext))





