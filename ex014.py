cel = float(input('\033[1;35mdigite a temperatura em escala\033[1;30m °C\033[m'))
fah = (cel * 9/5) + 32
kel = (cel + 273.15)
print('\033[1;35mA temperatura de \033[1;30m{}°C\033[m \033[1;35mcorresponde a \033[1;34m{}°F\033[1;35m e \033[1;31m{}°K'.format(cel, fah, kel))
