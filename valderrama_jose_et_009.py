
   
inscripciones = {
        'F001': [14990, 30],
        'F002': [22990, 10],
        'F003': [39990, 0],
        'F004': [35990, 6],
        'F005': [159990, 2],
        'F006': [18990, 15],
    }



planes = {
        'F001': ['Plan Básico', 'mensual', 1, False, False, 'libre'],
        'F002': ['Plan Full', 'mensual', 1, True, True, 'libre'],
        'F003': ['Plan Estudiante', 'trimestral', 3, False, True, 
    'tarde'],
        'F004': ['Plan Senior', 'trimestral', 3, True, False, 'mañana'],
        'F005': ['Plan Anual Pro', 'anual', 12, True, True, 'libre'],
        'F006': ['Plan Nocturno', 'mensual', 1, False, True, 'noche'],
        
    }



def menu_principal():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Cupos por tipo de plan")
    print("2. Búsqueda de planes por rango de precio")
    print("3. Actualizar precio de plan")
    print("4. Agregar plan")
    print("5. Eliminar plan")
    print("6.Salir")
    print("=====================================")

def leer_opcion():
    while True:
        opcion = input('Ingrese una opción (1-6): ')
        if opcion == "":
            print('Error, la opcion no puede quedar vacia, por favor, ingrese un número entre 1 y 6.')
        elif opcion.strip() == "":
            print('Error, la opcion no puede contener solo espacios en blanco, por favor, ingrese un número entre 1 y 6.')
        else:    
            try:
                opcion = int(opcion)
                if opcion not in (1, 2, 3, 4, 5, 6):
                    print('Error, la opción ingresada no es válida. Por favor, ingrese un número entre 1 y 6.')
                else:
                    return opcion
            except ValueError as e:
                print('Error, la opción ingresada no es válida. Por favor, ingrese un número entre 1 y 6.')
                print('Detalle del error:', e)






def main():
    while True:
        menu_principal()
        opcion = leer_opcion()
        if opcion == 1:
            stock_plan()
        elif opcion == 2:
            busqueda_planes_rango_precio()
        elif opcion == 3:
            actualizar_precio_plan()
        elif opcion == 4:
            agregar_plan()
        elif opcion == 5:
            eliminar_plan()
        elif opcion == 6:
            print("muchas gracias por usar el programa")
            print("Programa finalizado...")
            exit(3)   
        else:
            return False 
            


def validar_codigo(codigo_nuevo):
    if codigo_nuevo == "":
        print("Error, no puede quedar vacio")
    elif codigo_nuevo.strip() == "":
        print("no puede contener solo espacios")
    else:
        return True
def validar_nombre(nombre_nuevo):
    if nombre_nuevo == "":
        print("Error, no puede quedar vacio")
    elif nombre_nuevo.strip() == "":
        print("no puede contener solo espacios")
    else:
        return True



def detalle_planes(codigo_plan):
    print('=' * 60)
    print(f'El código {codigo_plan} se encuentra en el diccionario de planes.\n')
    print('-' * 60)
    print(f'Detalles del plan: {planes[codigo_plan]}')
    print(f'tipo plan: {planes[codigo_plan][0]}')
    print(f'Precio plan: {inscripciones[codigo_plan][0]}')
    print(f'Stock disponible : {inscripciones[codigo_plan][1]}')
    print('-' * 60, '\n')

def stock_planes():
    print('=' * 60)
    print('***** STOCK     ******')
    print('=' * 60, '\n')
    codigo_plan = input('Ingrese el código del plan a buscar su stock: ')
    if codigo_plan == "":
        print('Error, el código del plan no puede quedar vacío. Por favor, ingrese un código válido.\n')
    elif codigo_plan.strip() == "":
        print('Error, el código del plan no puede contener solo espacios en blanco. Por favor, ingrese un código válido.\n')
    elif codigo_plan not in inscripciones:
        print(f'El código {codigo_plan} no se encuentra en el diccionario de inscripciones.\n')
    else:
        detalle_planes(codigo_plan)

def filtro_plan_rango_precio():
    while True:
        precio_min = input('Ingrese el precio mínimo: ')
        precio_max = input('Ingrese el precio máximo: ')
        if precio_min == "" or precio_max == "":
            print('Error, los precios no pueden quedar vacíos. Por favor, ingrese valores válidos.\n')
        elif precio_min.strip() == "" or precio_max.strip() == "":
            print('Error, los precios no pueden contener solo espacios en blanco. Por favor, ingrese valores válidos.\n')
        else:
            try:      
                precio_min = float(precio_min)
                precio_max = float(precio_max)
                if precio_min < 0 or precio_max < 0:
                    print('Error, los precios no pueden ser negativos. Por favor, ingrese valores válidos.\n')
                if precio_min > precio_max:
                    print('Error, el precio mínimo no puede ser mayor que el precio máximo. Por favor, ingrese valores válidos.\n')
                return precio_min, precio_max
            except ValueError as e:
                print('Error, los valores ingresados no son válidos. Por favor, ingrese números válidos.\n')
                print('Detalle del error:', e)

def busqueda_planes_rango_precio():
    print('=' * 60)
    print('***** BUSQUEDA DE PLAN POR RANGO DE PRECIO     ******')
    print('=' * 60, '\n')
    precio_min, precio_max = filtro_plan_rango_precio()
    inscripciones_en_rango = []
    for codigo, (precio, stock) in planes.items():
        if (precio_min <= precio <= precio_max) and (stock > 0):
            inscripciones_en_rango.append((codigo, inscripciones[codigo][0], precio, stock))
    if inscripciones_en_rango:
        print(f'planes disponibles en el rango de precio {precio_min} - {precio_max}:')
        for codigo, tipo, precio, stock in inscripciones_en_rango:
            print(f'Código: {codigo}, Modelo: {tipo}, Precio: {precio}, Stock: {stock}')
    else:
        print(f'No se encontraron planes disponibles en el rango de precio {precio_min} - {precio_max}.')

def buscar_codigo_plan():
    codigo_plan = ""
    while True:
        codigo_plan = input('Ingrese el código del plan a buscar: ')
        if codigo_plan == "":
            print('Error, el código del plan no puede quedar vacío. Por favor, ingrese un código válido.\n')
        elif codigo_plan.strip() == "":
            print('Error, el código del plan no puede contener solo espacios en blanco. Por favor, ingrese un código válido.\n')
        elif codigo_plan not in inscripciones:
            print(f'El código {codigo_plan} no se encuentra en el diccionario de inscripciones.\n')
        else:
            print(f'El código {codigo_plan} se encuentra en el diccionario de inscripciones.\n')
            print(f'Detalles del plan: {inscripciones[codigo_plan]}')
            print(f'Precio: {inscripciones[codigo_plan][0]}, Stock: {inscripciones[codigo_plan][1]}\n')
            return True,codigo_plan

def validar_precio_plan():
    estado_busqueda = False
    estado_busqueda,codigo_plan = buscar_codigo_plan()
    if estado_busqueda == False:
        return False,codigo_plan
    else:
        while True:
            print(f'¿Desea actualizar el precio del plan {codigo_plan}(s/n)?: ')
            if input().lower() == 's':
                precio_nuevo = input(f'Ingrese el nuevo precio para el plan {codigo_plan}: ')
                if precio_nuevo == "":
                    print('Error, el precio no puede quedar vacío. Por favor, ingrese un valor válido.\n')
                elif precio_nuevo.strip() == "":
                    print('Error, el precio no puede contener solo espacios en blanco. Por favor, ingrese un valor válido.\n')
                else:
                    try:
                        precio_nuevo = int(precio_nuevo)
                        if precio_nuevo < 0:
                            print('Error, el precio no puede ser negativo. Por favor, ingrese un valor válido.\n')                      
                        bodega[codigo_plan][0] = int(precio_nuevo)
                        print(f'El precio del notebook {codigo_plan} ha sido actualizado a: {inscripciones[codigo_plan][0]}\n')
                        return True,codigo_plan
                    except ValueError as e:
                        print('Error, el valor ingresado no es válido. Por favor, ingrese un número válido.\n')
                        print('Detalle del error:', e)   

def actualizar_precio_plan():
    estado_actualizacion = False
    estado_actualizacion,codigo_plan = validar_precio_plan()
    if estado_actualizacion:
        print(f'El precio del plan {codigo_plan} ha sido actualizado a: {inscripciones[codigo_plan][0]}\n')
    else:
        print('Se ha cancelado la operacion.\n')  


def validar_codigo(codigo_nuevo):
    if codigo_nuevo == "":
        print('Error: el codigo del nuevo plan no puede quedar vacio.\n')       
    elif codigo_nuevo.strip() == "":
        print('Error: el codigo del nuevo plan no puede contener solo espacios.\n')
    else:
        return True

def validar_nombre():

def validar_tipo():

def validar_duracion():

def validar_acceso_piscina():

def validar_incluye_clases():

def validar_horario():

def validar_precio():

def validar_cupos():



def agregar_plan():
    codigo_nuevo = input('Ingrese el codigo del nuevo plan: ')
    nombre_nuevo = input('Ingrese el nombre del plan : ')
    tipo_nueva = input('Ingrese el tipo de plan: ')
    duracion_nuevo = input('Ingrese la duracion del plan: ')
    acceso_piscina_nueva = input('Ingrese si tiene acceso a piscina: ')
    incluye_clases_nueva = input('Ingrese si incluye clases: ')
    horario_nuevo = input('Ingrese el horario del plan: ')
    precio_nuevo = input('Ingrese el precio del plan: ')
    stock_nuevo = input('Ingrese el stock del plan: ')

    bool_codigo = validar_codigo(codigo_nuevo)
    bool_nombre = validar_nombre(nombre_nuevo)
    bool_tipo = validar_tipo(tipo_nueva)
    bool_duracion= validar_duracion(duracion_nuevo)
    bool_acceso_piscina = validar_acceso_piscina(acceso_piscina_nueva)
    bool_incluye_clases = validar_incluye_clases(incluye_clases_nueva)
    bool_horario = validar_horario(horario_nuevo)
    bool_precio_nuevo = validar_precio(precio_nuevo)
    bool_stock = validar_cupos(stock_nuevo)

    if bool_codigo and bool_nombre and bool_tipo and bool_duracion and bool_acceso_piscina and bool_incluye_clases and bool_horario and bool_precio_nuevo and bool_stock:
        if codigo_nuevo in planes:
            print('Error: el codigo del plan a ingresar ya esta registrado en sistema.\n')
        else:
            
            precio_nuevo = int(precio_nuevo)
            stock_nuevo = int(stock_nuevo)

            planes[codigo_nuevo] = [nombre_nuevo,tipo_nueva,duracion_nuevo,acceso_piscina_nueva,incluye_clases_nueva,horario_nuevo]
            inscripciones[codigo_nuevo] = [precio_nuevo,stock_nuevo]
            print('Se ha agregado un nuevo plan a inscripcion exitosamente!.\n')
    else:
        print('Error: para ingresar un nuevo plan, todos los datos deben estar completos.\n')

def eliminar_plan():
    bool_codigo,codigo_plan = buscar_codigo_plan()

    if bool_codigo:
        confirmacion = input('Desea confirmar la eliminacion de la plan seleccionada(si/no): ')
        if confirmacion in ('si','SI','Si','sI'):
            eliminado = planes.pop(codigo_plan)
            eliminado = inscripciones.pop(codigo_plan)
            print(f'Se ha eliminado el plan {eliminado} exitosamente.\n')







main()       