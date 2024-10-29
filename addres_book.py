addres_book= {
"alisa":"ул.пушкина д.22",
"bob":"ул.макаенко д.52",
"charli":"ул.пивчанский д.99"}

while True:  # учловие всегда будет истиным поэтому оно будет выполнятся
    print("выберите действие:")
    print("1.показать все адреса")
    print("2.изменить адрес")
    print("3. выйти из системы")
    choise = input("введите номер")
    if choise =="1":
        print("все адреса:")
        for name, addres in addres_book.items():
            print(f"{name}:{addres}")
    elif choise =="2":
        name = input('введите имя:')
        if name in addres_book:
            new_addres = input("введите адресс:")
            addres_book[name]= new_addres   #изменить адресс
            print(f"адрес для{name} изменили на {new_addres}")
        else:
            print("erooooor найди ошибку")
    elif choise == "3":
        break