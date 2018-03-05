from tools import *

cipher_text = "Zac xhjk hd zac glqklqsxlzl ugl rxtbomgugyrew zh rklr unrihkkl ml mcgvfoge og mxwcx mm mkyjx qznbkgry. Tlumfkk dagazbmt hd zac glqklqsxlzl gy mm ynnvhpz mfk ecgkloge vkmixqy, mfk eyzmcx isximyx fgl lum yrpyel zkxl kfnntqolcj. Xtowctvc yamcl rntr ymsjxlzl bkygtx y inpxbaaess uyyxb ug rnx yylcylkkgr ggb alc om ru zsowc zacok syx ml mgsx, yzmctmgug, ytw pklmakakl"

cipher_text = conditioning(cipher_text)
print(cipher_text)
frequencies, alphabet = frequency_counter(cipher_text)
sorted_alphabet = [x for y, x in sorted(zip(frequencies, alphabet),reverse=True)]
most_common_char = sorted_alphabet[0]

y_pos = np.arange(len(alphabet))
plt.bar(y_pos, frequencies, align='center', alpha=0.5)
plt.xticks(y_pos, alphabet)
plt.ylabel('Frequency')
plt.xlabel('Letter')
plt.title('Frequency Analysis')
plt.show()

y_pos = np.arange(len(alphabet))
plt.bar(y_pos, sorted(frequencies,reverse=True), align='center', alpha=0.5)
plt.xticks(y_pos, sorted_alphabet)
plt.ylabel('Frequency')
plt.xlabel('Letter')
plt.title('Frequency Analysis')
plt.show()

key_size = 3
cipher_list = split_cipher_text(cipher_text,key_size)
shifted_cipher_list = []

for text in cipher_list:
    frequencies, alphabet = frequency_counter(text)

    sorted_alphabet = [x for y, x in sorted(zip(frequencies, alphabet),reverse=True)]
    if(cipher_list.index(text)==1):
        most_common_char = sorted_alphabet[0]
        shift_amount = find_shift('s',most_common_char)
        print(shift_amount)
        shifted_cipher_text = shift(text,shift_amount)
        shifted_cipher_list.append(shifted_cipher_text)
    else:
        most_common_char = sorted_alphabet[0]
        shift_amount = find_shift('e',most_common_char)
        print(shift_amount)
        shifted_cipher_text = shift(text,shift_amount)
        shifted_cipher_list.append(shifted_cipher_text)

decoded_cipher_text = merge_cipher_text(shifted_cipher_list,key_size)
print(''.join(decoded_cipher_text))
