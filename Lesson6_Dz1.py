# получение списка кортежей из файла
import re
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    row = f.readline()
    result_list = []
    ip_list = []
    in_method_list = []
    url_download_list = []
    exam = []

    for row in f:
        exam.append(re.split(r'[ ,"-]+', row))
        ip_list.append(re.split(r'[ ,"-]+', row)[0])
        in_method_list.append(re.split(r'[ ,"-]+', row)[3])
        url_download_list.append(re.split(r'[ ,"-]+', row)[4])

result_list = zip(ip_list, in_method_list, url_download_list)

#print(*result_list, sep='\n')

#print(*result_list, sep='\n')
with open('test.txt', 'w', encoding='utf-8') as f:
    print(*result_list, sep='\n', file=f)
    # print(row,file=f)
    # print(ip_list,file=f )
    # print(in_method_list, file=f)
    #mrint(url_download_list, file=f)
