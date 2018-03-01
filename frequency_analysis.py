import sys
import binascii
import codecs
import os
import matplotlib.pyplot as plt
import itertools

def read_hex(filename):
    with open(filename, 'rb') as f:
        hexdata = binascii.hexlify(f.read())
        return hexdata

def bytes_to_char(hex_data):
    char_array=[]
    for i in range(0,len(hex_data),2):
        num = int(hex_data[i:i+2],16)
        char_array.append(chr(num))
    return char_array

def frequency_counter(char_array):
    alphabet = list(set(char_array))
    alphabet.sort()
    frequencies = [0]*len(alphabet)
    for char in char_array:
        index = alphabet.index(char)
        frequencies[index] += 1
    return frequencies, alphabet

def split_cipher_text(cipher_text,key_length):
    cipher_list = []
    number_of_ciphers=key_length
    for i in range(0,number_of_ciphers):
        new_cipher = []
        for j in range(0, len(cipher_text), key_length):
            new_cipher.append(cipher_text[j+i])
        cipher_list.append(new_cipher)

    return cipher_list

def merge_cipher_text(cipher_list,key_length):
    merged_cipher_text = []
    for i in range(0,cipher_list):
        for j in range(0, len(cipher_list)):
            merged_cipher_text.append(cipher_list[j][i])
        cipher_list.append(new_cipher)

def shift(cipher_text,shift):
    shifted_cipher_text = []
    for char in cipher_text:
        char = ord(char)
        if char+shift < 0:
            new_char = 127 + char+shift
        else:
            new_char = char + shift
        shifted_cipher_text.append(chr(new_char))
    return shifted_cipher_text

hexdata = read_hex('secret.hex')
cipher_text = bytes_to_char(hexdata)
print(cipher_text)
shifted_text = shift(cipher_text,-17)
print(shifted_text)

cipher_list = split_cipher_text(cipher_text,2)
for text in cipher_list:
    frequencies, alphabet = frequency_counter(text)
    index = frequencies.index(max(frequencies))
    most_common_char = alphabet[index]
