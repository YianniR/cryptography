import sys
import binascii
import codecs
import os
import matplotlib.pyplot as plt
import itertools
from operator import xor

from tools import *

def make_key_list(key_length):
    key_list = []
    possible_characters = [hex(x) for x in range(0,256)]
    possible_keys = itertools.combinations_with_replacement(possible_characters,key_length)
    return possible_keys

def bruteforce(cipher_text,key_length):
    key_list=make_key_list(key_length)
    for key in key_list:
        char = ord(cipher_text[0])
        key_part = int(key[0],16)
        new_char = xor(char,key_part)
        #print(chr(char),'^',hex(key_part),'=',chr(new_char))
        if new_char==ord('A'):
            decrypted_msg=decrypt(cipher_text,key)
            if decrypted_msg is not None:
                with open("output.txt", "ab") as text_file:
                    outtext = ''.join(decrypted_msg)
                    text_file.write(outtext.encode("utf-8"))
                    text_file.write('\n---KEY:'.encode("utf-8"))
                    text_file.write(str(key).encode("utf-8"))
                    text_file.write('\n'.encode("utf-8"))

                    text_file.flush()

def decrypt(cipher_text,key):
    decrypted_msg = []
    for i in range(0,len(cipher_text),len(key)):
        for j in range(0,len(key)):
            try:
                char = ord(cipher_text[i+j])
                key_part = int(key[j],16)
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

hex_encrypted_msg=read_hex("secret.hex")
cipher_text = bytes_to_char(hex_encrypted_msg)
print_char_array(cipher_text)
bruteforce(cipher_text,2)
