addres_book= {
"alisa":"ул.пушкина д.22",
"bob":"ул.макаенко д.52",
"charli":"ул.пивчанский д.99"} # Создаем пустой словарь для хранения данных о людях

while True:  # учловие всегда будет истиным поэтому оно будет выполнятся
    print("выберите действие:")
    print("1.показать все адреса")
    print("2.изменить адрес")
    print("3.удалить запись")
    print("4. выйти из системы")
    choise = input("введите номер____")  # Считываем выбор пользователя
    if choise =="1":
        print("все адреса:")
        for name, addres in addres_book.items():   
            print(f"{name}:{addres}")
    elif choise =="2":
        name = input('введите имя:')
        if name in addres_book: # Проверяем есть ли человек в словаре
            new_addres = input("введите адресс:")
            addres_book[name]= new_addres   #изменить адресс
            print(f"адрес для{name} изменили на {new_addres}")
        else:
            print("erooooor найди ошибку")
    elif choise == '3':
      name = input("Введите имя человека: ")
      if name in addres_book:
          del addres_book[name] # Удаляем человека из словаря
          print(f"Человек {name} удален из словаря.")
      else:
        print(f"Человека с именем {name} нет в словаре.")
    elif choise == "4":
        break   

    else:
        print("неверный ввод попробуй снова")
