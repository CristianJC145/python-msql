from publicaciones import listarPublicaciones, dibujarPublicaciones

limite = (input("Limite de consulta (Sin limite): "))
busqueda = input("Busqueda (Sin busqueda): ")
ordenar = input("""¿ordenar? 
1. ASC
2. DES: """)
if ordenar:
    campo= input("""ordenar por:
1. ID
2.TITULO
3.PUBLICACION
4.FECHA PUBLICACION
5.NOMBRE USUARIO
6.CANTIDAD DE COMENTARIOS
    """)
if limite:
    pagina = (input("Pagina (Pagina 1): "))
else: 
    pagina = ""

publicaciones = listarPublicaciones(limite=limite, busqueda=busqueda, pagina=pagina, ordenar=ordenar, campo=campo)

dibujarPublicaciones(publicaciones)