
def celsius_to_fahreiheit(celsius):
    return(celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahreiheit_to_Kelvin(fahreiheit):
    kelvin = (fahreiheit - 32)* 5/9 + 273.15
    return kelvin

def fahreiheit_to_celsius(fahreiheit):
    celsius = (fahreiheit - 32)* 5/9
    return celsius

def kelvin_to_fahreiheit(kelvin):
    fahreiheit = (kelvin - 273.15)* 9/5 + 32
    return fahreiheit

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

print("******/--/Convertor de temperaturas/--/******\n")
print("1 - CONVERTER EM CELSIUS")
print("2 - CONVERTER EM KELVIN")
print("3 - CONVERTER EM FAHREIHEIT\n")

escolha = input("||DIGITE A OPÇÃO||\n")

if escolha == '1':
    escolha_two = input("DESEJA CONVERTER PARA QUAL ESCALA TERMOMÉTRICA? FAHREIHEIT(F) OU KELVIN(K)\n").upper()
    celsius = float(input("Digite a temperatura em celsius: "))

    if escolha_two == 'F':
        resultado = celsius_to_fahreiheit(celsius)
        print(f"{celsius}°C é equivalente a {resultado:.2f}°F.")

    elif escolha_two == 'K':
        resultado = celsius_to_kelvin(celsius)
        print(f"{celsius}°C é equivalente a {resultado:.2f}°K.")

    else:
        print("opção invalida")

elif escolha == '2':
    escolha_two = input("DESEJA CONVERTER PARA QUAL ESCALA TERMOMÉTRICA? CELSIUS(C) OU FAHREIHEIT(F)\n").upper()
    kelvin = float(input("Digite a temperatura em Kelvin: "))

    if escolha_two == 'C':
        resultado = kelvin_to_celsius(kelvin)
        print(f"{kelvin}°K é equivalente a {resultado}°C.")

    elif escolha_two == 'F':
        resultado = kelvin_to_fahreiheit(kelvin)
        print(f"{kelvin}°K é equivalente a {resultado}°F")

    else:
        print("Opção invalida")

elif escolha == '3':
    escolha_two = input("DESEJA CONVERTER PARA QUAL ESCALA TERMOMÉTRICA? CELSIUS(C) OU KELVIN(K)\n").upper()
    fahreiheit = float(input("Digite a temperatura em Fahreiheit: "))

    if escolha_two == 'C':
        resultado = fahreiheit_to_celsius(fahreiheit)
        print(f"{fahreiheit}°F é equivalente a {resultado}°C")

    elif escolha_two == 'K':
        resultado = fahreiheit_to_Kelvin(fahreiheit)
        print(f"{fahreiheit}°F é equivalente a {resultado}°K")
    
    else:
        print("opçao invalida")

else:
    print("Opção invalida, tente os numeros 1, 2 ou 3")