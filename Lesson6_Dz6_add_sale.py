def add_sale(argv):
    '''
    :param argv: int price
    :return: write in bacery.csv
    '''

    program, args = argv


    with open('bacery.csv', 'a+', encoding='utf-8') as f:
        f.write(args + '\n')
        f.seek(0)
        price_list = [el.strip('\n') for el in f.readlines()]
        price_dict = {i+1:val for i, val in enumerate(price_list)}
        print(price_dict)
        f.seek(0,2)



if __name__ == '__main__':
    import sys

    exit(add_sale(sys.argv))
