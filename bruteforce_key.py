import sys
import binascii
import codecs
import os
import matplotlib.pyplot as plt
import itertools
from operator import xor

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

def print_char_array(char_array):
    print(''.join(char_array))

def check_result(char_array):
    result_str = ''.join(char_array);
    if result_str == "Hello World":
        return True
    else:
        return False

def make_key_list(key_length):
    key_list = []
    possible_characters = [hex(x) for x in range(0,127)]
    possible_keys = itertools.combinations_with_replacement(possible_characters,key_length)
    return possible_keys

def bruteforce(cipher_text,key_length):
    key_list=make_key_list(key_length)
    for key in key_list:
        char = ord(cipher_text[0])
        key_part = int(key[len(key)-1],16)
        new_char = xor(char,key_part)
        #print(chr(char),'^',hex(key_part),'=',chr(new_char))
        if new_char==ord('A'):
            decrypted_msg=decrypt(cipher_text,key)
            if decrypted_msg is not None:
                with open("output.txt", "ab") as text_file:
                    outtext = ''.join(decrypted_msg)
                    text_file.write(outtext.encode("utf-8"))
                    text_file.write('\n----------------------\n'.encode("utf-8"))
                    text_file.flush()


def decrypt(cipher_text,key):
    decrypted_msg = []
    for i in range(0,len(cipher_text),len(key)):
        for j in range(0,len(key)):
            try:
                char = ord(cipher_text[i+j])
                key_part = int(key[len(key)-1-j],16)
                new_char = chr(xor(char,key_part))
                #print(chr(char),'^',hex(key_part),'=',new_char)
                decrypted_msg.append(new_char)
            except IndexError:
                continue
    return decrypted_msg

def encrypt(plain_text,key):
    encrypted_msg = []
    for i in range(0,len(plain_text),len(key)):
        for j in range(0,len(key)):
            try:
                char = ord(plain_text[i+j])
                key_part = ord(key[len(key)-1-j])
                new_char = chr(xor(char,key_part))
                #print(chr(char),'^',hex(key_part),'=',new_char)
                encrypted_msg.append(new_char)
            except IndexError:
                continue
    return encrypted_msg

def cribdrag(hex_encrypted_msg,crib):
    decrypted_msg = []
    for i in range(0,len(hex_encrypted_msg),len(crib)):
        for j in range(0,len(crib)-1):
            new_char = hex_encrypted_msg[i+j] ^ ord(crib[j])
            decrypted_msg.append(new_char)
    return decrypted_msg

hex_encrypted_msg=read_hex("secret.hex")
cipher_text = bytes_to_char(hex_encrypted_msg)

print_char_array(cipher_text)

for key_length in range(1,5):
    bruteforce(cipher_text,key_length)
