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

#Nom del fitxer on desar/carregar dades
#----------------------------------------
#nom_fitxer = "existencias.json" 
#----------------------------------------
#GUARDEN LA INFORMACIÓ DEL JSON
#dades = json.load("existencias.json")
### menu() ###################################################
#   Aquesta funció mostra el menú d'opcions per pantalla. 
# 
#   Retorna (str): l'opció escollida per l'usuari
##############################################################
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

#Fins a l'infinit (i més enllà)
while True:
    
    #Executem una opció funció del que hagi escollit l'usuari
    match menu():

        # Mostrar existencias ##################################
        case "1":
            os.system('cls')
            print("Mostrar existencias")
            print("-------------------------------")
            
           # for existencias in dades:
           #     print(f"ID: {existencias['id']}")
           #     print(f"Nom: {existencias['nom']}")
           #     print(f"Cognom: {existencias['cognom']}")
            
            #print("[", alumnoPlantilla["id"], "]", alumnoPlantilla["nom"], alumnoPlantilla["cognom"])
        
            #Introduiu el vostre codi per mostrar existencias aquí
            
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
            
            #Introduiu el vostre codi per afegir un existencias aquí
            #DEFINIMOS
            print("Nom de producte") 
            nom_nou = input()
            print("Cantitat") 
            cantitat_nou = input()
            print("preu per unitat")
            preu_nou = input()
            #COMPILAMOS
            nou_existencias = {"id": (len(existencias)+1), "nom" : nom_nou, "cantitat": cantitat_nou, "Precio/unidad": preu_nou}
            #INSERTAMOS
            existencias.append(nou_existencias)
            print("Elemento creado")
        # Veure existencias ##################################
        #ESTO ESTÁ A MEDIAS--------------------------------------------------------------
        case "3":
            os.system('cls')
            print("Veure existencias")
            print("-------------------------------")
            
            #Introduiu el vostre codi per veure un existencias aquí
            print("Selecciona ID de l'existencias") 
            ID = input()
            j = json.dumps(ID)
            print(j)
            print(type(j))
            #SELECCIONAR CON LA ID ALUMNO Y MOSTRARLO------------------------------------------------------------------------


            input()

        # Esborrar existencias ##################################
        case "4":
            os.system('cls')
            print("Esborrar existencias")
            print("-------------------------------")
          
            #Introduiu el vostre codi per esborrar un existencias aquí
            print("Selecciona ID que eliminar") 
            #TAMPOCO FUNCIONA----------------------------------------------------------------------------------------
            existencias.pop(input())
            input()

        # Editar existencias ##################################
        case "5":
            os.system('cls')
            print("Editar existencias")
            print("-------------------------------")
          
            for existenciasEjemplo in existencias:
                print("elegir tabla")
                if existenciasEjemplo["id"] == input():
                    print("elegir elemento a editar y el valor final")
                    existenciasEjemplo[input()] = input()

            #Introduiu el vostre codi per esborrar un existencias aquí
            print("Selecciona ID que editar") 
            existencias.pop(input())
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