import random

money = 0
buyDict = {}
transactions = {}
counter = 0

def refill(money_old, counterOld):
    money_add = int(input('введите сумму пополнения: '))
    moneyNew = money_old + money_add
    counterOld += 1
    print('баланс = ', moneyNew )
    return moneyNew, counterOld, money_add

def buy(money_old, counterOld):
    cost_item = int(input('введите цену покупки: '))
    if cost_item <= money_old:

        moneyNew = money_old - cost_item
        counterOld +=1
        cost_name = input('средств достаточно. Введите наименование покупки: ')
        print('баланс = ', moneyNew)
    else:
        print('на вашем счете недостаточно средств')
        pass

    return [cost_name,cost_item, moneyNew, counterOld ]

def buy_stories(buyDict):
    for item,value in buyDict.items():
        print( f'Номер операции: {value[1]} Покупка: {item}, стоимость: {value[0]}')

def cassa(transactions):
    for item,value in transactions.items():
        print( f'Номер операции: {item} Расход/приход: {value[0]}, ,баланс: {value[1]}')


while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. история операций')
    print('5. выход')

    choice = input('Выберите пункт меню ')

    if choice == '1':
        moneyNew, counter, money_add = refill(money,counter)
        transactions[counter] = [money_add, moneyNew]
        money = moneyNew
        print(money, counter)

    elif choice == '2':
        cost_name, cost_item, moneyNew, counter = buy(money,counter)
        buyDict[cost_name] = [cost_item, counter]
        transactions[counter] = [-1 * cost_item, moneyNew]
        money = moneyNew

    elif choice == '3':
        buy_stories(buyDict)

    elif choice == '4':
        cassa(transactions)

    elif choice == '5':
        print('до встречи')
        print(transactions)
        print(buyDict)
        break
    else:
        print('Неверный пункт меню')