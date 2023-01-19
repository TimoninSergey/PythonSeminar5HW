""" Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.
aaaaabbbcccc -> 5a3b4c
5a3b4c -> aaaaabbbcccc

 """

with open('encode.txt', 'w') as data:
    data.write('aaaaabbbcccddd')

with open('encode.txt', 'r') as data:
    string = data.readline()


def encoding(string):
    encoded_string = ''
    i = 0
    while (i <= len(string)-1):
        count = 1
        char = string[i]
        j = i
        while (j < len(string)-1):
            if (string[j] == string[j+1]):
                count = count + 1
                j = j + 1
            else:
                break
        encoded_string = encoded_string + str(count) + char
        i = j + 1
    return encoded_string

def decoding(encoded_string):
    decoded_string = ''
    i = 0
    j = 0
    while (i <= len(encoded_string) - 1):
        count = int(encoded_string[i])
        char = encoded_string[i+1]
        for j in range(count):
            decoded_string = decoded_string + char
            j = j + 1
        i = i + 2
    return decoded_string


with open('encode.txt', 'r') as file:
    string = file.read()

with open('decode.txt', 'w') as file:
    encoded_string = encoding(string)
    file.write(encoded_string)

print('Decoded string: \t' + string)
print('Encoded string: \t' + encoding(string))