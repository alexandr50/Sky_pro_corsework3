from scripts.utils import sorted_func_for_date, correct_date_for_output, correct_number_card, get_correct_bill, FILE_NAME


def main():
    res: list = sorted_func_for_date(FILE_NAME)
    arr = []
    lst = []
    for item in res:
        lst.clear()
        lst.insert(0, correct_date_for_output(item['date']) + ' ' + item['description'])
        lst.append(item['operationAmount']['amount'] + ' ' + item['operationAmount']['currency']['name'])
        lst.insert(1, correct_number_card(item.get('from')) + ' -> ' + get_correct_bill(item['to']))
        lst.append('\n')
        lst1 = lst[::]
        arr.append(lst1)
    for i in arr:
        for j in i:
            print(j.strip())



if __name__ == '__main__':
    main()