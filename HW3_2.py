def data(name, surname, year, city, email, phone):
    print(f"{name}, {surname}, {year}, {city}, {email}, {phone}")


data(name=input("Введите ваше имя"), surname=input("Введите вашу фамилию"),
     year=input("Введите год вашего рождения"), city=input("Введите ваш город проживания"),
     email=input("Введите ваш еmail"), phone=input("Введите ваш номер телефона"))
