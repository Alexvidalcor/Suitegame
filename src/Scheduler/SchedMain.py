'''
Hacer una agenda basada en fichero

Se trata de tener un fichero tipo csv donde en cada linea guardemos datos 
de un contacto, divido el problema en partes.
Mostrar un menu interactivo (print / int(input())) 
Hacer que en el menu se pueda volver atras desde un submenu (pulso 0 y vuelvo al menu principals).
Hacemos lo que nos resulta mas intuitivo dada nuestra experiencia previa: hacer el listado de la agenda.
'''

def Scheduler():
    #Generar archivo csv
    columns = ss.FormatInput(input("Introduce nombre de columnas separados por comas: "))
    newTable = ss.EmptyTableCreate(*columns)
    print(newTable)

    while True:
        print("Puedes modificar la tabla de la siguiente manera \n 1. Insertar datos (insertar) \
            \n 2. Modificar datos (modificar) \n 3. Mostrar tabla (mostrar) \
            \n 4. Eliminar datos (eliminar) \n 5. Ordenar columnas (ordenar) \
            \n 6. Finalizar programa (finalizar)")
        mainCursor = input("¿Qué deseas hacer? ")

        #Insertar datos
        if mainCursor.lower() == "insertar":
            columnSelect = ss.FormatInput(input("Introduce Columnas a añadir datos: "))
            value = input("Introduce un único valor para añadir: ")
            newTable = ss.InsertValues(newTable,value,columnSelect)
            print(newTable)

        #Mostrar tabla
        elif mainCursor.lower() =="mostrar":
            print(f"\n Tienes {newTable.shape[0]} filas y {newTable.shape[1]} columnas: \n")
            print(newTable,"\n")

        #Eliminar datos
        elif mainCursor.lower() =="eliminar":
            modeSelect = ss.FormatInput(input("¿Quieres eliminar una columna o una fila? (columna/fila/nada)"))[0]
            print(modeSelect)
            if modeSelect.lower() == "columna":
                selection = ss.FormatInput(input("Introduce columnas a eliminar separadas por comas: "))
                newTable = ss.DropValues(newTable, selection,colsMode=1)
            elif modeSelect.lower() == "fila":
                selection = ss.FormatInput(input("Introduce filas a eliminar separadas por comas: "))
                newTable = ss.DropValues(newTable, selection)
            elif modeSelect.lower() == "nada":
                continue
            print(newTable)

        #Modificar datos
        elif mainCursor.lower() == "modificar":
            selection = ss.FormatInput(input("Selecciona celda a modificar (fila,columna/nada): "))
            if selection != "nada":
                value = ss.FormatInput(input("Introduce valor a modificar (valor)"))
                newTable = ss.ModValues(newTable,(selection), value[0])
                print(newTable)
            else:
                continue

        #Ordenar datos
        elif mainCursor.lower() == "ordenar":
            selection = ss.FormatInput(input("Selecciona columnas a ordenar (columna/nada): "))
            newTable = ss.sortValues(newTable, selection)
            print(newTable)

        #Forzar cierre de programa
        elif mainCursor.lower() =="eliminar":
            break

        #Finalizar y guardar archivo
        ending = input("Deseas cerrar la operación (s/n): ")
        if ending.lower() =="s":
            howResult= input("Deseas guardar como excel o csv (Excel/CSV/Nada)")
            if howResult.lower() != "nada":
                ending = ss.GenerateOutput(newTable,howResult=True)
            else:
                print("Programa cerrado sin output")
                break
        
if __name__ != "__main__":
    import src.Scheduler.SchedSupport as ss
else:
    import SchedSupport as ss
    Scheduler()

