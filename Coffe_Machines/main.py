from replit import clear

from data import MENU, resources

PRECIO_ESPRESSO = MENU['espresso']['cost']
PRECIO_LATTE = MENU['latte']['cost']
PRECIO_CAPPUCCINO = MENU['cappuccino']['cost']
DEPOSITO_AGUA = resources['water']


def informe_estado(deposito, caja):
    print(f"Agua: {deposito['water']}ml")
    print(f"Leche: {deposito['milk']}ml")
    print(f"Café: {deposito['coffee']}g")
    print(f"Dinero: ${caja}")


def comprobar_estado(eleccion_cliente, deposito_maq, menu_maq):
    water = menu_maq[eleccion_cliente]['ingredients']['water']
    coffee = menu_maq[eleccion_cliente]['ingredients']['coffee']
    if eleccion_cliente == 'espresso':
        if water > deposito_maq['water']:
            print("Lo siento, no hay suficiente agua.")
            return False
        elif coffee > deposito_maq['coffee']:
            print("Lo siento, no hay suficiente coffee.")
            return False
        else:
            return True
    elif eleccion_cliente == 'latte' or eleccion_cliente == 'cappuccino':
        milk = menu_maq[eleccion_cliente]['ingredients']['milk']
        if water > deposito_maq['water']:
            print("Lo siento, no hay suficiente agua.")
            return False
        elif coffee > deposito_maq['coffee']:
            print("Lo siento, no hay suficiente café.")
            return False
        elif milk > deposito_maq['milk']:
            print("Lo siento, no hay suficiente leche.")
            return False
        else:
            return True


def insertar_dinero():
    print("Escriba el número de monedas que va ha insertar.")
    moneda_euro = int(input("Cuantas monedas de 1 euro?: "))
    moneda_20 = int(input("Cuantas monedas de 20 céntimos?: "))
    moneda_10 = int(input("Cuantas monedas de 10 céntimos?: "))
    moneda_5 = int(input("Cuantas monedas de 5 céntimos?: "))
    total_insertado = (1 * moneda_euro) + (0.20 * moneda_20) + (0.10 * moneda_10) + (0.05 * moneda_5)
    return total_insertado


def restar_ingredientes(tipo_cafe, menu_maq, deposito_ingredientes):
    water = menu_maq[tipo_cafe]['ingredients']['water']
    coffee = menu_maq[tipo_cafe]['ingredients']['coffee']
    if tipo_cafe == 'espresso':
        deposito_ingredientes['water'] -= water
        deposito_ingredientes['coffee'] -= coffee
    elif tipo_cafe == 'latte' or tipo_cafe == 'cappuccino':
        milk = menu_maq[tipo_cafe]['ingredients']['milk']
        deposito_ingredientes['water'] -= water
        deposito_ingredientes['coffee'] -= coffee
        deposito_ingredientes['milk'] -= milk


total_caja = 0
apagado = True
while apagado:
    clear()
    eleccion = input("Qué le gustaría? (espresso/latte/cappuccino): ").lower()
    if eleccion == 'espresso':
        if comprobar_estado(eleccion, resources, MENU):
            dinero = insertar_dinero()
            if dinero > PRECIO_ESPRESSO:
                total_caja += PRECIO_ESPRESSO
                devolucion = dinero - PRECIO_ESPRESSO
                print(f"Aquí tiene su vuelta: {devolucion}")
                print("Espresso servido, gracias por su visita")
                restar_ingredientes(eleccion, MENU, resources)
            elif dinero == PRECIO_ESPRESSO:
                total_caja += PRECIO_ESPRESSO
                print("Espresso servido, gracias por su visita")
                restar_ingredientes(eleccion, MENU, resources)
            else:
                print("Dinero insuficiente. Elija otra opción")
    elif eleccion == 'latte' or eleccion == 'cappuccino':
        if comprobar_estado(eleccion, resources, MENU):
            dinero = insertar_dinero()
            if eleccion == 'latte':
                if dinero > PRECIO_LATTE:
                    total_caja += PRECIO_LATTE
                    devolucion = dinero - PRECIO_LATTE
                    print(f"Aquí tiene su vuelta: {devolucion}")
                    print("Latte servido, gracias por su visita")
                    restar_ingredientes(eleccion, MENU, resources)
                elif dinero == PRECIO_LATTE:
                    total_caja += PRECIO_LATTE
                    print("Latte servido, gracias por su visita")
                    restar_ingredientes(eleccion, MENU, resources)
                else:
                    print("Dinero insuficiente. Elija otra opción")
            elif eleccion == 'cappuccino':
                if dinero > PRECIO_CAPPUCCINO:
                    total_caja += PRECIO_CAPPUCCINO
                    devolucion = dinero - PRECIO_CAPPUCCINO
                    print(f"Aquí tiene su vuelta: {devolucion}")
                    print("Cappuccino servido, gracias por su visita")
                    restar_ingredientes(eleccion, MENU, resources)
                elif dinero == PRECIO_CAPPUCCINO:
                    total_caja += PRECIO_CAPPUCCINO
                    print("Cappuccino servido, gracias por su visita")
                    restar_ingredientes(eleccion, MENU, resources)
                else:
                    print("Dinero insuficiente. Elija otra opción")
    elif eleccion == 'informe':
        informe_estado(resources, total_caja)
    elif eleccion == 'apagado':
        apagado = False
    else:
        print("Elija una opción correcta.")
