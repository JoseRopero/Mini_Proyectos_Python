import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(plain_text, shift_number, direction_choice):  # Función para codificar y descodificar un texto
    cipher_text = ""  # Inicializamos una cadena vacía que contendrá el cifrado
    if direction_choice == 'encode':
        for letter in plain_text:  # Recorremos el mensaje y si hay algún símbolo o espacio lo dejamos en su posición
            if letter not in alphabet:
                cipher_text += letter
            else:  # Si no, movemos el alphabet el número de posiciones que introducimos en shift
                position = alphabet.index(letter)
                new_position = position + shift_number
                cipher_text += alphabet[new_position]
        print(f"Texto encriptado: {cipher_text}")
    elif direction_choice == 'decode':  # Igual, pero para desencriptar, lo que hacemos es retroceder en alphabet
        for letter in plain_text:
            if letter not in alphabet:
                cipher_text += letter
            else:
                position_encrypt = alphabet.index(letter)
                new_position_backwards = position_encrypt - shift_number
                cipher_text += alphabet[new_position_backwards]
        print(f"Texto desencriptado: {cipher_text}")


opcion_bool = True
print(art.logo)

while opcion_bool:

    print("\n")

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    print()
    text = input("Type your message: ").lower()
    print()
    shift = int(input("Type the shift number: "))
    print()

    if shift > 25:  # Si el número introducido es mayor de 25, el programa nos lanza un error, con esto lo solucionamos
        shift %= 26

    caesar(text, shift, direction)

    print()
    opcion = input("Quiere codificar otro mensaje: Y or N: ").lower()
    if opcion == 'n':
        opcion_bool = False
print()
print("Goodbye")
