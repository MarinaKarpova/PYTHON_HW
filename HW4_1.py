def salary():
    from sys import argv

    name, hourly_rate, hours, prime = argv
    print("Имя скрипта: ", name)
    print("Выработка в часах:", hours)
    print("Ставка в час:", hourly_rate)
    print("Премия:", prime)
    hourly_rate = int(hourly_rate)
    hours = int(hours)
    prime = int(prime)
    salary = hourly_rate * hours + prime
    print(f"Заработная плата сотрудника равна {salary}")

salary()
