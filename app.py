from classes.nombre import Get_user
from classes.fecha import Get_posts

def main():

    while True:
        
        menu = str(input("Que desea hacer? \n" + 
        "1. Get Usuario\n" + 
        "2. Get Post \n" + 
        "3. Salir\n" +
        ">> "
        ))
        
        if(menu == "1"):
            user = str(input("Ingrese username de la cuenta que desea buscar: "))
            req = Get_user(user)
            req.getAccountInfo()
            req.displayData()

        elif(menu == "2"):

            user = str(input("Ingrese username de la cuenta que desea buscar: "))
            fecha_ini = str(input("Año inicial en formato (aaaa-m-d)\n")) #2019-01-01
            fecha_fin = str(input("Año final en formato (aaaa-m-d)\n")) #2020-12-31

            req = Get_posts( user, fecha_ini, fecha_fin )
            req.getAccountPosts()
            req.displayData()
            
        elif(menu == "3"):
            break
        else:
            print("\n Dato no valido!!!!")
            print("\n")

    pass

if __name__ == "__main__":

    main()