# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def rle_encode(data_file):
    encoding_line = ""
    i = 0
    while i < len(data_file):
        count = 1
        while i + 1 < len(data_file) and data_file[i] == data_file[i + 1]:
            count = count + 1
            i += 1
        encoding_line += str(count) + data_file[i]
        i += 1
    return encoding_line
 
with open ('parameters.txt', 'w') as data:
    data.write('QQQ5555QQAWWWWWWWWWWEEEEEEEEEEEERRRRRRRRRRRRRRRTTTTTTTTTYYYYYYYYYYYY')
with open ('parameters.txt', 'r') as data:
    new_data = rle_encode(data.readline())
with open ('encode_parameters.txt', 'w') as data:
    print(new_data, file=data)