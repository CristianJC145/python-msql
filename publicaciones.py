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

def listarPublicaciones(limite, busqueda, pagina, ordenar,campo):
    cursor = db.cursor(dictionary=True)
    contar=' GROUP BY `publicaciones`.`id_publicaciones` '
    campo_sql=''
    ordenar_sql=''
    pagina_sql= ''
    limit_sql = ''
    busqueda_sql = ''


    if busqueda:
        busqueda_sql = " WHERE publicaciones.titulo LIKE '%"+ busqueda +"%' OR `publicaciones`.`id_usuarios` OR `publicaciones`.`fecha_de_publicacion` "

    cursor.execute("SELECT COUNT(*) AS total FROM publicaciones" + busqueda_sql)
    respuesta_total = cursor.fetchone()
    respuesta_str= str(respuesta_total['total'])

    if ordenar and campo:
        ordenar=int(ordenar)
        if ordenar == 1:
            ordenar_sql=' ASC '
        elif ordenar ==2:
            ordenar_sql=' DESC '
    if campo:
        campo=int(campo)
        if campo ==1:
            campo_sql=" ORDER BY `id_publicaciones` "
        elif campo == 2:
            campo_sql=" ORDER BY `titulo` "
        elif campo == 3:
            campo_sql=" ORDER BY `imagen` "
        elif campo == 4:
            campo_sql=" ORDER BY `fecha_publicacion` "
        elif campo == 5:
            campo_sql=" ORDER BY `nombre` "
        elif campo == 6:
            campo_sql=" ORDER BY `cantidad_de_comentarios` "
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
    if limite:
        limit_sql = ' limit ' + pagina_actual

    if pagina and limite:
        pagina_sql =', '+ limite
    else:
        pagina = 1
        numero_pagina=1
    #print("select * from publicaciones" + busqueda_sql +  limit_sql + pagina_sql)
    cursor.execute("""SELECT GROUP_CONCAT(`categorias`.`caracteristicas`)  `id_publicaciones`, `titulo`, `imagen`, fecha_de_publicacion, `usuarios`.`nombre`,
    COUNT(`comentarios`.`id`) AS "CANTIDAD_DE_COMENTARIOS"
	FROM publicaciones
    LEFT JOIN `comentarios` ON `publicaciones`.`id_publicaciones` = `comentarios`.`publicacion_id`
	INNER JOIN `usuarios` ON `usuarios`.`id_usuarios` = `publicaciones`.`id_usuarios`
    INNER JOIN `categoria_publicacion` ON `categoria_publicacion`.`publicacion_id` = `publicaciones`.`id_publicaciones`
	INNER JOIN `categorias` ON `categorias`.`id_categoria` = `categoria_publicacion`.`categoria_id`
    """ + busqueda_sql + contar + campo_sql + ordenar_sql + limit_sql + pagina_sql)        
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
            + str(publicacion['fecha_de_publicacion']) + '    ' \
            + str(publicacion['CANTIDAD_DE_COMENTARIOS'])
            )
    

    print(str(len(publicaciones)) + ' de '+ str(datos['total']) +' registros encontrados')    
    print("pagina " + str(datos['pagina']) + ' de '+ str(datos['numero_pagina']))



def crearPublicacion():
    pass

def editarPublicacion():
    pass

def eliminarPublicacion():
    pass