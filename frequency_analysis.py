import sys
import binascii
import codecs
import os
import matplotlib.pyplot as plt
import itertools
import re
import numpy as np
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
            try:
                new_cipher.append(cipher_text[j+i])
            except IndexError:
                continue
        cipher_list.append(new_cipher)
    return cipher_list

def merge_cipher_text(cipher_list,key_length):
    merged_cipher_text = []
    for j in range(0, len(cipher_list[0])):
        for i in range(0,len(cipher_list)):
            try:
                merged_cipher_text.append(cipher_list[i][j])
            except IndexError:
                continue
    return merged_cipher_text

def shift(cipher_text,shift):
    shifted_cipher_text = []

    for char in cipher_text:
        diff_from_a = (ord(char) + shift) - ord('a')
        diff_from_z = (ord(char) + shift) - ord('z')
        if diff_from_a < 0:
            new_char = ord('z') + diff_from_a +1
        elif diff_from_z > 0:
            new_char = ord('a') + diff_from_z -1
        else:
            new_char = ord(char) + shift
        #print(new_char)
        shifted_cipher_text.append(chr(new_char))
    return shifted_cipher_text

def conditioning(cipher_text):
    regex = re.compile('[^a-zA-Z]')
    cipher_text = regex.sub('', cipher_text).lower()
    return cipher_text

def find_shift(original,shifted):
    shift = ord(original) - ord(shifted)
    return shift

cipher_text = "Zac xhjk hd zac glqklqsxlzl ugl rxtbomgugyrew zh rklr unrihkkl ml mcgvfoge og mxwcx mm mkyjx qznbkgry. Tlumfkk dagazbmt hd zac glqklqsxlzl gy mm ynnvhpz mfk ecgkloge vkmixqy, mfk eyzmcx isximyx fgl lum yrpyel zkxl kfnntqolcj. Xtowctvc yamcl rntr ymsjxlzl bkygtx y inpxbaaess uyyxb ug rnx yylcylkkgr ggb alc om ru zsowc zacok syx ml mgsx, yzmctmgug, ytw pklmakakl"
cipher_text = conditioning(cipher_text)
print(cipher_text)

cipher_list = split_cipher_text(cipher_text,3)
shifted_cipher_list = []
for text in cipher_list:
    frequencies, alphabet = frequency_counter(text)

    sorted_alphabet = [x for y, x in sorted(zip(frequencies, alphabet),reverse=True)]
    index = frequencies.index(max(frequencies))
    print(sorted(frequencies))
    if(cipher_list.index(text)==1):
        most_common_char = sorted_alphabet[0]
        shift_amount = find_shift('s',most_common_char)
        shifted_cipher_text = shift(text,shift_amount)
        shifted_cipher_list.append(shifted_cipher_text)
    else:
        most_common_char = sorted_alphabet[0]
        shift_amount = find_shift('e',most_common_char)
        shifted_cipher_text = shift(text,shift_amount)
        shifted_cipher_list.append(shifted_cipher_text)

decoded_cipher_text = merge_cipher_text(shifted_cipher_list,3)
print(''.join(decoded_cipher_text))
