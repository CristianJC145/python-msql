from publicaciones import listarPublicaciones, dibujarPublicaciones

limite = (input("Limite de consulta (Sin limite): "))
busqueda = input("Busqueda (Sin busqueda): ")

if limite:
    pagina = (input("Pagina (Pagina 1): "))
else: 
    pagina = ""

publicaciones = listarPublicaciones(limite=limite, busqueda=busqueda, pagina=pagina)

dibujarPublicaciones(publicaciones)