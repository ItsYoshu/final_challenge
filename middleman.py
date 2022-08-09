"""YOU ARE NOT ALLOWED TO CHANGE ANY PART OF THIS CODE!!"""
'''YOU ARE NOT ALLOWED TO CHANGE ANY PART OF THIS CODE!!'''
'''YOU ARE NOT ALLOWED TO CHANGE ANY PART OF THIS CODE!!'''
'''YOU ARE NOT ALLOWED TO CHANGE ANY PART OF THIS CODE!!'''
'''YOU ARE NOT ALLOWED TO CHANGE ANY PART OF THIS CODE!!'''
'''YOU ARE NOT ALLOWED TO CHANGE ANY PART OF THIS CODE!!'''
import random
import requests

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(word_site)
words = [str(value) for value in response.content.splitlines()]


def get_random_word():
    return words[random.randint(0,10000)][2:-1]


def send_to_receiver(message):
    noise_level = 90
    strng = ""
    for bit in message:
        if random.randint(0, 100) > noise_level:
            if bit == "1":
                strng += "0"
            else:
                strng += "1"
            continue
        strng += bit
    return strng


# For converting a string to binary
def text_to_binary(message):
    l, m = [], []
    for i in message:
        l.append(ord(i))
    for i in l:
        binary = str(int(bin(i)[2:]))
        if len(binary) < 8:
            binary = "".join(["0" for _ in range(8 - len(binary))]) + binary
        m.append(binary)
    return "".join(m)


# For converting a BYTE (8 bits) into a String
def byte_to_text(byte):
    if len(byte) > 8:
        raise ValueError("Byte length is longer than 8.")
    return chr(int(byte, 2))
