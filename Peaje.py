'''
Vehiculos $3.5
tractores $16
camiones $12
'''
#los precios de cada vehicculo
veh = 3.5
tra = 16
cam = 12


def calculo(n1,n2):#funcion para calcular el peaje
    resultado = n1 * n2
    return resultado#regreso el valor del resultado para acceder a el fuera de la funcion

opc = int(input("-----Menu-----\n1-Comenzar dia\n2-Salir\n"))
if opc == 1:
    print("---PEAJE DIA DE HOY---")
    x = 0 # conteo vehiculo
    y = 0 #conteo camion
    z = 0 #conteo tractor
    while opc == 1:
        opc1 = int(input("1-Auto\n2-Camion\n3-Tractor\n4-Cerrar Dia\n-Seleccione el vehiculo a cobrar: "))
        if opc1 == 1:
            x += 1#sumo para el conteo de vehiculos
            print("Se le cobrara un peaje de $3.5")
        elif opc1 == 2:
            y += 1 #sumo para el conteo de camiones
            print("Se le cobrara un peaje de $12")
        elif opc1 == 3:
            z += 1 #sumo para el conteo de tractores
            print("Se le cobrara un peaje de $16")
        elif opc1 == 4: #para cerrar el turno y sacar los resultados
            opc2 = input("Seguro que desea terminar el dia?")
            if opc2 == 'si' or 'SI' or 'Si':
                #asigno los resultados de cada calculo en sus respectivas variables
                totalx = calculo(x,veh)#le otorgo los parametros del conteo y de el precio
                totaly = calculo(y,cam)
                totalz= calculo(z,tra)
                #muestro los resultados
                print(f"---CORTE---\n-Numero de vehiculos-\nVehiculos: {x}\nCamiones: {y}\nTractores: {z}\n\n -Recaudado-\nVehiculos: ${totalx}\nCamiones: ${totaly}\nTractores: ${totalz}")
                input("Continuar...")
                opc = 2#para salir del ciclo
        