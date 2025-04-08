### Imports ################################################## 
import os   #per neteja la pantalla
import json
#Variables ###################################################

existenciasEjemplo = {
 "id": 1 ,
 "nombre" : "Don simon",
 "cantidad": 200,
 "Precio/unidad" : 15
}
existencias = [existenciasEjemplo]
nom_fitxer = "existencias.json"

def menu():
    #Netejem la pantalla
    os.system('cls')            
    #Mostrem les diferents opcions
    print("Gestió existencias")
    print("-------------------------------")
    print("1. Mostrar existencias")
    print("2. Afegir existencias")
    print("3. Veure existencias")
    print("4. Esborrar existencias")
    print("5. Editar existencias")

    print("\n0. Sortir\n\n\n")
    print(">", end=" ")

    #i retornem l'opció escollida per l'usuari
    return input()

### Programa ################################################
while True:    
    #Executem una opció funció del que hagi escollit l'usuari
    match menu():
        # Mostrar existencias ##################################
        case "1":
            os.system('cls')
            print("Mostrar existencias")
            print("-------------------------------")
            for x in existencias:
                j = json.dumps(x)
                print(j)
                print(type(j)) 
            input()
        # Afegir existencias ##################################
        case "2":
            os.system('cls')
            print("Afegir existencias")
            print("-------------------------------")
            #DEFINIMOS
            print("Nom de producte") 
            nom_nou = input()
            print("Cantitat") 
            cantitat_nou = input()
            print("preu per unitat")
            preu_nou = input()
            #COMPILAMOS
            nou_existencias = {"id": (len(existencias)+1), "nombre" : nom_nou, "cantidad": cantitat_nou, "Precio/unidad": preu_nou}
            #INSERTAMOS
            existencias.append(nou_existencias)
            print("Elemento creado")
        # Veure existencias ##################################
        case "3":
            os.system('cls')
            print("Veure existencias")
            print("-------------------------------")            
            id_Existencia = int(input("Selecciona ID de l'existencias: ")) 
            existencia = next((a for a in existencias if a["id"] == id_Existencia), None)
            if existencia:
                print(f"ID: {existencia['id']}, nombre: {existencia['nombre']}, cantidad: {existencia['cantidad']}, Precio/unidad: {existencia['Precio/unidad']}")
            else:
                print("fuerda de rango")
            input()        
        # Esborrar existencias ##################################
        case "4":
            os.system('cls')
            print("Esborrar existencias")
            print("-------------------------------")
            try:
                id_Existencia = int(input("Selecciona ID que vols eliminar: "))
                # Busquem l'índex de l'element amb l'ID donat
                index = next((i for i, x in enumerate(existencias) if x["id"] == id_Existencia), None)
                
                if index is not None:
                    existencias.pop(index)
                    print("Existència esborrada correctament!")
                else:
                    print("No s'ha trobat cap existència amb aquest ID.")
            except ValueError:
                print("ID no vàlid.")
            input()
        # Editar existencias ##################################
        case "5":
            os.system('cls')
            print("Editar existencias")
            print("-------------------------------")

            selectedName = input("Nombre de la existencia: ")
            for existenciasEjemplo in existencias:
                
                if existenciasEjemplo["nombre"] == selectedName:
                    selectedKey = input("elegir elemento a editar: ")
                    selectedValue = input("Nuevo valor: ")
                    existenciasEjemplo[selectedKey] = selectedValue
                    print("valor actualizado")

            input()

        # Sortir ##################################
        case "0":
            os.system('cls')
            print("Adeu!")

            #Trenquem el bucle infinit
            break

        #Qualsevol altra cosa #####################   
        case _:
            print("\nOpció incorrecta\a")            
            input()
    
    def desar_dades():
        os.system('cls')
        print("Desar a fitxer")
        print("-------------------------------")
        #Introduiu el vostre codi per desar a fitxer aquí
        #????????????????????????????????????????????
        with open(nom_fitxer, "w") as f:
            json.dump(existencias, f, indent=4)