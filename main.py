def opcion1():
    print('Ingrese una evaluación del 1 al 5')
    point = input()
    if point.isdecimal():
        point = int(point)
        if  point <= 0 or point > 5: 
            print('Ingrese un valor del 1 al 5')
        else:
            print('Ingrese un comentario')
            comment = input()
            post = f'Puntos: {point} Comentario: {comment}'
            file_pc = open("data.txt", 'a')
            file_pc.write(f'{post}\n')
            file_pc.close()
    else:
        print('Por favor, ingrese un valor numérico para los puntos de evaluación')
    
def opcion2():
    print('Resultados anteriores')
    read_file = open("data.txt", "r")
    print(read_file.read())
    read_file.close()
    



while True:
    print('Seleccione la acción que desea realizar')
    print('1: Ingresar puntos de evaluación y comentarios')
    print('2: Ver resultados anteriores')
    print('3: Salir')
    num = input()

    if num.isdecimal():
        num = int(num)

        if num == 1:
            opcion1()
        
        elif num == 2:
            opcion2()
            
        elif num == 3:
            print('Saliendo del programa')
            break
        else:
            print('Por favor, ingrese un valor del 1 al 3')
    else:
        print('Por favor, ingrese un valor del 1 al 3')
