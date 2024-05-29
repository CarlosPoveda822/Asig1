import sqlite3

conn = sqlite3.connect('recetas.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS recetas (
                    id              INTEGER PRIMARY KEY,
                    nombre          TEXT,
                    ingredientes    TEXT,
                    pasos           TEXT                     
                    )''')
conn.commit()

def agregar_receta(nombre, ingredientes, pasos):
    cursor.execute('''INSERT INTO recetas (nombre, ingredientes, pasos)
                      VALUES (?, ?, ?)''', (nombre, ingredientes, pasos))
    conn.commit()
    print("Receta agregada exitosamente.")

def actualizar_receta(id_receta, nombre, ingredientes, pasos):
    cursor.execute('''UPDATE recetas 
                      SET nombre = ?, ingredientes = ?, pasos = ?
                      WHERE id = ?''', (nombre, ingredientes, pasos, id_receta))
    conn.commit()
    print("Receta actualizada exitosamente.")

def eliminar_receta(id_receta):
    cursor.execute('''DELETE FROM recetas WHERE id = ?''', (id_receta,))
    conn.commit()
    print("Receta eliminada exitosamente.")

def ver_listado_recetas():
    cursor.execute('''SELECT id, nombre FROM recetas''')
    recetas = cursor.fetchall()
    if recetas:
        for receta in recetas:
            print(f"ID: {receta[0]}, Nombre: {receta[1]}")
    else:
        print("No hay recetas en la base de datos.")

def buscar_receta_por_ingredientes(ingredientes):
    cursor.execute('''SELECT * FROM recetas WHERE ingredientes LIKE ?''', ('%'+ingredientes+'%',))
    recetas = cursor.fetchall()
    if recetas:
        for receta in recetas:
            print(f"Nombre: {receta[1]}")
            print(f"Ingredientes: {receta[2]}")
            print(f"Pasos: {receta[3]}")
            print()
    else:
        print("No se encontraron recetas con esos ingredientes.")

def buscar_receta_por_pasos(pasos):
    cursor.execute('''SELECT * FROM recetas WHERE pasos LIKE ?''', ('%'+pasos+'%',))
    recetas = cursor.fetchall()
    if recetas:
        for receta in recetas:
            print(f"Nombre: {receta[1]}")
            print(f"Ingredientes: {receta[2]}")
            print(f"Pasos: {receta[3]}")
            print()
    else:
        print("No se encontraron recetas con esos pasos.")

def main():
    while True:
        print("\n<<<<<<<<<< Menú >>>>>>>>>>")
        print("a) Agregar nueva receta")
        print("b) Actualizar receta existente")
        print("c) Eliminar receta existente")
        print("d) Ver listado de recetas")
        print("e) Buscar recetas por ingredientes")
        print("f) Buscar recetas por pasos")
        print("g) Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == 'a':
            nombre = input("Nombre de la receta: ")
            ingredientes = input("Ingredientes (separados por comas): ")
            pasos = input("Pasos de la receta: ")
            agregar_receta(nombre, ingredientes, pasos)
        elif opcion == 'b':
            id_receta = int(input("ID de la receta a actualizar: "))
            nombre = input("Nuevo nombre de la receta: ")
            ingredientes = input("Nuevos ingredientes (separados por comas): ")
            pasos = input("Nuevos pasos de la receta: ")
            actualizar_receta(id_receta, nombre, ingredientes, pasos)
        elif opcion == 'c':
            id_receta = int(input("ID de la receta a eliminar: "))
            eliminar_receta(id_receta)
        elif opcion == 'd':
            ver_listado_recetas()
        elif opcion == 'e':
            ingredientes = input("Ingrese los ingredientes a buscar: ")
            buscar_receta_por_ingredientes(ingredientes)
        elif opcion == 'f':
            pasos = input("Ingrese los pasos a buscar: ")
            buscar_receta_por_pasos(pasos)
        elif opcion == 'g':
            print("Adios :D")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
