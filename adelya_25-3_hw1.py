Naryn = int(input("Введите температуру Нарына"))
Chuy = int(input("Введите температуру Чуя"))
Batken = int(input("Введите температуру Баткена"))
Jalal_Abad = int(input("Введите температуру Джалал-Абада"))
Osh = int(input("Введите температуру Оша"))
Talas = int(input("Введите температуру Таласа"))
Issyk_Kul = int(input("Введите температуру Иссык-Куля"))

average = (Naryn + Chuy + Batken + Jalal_Abad + Osh + Talas + Issyk_Kul)/7
rounded = round(average, 2)
print(f"Средний показатель температуры воздуха по КР на сегодня {rounded}°C.")







