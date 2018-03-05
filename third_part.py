from tools import *

cipher_text = "RyUaRbTbIbSsIrLwSwBR~ObOyUyEbDxM~SdEsI~MsEbSaRuEbHyFbIbTwFdSyEtFyWxSzTxTcNsE"

cipher_text_part1 = []
for letter in cipher_text:
    if letter.islower():
        cipher_text_part1.append(letter)


cipher_text_part2 = []
for letter in cipher_text:
    if not letter.islower():
        cipher_text_part2.append(letter)

print(''.join(cipher_text_part1))
print(''.join(cipher_text_part2))

frequencies, alphabet = frequency_counter(cipher_text_part1)
sorted_alphabet = [x for y, x in sorted(zip(frequencies, alphabet),reverse=True)]
most_common_char = sorted_alphabet[0]

y_pos = np.arange(len(alphabet))
plt.bar(y_pos, frequencies, align='center', alpha=0.5)
plt.xticks(y_pos, alphabet)
plt.ylabel('Frequency')
plt.xlabel('Letter')
plt.title('Frequency Analysis')
plt.show()

frequencies, alphabet = frequency_counter(cipher_text_part1)
sorted_alphabet = [x for y, x in sorted(zip(frequencies, alphabet),reverse=True)]
most_common_char = sorted_alphabet[0]
shift_amount = find_shift('e',most_common_char)
shifted_cipher_text = shift(cipher_text_part1,shift_amount)
print(''.join(shifted_cipher_text))

frequencies, alphabet = frequency_counter(cipher_text_part2)
sorted_alphabet = [x for y, x in sorted(zip(frequencies, alphabet),reverse=True)]
most_common_char = sorted_alphabet[0]
shift_amount = find_shift('e',most_common_char)
shifted_cipher_text = shift(cipher_text_part2,shift_amount)
print(''.join(shifted_cipher_text))
