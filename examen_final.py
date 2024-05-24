def caracter_byte(caracter):
    return format(ord(caracter), '08b')

def palabra_byte(palabra):
    return ' '.join(format(ord(c), '08b') for c in palabra)

def byte_ascii(byte):
    character = chr(int(byte, 2))
    hex_value = format(ord(character), 'x')
    return f"{character}-{hex_value}"

def main():
    while True:
        print("\nMenú de Opciones")
        print("a. Generar la representación en byte de un carácter")
        print("b. Generar la representación en byte de una palabra")
        print("c. Generar la representación ASCII de un byte")
        print("d. Salir")
        
        opc = input("Seleccione una opción: ").strip().lower()
        
        if opc == 'a':
            caracter = input("Ingrese un carácter: ").strip()
            if len(caracter) != 1:
                print("Por favor, ingrese un único carácter.")
            else:
                print(f"La representación en byte de '{caracter}' es: {caracter_byte(caracter)}")
        
        elif opc == 'b':
            palabra = input("Ingrese una palabra: ").strip()
            print(f"La representación en byte de '{palabra}' es: {palabra_byte(palabra)}")
        
        elif opc == 'c':
            byte = input("Ingrese una representación en byte (8 bits): ").strip()
            if len(byte) != 8 or not all(bit in '01' for bit in byte):
                print("Por favor, ingrese una cadena de 8 bits válida.")
            else:
                print(f"La representación ASCII de '{byte}' es: {byte_ascii(byte)}")
        
        elif opc == 'd':
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
