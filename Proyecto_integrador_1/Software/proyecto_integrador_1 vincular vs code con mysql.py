
import mysql.connector
midb = mysql.connector.connect(
 host="localhost",
 user="root",
 password="Prueba!123",
 database="Proyectointegradorv01"
)
print(midb)

def insertar_Producto(self, iD, modelo, numero_serie, direccion_instalacion, coordenadas, estado):
    if self.conexion.is_connected():
        try:
            cursor = self.conexion.cursor()
            senteciaSQL="INSERT INTO dispositivos_iot values('01_Luz','Phillips_Hue','L00001', 'Cerro Colorado 1458','(51° 30’ 30’’ N; 0° 7’ 32’’ O)','En proceso')"
            data = (dispositivos_iot.getiD(),
                    dispositivos_iot.getmodelo(),
                    dispositivos_iot.numero_serie(),
                    dispositivos_iot.direccion_instalacion(),
                    dispositivos_iot.coordenadas(),
                    dispositivos_iot.getestado(),
                    )
            
            cursor.execute(sentenciaSQL,data)
            cursor.Conexion.commit()
            cursor.Conexion.close()   
            print("Producto insertado correctamente")

        except mysql.connector.Error as descripcionDelError:
            print("¡Hubo un error al intentar conctar la Base de Datos", descripcionDelError)



