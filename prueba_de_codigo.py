#CREANDO CLASE "MIEMBRO" 

class Member:
    
    #he añadido "__" a los atributos para que estén hecho privados
    
    def __init__(self,name="",seniority="",subordinates="",boss=""):            
        
        self.__name = name           
        self.__seniority = seniority
        self.__subordinates = subordinates
        self.__boss = boss
        
    def __str__(self):
        
        return f"{self.__name}"
    
    # "get" función para accesar los atributos
    
    def get(self,attribute):
        if attribute == "name":
            return (self.__name)
        elif attribute == "seniority":
            return (self.__seniority)
        elif attribute == "subordinates":
            return (self.__subordinates)
        elif attribute == "boss":
            return (self.__boss)
        else:
            print("There is no such attribute.\n")
    
    # "set" función para cambiar los atributos 
    
    def change(self,attribute,new_value):            
        if attribute == "name":
            self.__name = new_value
        elif attribute == "seniority":
            self.__seniority = new_value
        elif attribute == "subordinates":
            self.__subordinates = new_value
        elif attribute == "boss":
            self.__boss = new_value
        else:
            print("There is no such attribute.\n")

#CREANDO CLASE "CARCEL"

class Prison:
    
    def __init__(self):
        self.currently_holding = "No one"
        
    def __str__(self):
        return f"{self.currently_holding} is currently in prison.\n"
    
    #entrar función    
    def put_in_prison(self,member):
        self.currently_holding = member
        print(f"Member {member} has been put in prison.\n")
    #salir función
    def release(self):
        print(f"Member {self.currently_holding} has been released from prison.\n")
        self.currently_holding = "No one"


#CREANDO CLASE "PRINCIPAL"

class Main():
        
        def __init__(self,data_file_path):
        
            #EXTRAYENDO LOS DATOS DESDE ARCHIVO DATOS.JSON 
        
            import json
            import time
        
            with open(data_file_path) as datos:
                dataset = json.load(datos)
        
            #CREANDO LISTA DE MIEMBROS 
            member_list = []
            for member in dataset["members"]:
                member_list.append(Member(member["name"],member["seniority"],member["subordinates"],member["boss"]))
                
            print("Member list has been created.\n")
            time.sleep(3)
            
            #CREANDO UN OBJETO DE CARCEL
            
            prison = Prison()
            
            print("Prison has been created.\n")
            time.sleep(3)
            
            #ENCARCELAR A JHON 
            
            for member in member_list:
                if member.get("name") == "Jhon":
                    prison.put_in_prison(member)
                    break
                else:
                    pass
            
            for member in member_list: #obtener detalles de Jhon
                if member.get("name") == "Jhon":
                    jhon_seniority = member.get("seniority")
                    jhon_subordinates = member.get("subordinates")
                    jhon_boss = member.get("boss")
                    break
                else:
                    pass
            
            for member in member_list:  #quitar a Jhon de la lista de miembros
                if member.get("name") == "Jhon":
                    member_list.remove(member)
                    
                    
            time.sleep(3)
            #REUBICAR LOS SUBORDINADOS DE JHON
            
                
            for member in member_list:       
                
                #revisar si la antigüedad de otros miembros iguala la de Jhon, si lo hace,       
                #redistribuirlos a ese miembro
                
                if member.get("seniority") == jhon_seniority:     
                    member.change("subordinates",member.get("subordinates").extend(jhon_subordinates))
                    break
                    
                #revisar quien tiene la mas antigüedad de los subordinados de Jhon y
                #redistribuir los subordinados a ese miembro 
                
                elif member.get("seniority") == (jhon_seniority - 1) and member.get("name") in jhon_subordinates:
                    member.change("boss",jhon_boss)
                    if member.get("name") in jhon_subordinates:
                        jhon_subordinates.remove(member.get("name"))
                    member.change("subordinates",jhon_subordinates)
                    break
                    
            for member in member_list:  #quitando a Jhon de la lista de subordinados de los otros miembros
                if "Jhon" in member.get("subordinates"):
                    member.change("subordinates",["Carl","Pascual"])
                    break
                    
            for member in member_list:  #quitando a Jhon si es jefe de otro miembro y cambiando jefe de ese miembro
                if "Jhon" == member.get("boss"):
                    member.change("boss","Pascual")
                    break
                    
                    
            print(f"{prison.currently_holding}'s subordinates have been reallocated.\n")
            time.sleep(3)  
                            
                    
            #IMPRIMIENDO UNA TABLA NUEVA DE LA ORGANISACIÓN 
            
            print("The mafia's current structure looks as follows:\n\n")
            print("MEMBER NAME  /  SENIORITY  /     SUBORDINATES     /  MEMBER'S BOSS\n")
            
            member_list = sorted(member_list, key =lambda x: (x.get("seniority"),x.get("subordinates")),reverse = True)
            
            
            for x in member_list:
                print_name = str(x.get("name"))
                print_sen = str(x.get("seniority"))
                print_subs = str(x.get("subordinates"))
                print_boss = str(x.get("boss"))
                print("{:^13}{:^10}{:^30}{:^10}\n".format(print_name,print_sen,print_subs,print_boss))
            print("\n")
            input("Press enter to continue...")
            print("\n" * 100)
            
            #LIBERAR A JHON DEL CÁRCEL  
            
            prison.release()
            time.sleep(3) 
            
            
            #REORGANIZAR LOS SUBORDINADOS 
            
            with open(data_file_path) as datos_new:
                dataset = json.load(datos_new)
            
            member_list = []
            for member in dataset["members"]:
                member_list.append(Member(member["name"],member["seniority"],member["subordinates"],member["boss"]))
            
            
            #IMPRIMIENDO UNA TABLA NUEVA DE LA ORGANISACIÓN   
            
            print("The mafia's current structure looks as follows:\n\n")
            print("MEMBER NAME  /  SENIORITY  /     SUBORDINATES     /  MEMBER'S BOSS\n")
            
            member_list = sorted(member_list, key =lambda x: (x.get("seniority"),x.get("subordinates")),reverse = True)
            
            
            for x in member_list:
                print_name = str(x.get("name"))
                print_sen = str(x.get("seniority"))
                print_subs = str(x.get("subordinates"))
                print_boss = str(x.get("boss"))
                print("{:^13}{:^10}{:^30}{:^10}\n".format(print_name,print_sen,print_subs,print_boss))
            print("\n")
            
            
            #MOSTRANDO EL JEFE DE LA ORGANISACIÓN 
            
            print(f"The current leader of the mafia is {member_list[0]}.\n\n")
            
            input("Press enter to continue...")
            print("\n" * 100)
            
            #---PLUS---
            
            #ENCARCELAR AL JEFE
            
            prison.put_in_prison(member_list[0])
            
            for member in member_list: #obtener los detalles del jefe
                if member.get("name") == "Andy":
                    andy_seniority = member.get("seniority")
                    andy_subordinates = member.get("subordinates")
                    andy_boss = member.get("boss")
                    break
                else:
                    pass
            
            for member in member_list:  #quitar el jefe de la lista de miembros
                if member.get("name") == "Andy":
                    member_list.remove(member)
                    
            time.sleep(3)
            
            #REORGANIZAR LOS SUBORDINADOS
            
            for member in member_list:       
                
                #revisar si la antigüedad de otros miembros iguala la de el jefe, si lo hace,       
                #redistribuirlos a ese miembro
                
                if member.get("seniority") == andy_seniority:     
                    member.change("subordinates",member.get("subordinates").extend(andy_subordinates))
                    break
                    
                #revisar quien tiene la mas antigüedad de los subordinados de el jefe y
                #redistribuir los subordinados a ese miembro 
                
                elif member.get("seniority") == (andy_seniority - 1) and member.get("name") in andy_subordinates:
                    member.change("boss",andy_boss)
                    if member.get("name") in andy_subordinates:
                        andy_subordinates.remove(member.get("name"))
                        andy_subordinates.extend(member.get("subordinates"))
                    member.change("subordinates",andy_subordinates)
                    break
                    
            
            for member in member_list:  #quitando a Jhon si es jefe de otro miembro y cambiando jefe de ese miembro
                if "Andy" == member.get("boss"):
                    member.change("boss","Jhon")
                    break
                    
                    
            print(f"{prison.currently_holding}'s subordinates have been reallocated.\n")
            time.sleep(3)
            
            #IMPRIMIENDO UNA TABLA NUEVA DE LA ORGANISACIÓN
            
            print("The mafia's current structure looks as follows:\n\n")
            print("MEMBER NAME  /  SENIORITY  /     SUBORDINATES     /  MEMBER'S BOSS\n")
            
            member_list = sorted(member_list, key =lambda x: (x.get("seniority"),x.get("subordinates")),reverse = True)
            
            
            for x in member_list:
                print_name = str(x.get("name"))
                print_sen = str(x.get("seniority"))
                print_subs = str(x.get("subordinates"))
                print_boss = str(x.get("boss"))
                print("{:^13}{:^10}{:^30}{:^10}\n".format(print_name,print_sen,print_subs,print_boss))
            print("\n")
            input("Press enter to continue...")
            print("\n" * 100)
            
            #LIBERAR EL JEFE DEL CÁRCEL
            
            prison.release()
            time.sleep(3)
            
            #REORGANIZAR LOS SUBORDINADOS
            
            with open(data_file_path) as datos_new:
                dataset = json.load(datos_new)
            
            member_list = []
            for member in dataset["members"]:
                member_list.append(Member(member["name"],member["seniority"],member["subordinates"],member["boss"]))
            
            #IMPRIMIENDO UNA TABLA NUEVA DE LA ORGANISACIÓN
            
            print("The mafia's current structure looks as follows:\n\n")
            print("MEMBER NAME  /  SENIORITY  /     SUBORDINATES     /  MEMBER'S BOSS\n")
            
            member_list = sorted(member_list, key =lambda x: (x.get("seniority"),x.get("subordinates")),reverse = True)
            
            
            for x in member_list:
                print_name = str(x.get("name"))
                print_sen = str(x.get("seniority"))
                print_subs = str(x.get("subordinates"))
                print_boss = str(x.get("boss"))
                print("{:^13}{:^10}{:^30}{:^10}\n".format(print_name,print_sen,print_subs,print_boss))
            print("\n")
            input("Press enter to end program.")


'''
SCRIPT PRINCIPAL
'''
if __name__ == '__main__':
    prueba_de_codigo = Main("datos.json")


'''
FIN DEL PROGRAMA
'''
