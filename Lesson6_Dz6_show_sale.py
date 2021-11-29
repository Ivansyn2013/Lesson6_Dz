def show_sale(argv):


    with open('bacery.csv', 'r', encoding='utf-8') as f:
        if len(argv) == 1:
            for row in f:
                print(row, end='')
        elif len(argv) == 2:
            path, row_in = argv
            f.seek(0)
            price_list = [el.strip('\n') for el in f.readlines()]
            price_dict = {i + 1: val for i, val in enumerate(price_list)}
            print(*[val for key, val in price_dict.items() if key >= int(row_in)], sep='\n')

        elif len(argv) == 3:
            path, row_in, row_out = argv
            f.seek(0)
            price_list = [el.strip('\n') for el in f.readlines()]
            price_dict = {i + 1: val for i, val in enumerate(price_list)}
            print(*[val for key, val in price_dict.items() if int(row_out) >= key >= int(row_in)] , sep='\n')
        else:
            print('Неправильно заданы значения')



if __name__ == '__main__':
    import sys
    exit(show_sale(sys.argv))