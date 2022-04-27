from math import ceil
import mysql.connector

# Conexion a la base de datos MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port=3306, # Opcional por defecto 3306
    database="blog", # Opcional
)

def listarPublicaciones(limite, busqueda, pagina):
    cursor = db.cursor(dictionary=True)
    pagina_sql= ''
    limit_sql = ''
    busqueda_sql = ''


    if busqueda:
        busqueda_sql = " WHERE publicaciones.titulo LIKE '%"+ busqueda +"%' "


    cursor.execute("SELECT COUNT(*) AS total FROM publicaciones" + busqueda_sql)
    respuesta_total = cursor.fetchone()
    respuesta_str= str(respuesta_total['total'])


    if limite and pagina:
        limite=int(limite)
        pagina=int(pagina)
        numero_pagina = ceil(int(respuesta_str) / int(limite))
        pagina_actual= (int(pagina-1) * int(limite))
        pagina_actual=(str(pagina_actual))
        limite = str(limite)
    elif limite and pagina is None:
        pagina = 1
        pagina_actual = str(pagina)
        numero_pagina = int(respuesta_str)
    else:
        pagina = 1
        pagina_actual = str(pagina)
        numero_pagina = int(respuesta_str)
    print(pagina_actual)
    if limite:
        limit_sql = ' limit ' + pagina_actual

    if pagina and limite:
        pagina_sql =', '+ limite
    else:
        pagina = 1
        numero_pagina=1
    #print("select * from publicaciones" + busqueda_sql +  limit_sql + pagina_sql)
    cursor.execute("""SELECT  `id_publicaciones`, `titulo`, `imagen`, fecha_de_publicacion, `usuarios`.`nombre`
	FROM publicaciones
	INNER JOIN `usuarios` ON `usuarios`.`id_usuarios` = `publicaciones`.`id_usuarios`
    """ + busqueda_sql +  limit_sql + pagina_sql)        
    publicaciones = cursor.fetchall()
    
    
    db.commit()
    cursor.close()
    
    return {
        "total": respuesta_total['total'],
        "data": publicaciones,
        "pagina": pagina,
        "numero_pagina": numero_pagina
    }

def dibujarPublicaciones(datos):
    publicaciones = datos['data']
    
    print('ID    NOMBRE                  TITUTLO                        IMAGEN                                        FECHA_PUBLICACION')
    
    for publicacion in publicaciones:
        print(str(publicacion['id_publicaciones']) + '     ' \
            + publicacion['nombre'] + '     '\
            + publicacion['titulo'] + '    ' \
            + publicacion['imagen'] + '    ' \
            + str(publicacion['fecha_de_publicacion']))
    

    print(str(len(publicaciones)) + ' de '+ str(datos['total']) +' registros encontrados')    
    print("pagina " + str(datos['pagina']) + ' de '+ str(datos['numero_pagina']))



def crearPublicacion():
    pass

def editarPublicacion():
    pass

def eliminarPublicacion():
    pass