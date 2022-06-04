import math
print('---------------------------------------')
print('Convertidor de unidades/Unity convertor')
print('---------------------------------------')

idioma = input('Español(1)/English(2)')

if idioma == '1':
    #Se solicta si se quiere convertir peso o medidas

    m_p = int(input('Quieres convertir medidas o pesos?(1/2)'))

    #Si se eligio medida

    if m_p == 1:
        #Se solisita de que sitema convertir
        i_m = int(input('Quieres convertir de imperial a metrico o de metrico a imperial?(1/2)'))
        #Si se introduce 1
        if i_m == 1:
            m_i_p_y = input('Que unidad imperial deseas convertir, millas, pies, pulgadas, o yardas(m/f/i/y)')
            #Si se introdujo millas, lo convierte a metros, y si son mas de 5 millas, a kilometros
            if m_i_p_y == 'm':
                while True:
                    try:
                        cantidad = float(input("Cuantas millas deseas converit?"))
                        break
                    except ValueError:
                        print("Valor no valido. Intenta de nuevo")
                if cantidad > 5:
                    millas = 1.60934
                    resultado = millas * cantidad
                    print(round(resultado, 2), ' kilometros')
                else:
                    millas = 1609.34
                    resultado = millas * cantidad
                    print(round(resultado, 2), ' metros')
            #Si se introdujo pies, lo convierte a centimetros
            elif m_i_p_y == 'f':
                pies = 30.48
                while True:
                    try:
                        cantidad = float(input("Cuantos pies deseas converit?"))
                        break
                    except ValueError:
                        print("Valor no valido. Intenta de nuevo")
                resultado = pies * cantidad
                print(round(resultado, 2), ' centimetros')
            #Si se introdujo pulgadas, lo convierte a centimetros
            elif m_i_p_y == 'i':
                pulgadas = 2.54
                while True:
                    try:
                        cantidad = float(input("Cuantas pulgadas deseas converit?"))
                        break
                    except ValueError:
                        print("Valor no valido. Intenta de nuevo")
                resultado = pulgadas * cantidad
                print(round(resultado, 2), ' centimetros')
            #Si se introudujo y
            elif m_i_p_y == 'y':
                yardas = 0.9144
                while True:
                    try:
                        cantidad = float(input("Cuantas yardas deseas converit?"))
                        break
                    except ValueError:
                        print("Valor no valido. Intenta de nuevo")
                resultado = yardas * cantidad
                print(round(resultado, 2), ' metros')
            #Si se eintrodujo otra cosa
            else:
                print('Opcion no disponible')
        #Si se introduce 2
        elif i_m == 2:
            km_mt_cm = input('Que unidad metrica deseas convertir, kilometros, metros, o centimetros(km/mt/cm)')
            #Si se introduce km, se convierte a millas
            if km_mt_cm == 'km':
                kilometros = 0.621371
                while True:
                    try:
                        cantidad = float(input("Cuantos kilometros deseas converit?"))
                        break
                    except ValueError:
                        print("Valor no valido. Intenta de nuevo")
                resultado = kilometros * cantidad
                print(round(resultado, 2), ' millas')
            #Si se introduce mt, se convierte a pies
            elif km_mt_cm == 'mt':
                metros = 3.28084
                while True:
                    try:
                        cantidad = float(input("Cuantos metros deseas converit?"))
                        break
                    except ValueError:
                        print("Valor no valido. Intenta de nuevo")
                resultado = metros * cantidad
                print(round(resultado, 2), ' pies')
            #Si se introduce cm, se convierte a pulgadas
            elif km_mt_cm == 'cm':
                centimetros = 0.393701
                while True:
                    try:
                        cantidad = float(input("Cuantos centimetros deseas converit?"))
                        break
                    except ValueError:
                        print("Valor no valido. Intenta de nuevo")
                resultado = centimetros * cantidad
                print(round(resultado, 2), ' pulgadas')
            #Si se introduce otra cosa
            else:
                print('Opcion no disponible 1')
        #Si se introduce otro numero
        else:
            print('Opcion no disponible 2')

    #Si se eligio peso

    elif m_p == 2:
        #Se solocira de que sistema convertir
        i_m2 = int(input('Quieres convertir de imperial a metrico o de metrico a imperial?(1/2)'))

        #Si se introdujo 1
        if i_m2 == 1:
            t_l_o = input('Quieres convertir toneladas, libras, u onzas?(t/l/o)')
            #Si se introdujo t
            if t_l_o == 't':
                toneladas = 1000
                while True:
                    try:
                        cantidad = float(input("Cuantos toneladas deseas converit?"))
                        break
                    except ValueError:
                        print("Valor no valido. Intenta de nuevo")
                resultado = toneladas * cantidad
                print(round(resultado, 2), 'kilogramos')
            #Si se introdujo l
            elif t_l_o == 'l':
                libra = 453.592
                while True:
                    try:
                        cantidad = float(input("Cuantos libras deseas converit?"))
                        break
                    except ValueError:
                        print("Valor no valido. Intenta de nuevo")
                resultado = libra * cantidad
                print(round(resultado, 2), 'gramos')
            #Si se introdujo o
            elif t_l_o == 'o':
                onzas = 29.5735
                while True:
                    try:
                        cantidad = float(input("Cuantos onzas deseas converit?"))
                        break
                    except ValueError:
                        print("Valor no valido. Intenta de nuevo")
                resultado = onzas * cantidad
                print(round(resultado, 2), 'mililitros')
            #Si se introdujo otra cosa
            else:
                print('Opcion no disponible 3')

        #Si se introdujo 2
        elif i_m2 == 2:
            k_g_m = input('Quieres convertir kilogrmos, gramos o miligramos(k/g/ml)')
            #Si se introdujo k
            if k_g_m == 'k':
                kilogramos = 0.001
                while True:
                    try:
                        cantidad = float(input("Cuantos kilogramos deseas converit?"))
                        break
                    except ValueError:
                        print("Valor no valido. Intenta de nuevo")
                resultado = kilogramos * cantidad
                print(round(resultado, 5), 'toneladas')
            #Si se introdujo g
            elif k_g_m == 'g':
                gramos = 0.00220462
                while True:
                    try:
                        cantidad = float(input("Cuantos gramos deseas converit?"))
                        break
                    except ValueError:
                        print("Valor no valido. Intenta de nuevo")
                resultado = gramos * cantidad
                print(round(resultado, 7), 'libras')
            #Si se introdujo m
            elif k_g_m == 'ml':
                mililitros = 29.5735
                while True:
                    try:
                        cantidad = float(input("Cuantos mililitros deseas converit?"))
                        break
                    except ValueError:
                        print("Valor no valido. Intenta de nuevo")
                resultado = mililitros * cantidad
                print(round(resultado, 7), 'onzas')

    #Si se eligio una opcion imbalida

    else:
        print('Opcion no disponible 4')


elif idioma == '2':
    #Se solicta si se quiere convertir peso o medidas

    m_p = int(input('Do you want to convert measures or weights? (1/2)'))

    #Si se eligio medida

    if m_p == 1:
        #Se solisita de que sitema convertir
        i_m = int(input('Do you want to convert from imperial to metric or from metric to imperial? (1/2)'))
        #Si se introduce 1
        if i_m == 1:
            m_i_p_y = input('What imperial unit do you want to convert, miles, feet, inches, or yards? (M / f / i / y)')
            #Si se introdujo millas, lo convierte a meters, y si son mas de 5 millas, a kilometers
            if m_i_p_y == 'm':
                while True:
                    try:
                        cantidad = float(input("How many miles do you want to convert?"))
                        break
                    except ValueError:
                        print("Invalid value. Try again")
                if cantidad > 5:
                    millas = 1.60934
                    resultado = millas * cantidad
                    print(round(resultado, 2), ' kilometers')
                else:
                    millas = 1609.34
                    resultado = millas * cantidad
                    print(round(resultado, 2), ' meters')
            #Si se introdujo pies, lo convierte a centimetros
            elif m_i_p_y == 'f':
                pies = 30.48
                while True:
                    try:
                        cantidad = float(input("How many feet do you want to convert?"))
                        break
                    except ValueError:
                        print("Invalid value. Try again")
                resultado = pies * cantidad
                print(round(resultado, 2), ' centimeters')
            #Si se introdujo pulgadas, lo convierte a centimetros
            elif m_i_p_y == 'i':
                pulgadas = 2.54
                while True:
                    try:
                        cantidad = float(input("How many inches do you want to convert?"))
                        break
                    except ValueError:
                        print("Invalid value. Try again")
                resultado = pulgadas * cantidad
                print(round(resultado, 2), ' centimeters')
            #Si se introudujo y
            elif m_i_p_y == 'y':
                yardas = 0.9144
                while True:
                    try:
                        cantidad = float(input("How many yards do you want to convert?"))
                        break
                    except ValueError:
                        print("Invalid value. Try again")
                resultado = yardas * cantidad
                print(round(resultado, 2), ' meters')
            #Si se eintrodujo otra cosa
            else:
                print('Option not available')
        #Si se introduce 2
        elif i_m == 2:
            km_mt_cm = input('What metric unit do you want to convert, kilometers, meters, or centimeters(km/mt/cm)')
            #Si se introduce km, se convierte a millas
            if km_mt_cm == 'km':
                kilometers = 0.621371
                while True:
                    try:
                        cantidad = float(input("How many kilometers do you want to convert?"))
                        break
                    except ValueError:
                        print("Invalid value. Try again")
                resultado = kilometers * cantidad
                print(round(resultado, 2), ' miles')
            #Si se introduce mt, se convierte a pies
            elif km_mt_cm == 'mt':
                meters = 3.28084
                while True:
                    try:
                        cantidad = float(input("How many meters do you want to convert?"))
                        break
                    except ValueError:
                        print("Invalid value. Try again")
                resultado = meters * cantidad
                print(round(resultado, 2), ' feet')
            #Si se introduce cm, se convierte a pulgadas
            elif km_mt_cm == 'cm':
                centimeters = 0.393701
                while True:
                    try:
                        cantidad = float(input("How many centimeters do you want to convert?"))
                        break
                    except ValueError:
                        print("Invalid value. Try again")
                resultado = centimeters * cantidad
                print(round(resultado, 2), ' inches')
            #Si se introduce otra cosa
            else:
                print('Option not available 1')
        #Si se introduce otro numero
        else:
            print('Option not available 2')

    #Si se eligio peso

    elif m_p == 2:
        #Se solocira de que sistema convertir
        i_m2 = int(input('Do you want to convert from imperial to metric or from metric to imperial? (1/2)'))

        #Si se introdujo 1
        if i_m2 == 1:
            t_l_o = input('Do you want to convert tons, pounds, or ounces? (t / l / o)')
            #Si se introdujo t
            if t_l_o == 't':
                toneladas = 1000
                while True:
                    try:
                        cantidad = float(input("How many tons do you want to convert?"))
                        break
                    except ValueError:
                        print("Invalid value. Try again")
                resultado = toneladas * cantidad
                print(round(resultado, 2), 'kilograms')
            #Si se introdujo l
            elif t_l_o == 'l':
                libra = 453.592
                while True:
                    try:
                        cantidad = float(input("How many pounds do you want to convert?"))
                        break
                    except ValueError:
                        print("Invalid value. Try again")
                resultado = libra * cantidad
                print(round(resultado, 2), 'grams')
            #Si se introdujo o
            elif t_l_o == 'o':
                onzas = 29.5735
                while True:
                    try:
                        cantidad = float(input("How many ounces do you want to convert?"))
                        break
                    except ValueError:
                        print("Invalid value. Try again")
                resultado = onzas * cantidad
                print(round(resultado, 2), 'milliliters')
            #Si se introdujo otra cosa
            else:
                print('Option not available 3')

        #Si se introdujo 2
        elif i_m2 == 2:
            k_g_m = input('Do you want to convert kilograms, grams or milligrams? (K / g / mg)')
            #Si se introdujo k
            if k_g_m == 'k':
                kilograms = 0.001
                while True:
                    try:
                        cantidad = float(input("How many kilograms do you want to convert?"))
                        break
                    except ValueError:
                        print("Invalid value. Try again")
                resultado = kilograms * cantidad
                print(round(resultado, 5), 'tons')
            #Si se introdujo g
            elif k_g_m == 'g':
                gramos = 0.00220462
                while True:
                    try:
                        cantidad = float(input("How many grams do you want to concert?"))
                        break
                    except ValueError:
                        print("Invalid value. Try again")
                resultado = gramos * cantidad
                print(round(resultado, 7), 'punds')
            #Si se introdujo m
            elif k_g_m == 'ml':
                mililitros = 29.5735
                while True:
                    try:
                        cantidad = float(input("How many milliliters do you want to convert?"))
                        break
                    except ValueError:
                        print("Invalid value. Try again")
                resultado = mililitros * cantidad
                print(round(resultado, 7), 'ounces')

    #Si se eligio una opcion imbalida

    else:
        print('Option not available 4')

else:
    print('Opcion no disponible')