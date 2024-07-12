import tkinter as tk
from tkinter import Scrollbar, Listbox, END, Entry, Button, Toplevel, Text, messagebox
import requests

# Configuración de API de juegos
url_base_juegos = 'https://api.rawg.io/api/games'
api_key_juegos = 'd07a038f2ab3445bbc3bb89c66ac426d'

# Configuración de API de recetas
BASE_URL_RECETAS = 'https://www.themealdb.com/api/json/v2/1/'

# Función para obtener juegos mejor calificados
def obtener_juegos_mejor_calificados(max_results=10):
    try:
        parametros = {
            'key': api_key_juegos,
            'ordering': '-rating',
            'page_size': max_results
        }
        response = requests.get(url_base_juegos, params=parametros)
        response.raise_for_status()
        juegos = response.json().get('results', [])
        return juegos
    except requests.exceptions.RequestException as e:
        print(f'Error al obtener juegos mejor calificados: {e}')
        return []

# Función para obtener juegos por categoría
def obtener_juegos_por_categoria(categoria, max_results=10):
    try:
        parametros = {
            'key': api_key_juegos,
            'genres': categoria,
            'ordering': '-rating',
            'page_size': max_results
        }
        response = requests.get(url_base_juegos, params=parametros)
        response.raise_for_status()
        juegos = response.json().get('results', [])
        return juegos
    except requests.exceptions.RequestException as e:
        print(f'Error al obtener juegos por categoría: {e}')
        return []

# Función para mostrar juegos en el área de texto
def mostrar_juegos(juegos, text_area):
    text_area.delete(1.0, tk.END)
    for juego in juegos:
        text_area.insert(tk.END, f"Nombre: {juego.get('name')}\n")
        text_area.insert(tk.END, f"Descripción: {juego.get('description', 'No hay descripción disponible')}\n")
        categorias = ', '.join([genre['name'] for genre in juego.get('genres', [])])
        text_area.insert(tk.END, f"Categorías: {categorias}\n")
        text_area.insert(tk.END, f"Calificación: {juego.get('rating', 'No hay calificación')}\n")
        text_area.insert(tk.END, "-" * 30 + "\n")

# Función para obtener recetas populares
def obtener_recetas_populares():
    url = f'{BASE_URL_RECETAS}latest.php'
    try:
        response = requests.get(url)
        response.raise_for_status()
        if response.status_code == 200:
            return response.json().get('meals', [])
        else:
            print(f"Error al obtener recetas populares: {response.status_code}")
            return []
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")
        return []

# Función para mostrar recetas en la GUI
def mostrar_recetas_en_gui(recetas):
    root_recetas = Toplevel()
    root_recetas.title("Recetas de Comida")

    messagebox.showinfo("Instrucciones de Recetas", "En esta sección puedes ver las recetas populares.\n"
                                                     "Selecciona una receta de la lista para ver los ingredientes e instrucciones.\n"
                                                     "También puedes buscar recetas por ingredientes ingresando el nombre del ingrediente y presionando 'Buscar'.\n\n"
                                                     "Para volver al menú principal, simplemente cierra esta ventana.")

    scrollbar = Scrollbar(root_recetas)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    listbox = Listbox(root_recetas, yscrollcommand=scrollbar.set, width=60, height=20)
    listbox.pack(pady=10)

    for receta in recetas:
        nombre = receta.get('strMeal', 'Nombre Desconocido')
        listbox.insert(END, nombre)

    scrollbar.config(command=listbox.yview)

    entry_ingrediente = Entry(root_recetas, width=40)
    entry_ingrediente.pack(pady=10)

    def buscar_por_ingrediente():
        ingrediente = entry_ingrediente.get()
        if ingrediente:
            recetas_encontradas = buscar_recetas_por_ingrediente(ingrediente)
            if recetas_encontradas is not None:
                listbox.delete(0, END)
                for receta in recetas_encontradas:
                    nombre = receta.get('strMeal', 'Nombre Desconocido')
                    listbox.insert(END, nombre)
            else:
                messagebox.showinfo("Sin Resultados", "No se encontraron recetas con ese ingrediente.")

    btn_buscar = Button(root_recetas, text="Buscar por Ingrediente", command=buscar_por_ingrediente)
    btn_buscar.pack()

    def mostrar_ingredientes_instrucciones(event):
        seleccion = listbox.curselection()
        if seleccion:
            indice = seleccion[0]
            receta = recetas[indice]
            receta_detalle = obtener_detalle_receta(receta['idMeal'])
            if receta_detalle:
                ingredientes = obtener_ingredientes(receta_detalle)
                instrucciones = receta_detalle.get('strInstructions', 'No hay instrucciones disponibles.')
                mostrar_ventana_ingredientes_instrucciones(receta['strMeal'], ingredientes, instrucciones)

    listbox.bind('<<ListboxSelect>>', mostrar_ingredientes_instrucciones)

    # Botón para cerrar la ventana de recetas y volver al menú principal
    boton_volver = tk.Button(root_recetas, text="Volver al Menú Principal", command=lambda: [root_recetas.destroy(), main()])
    boton_volver.pack(pady=10)

    root_recetas.mainloop()

# Función para buscar recetas por ingrediente
def buscar_recetas_por_ingrediente(ingrediente):
    url = f'{BASE_URL_RECETAS}filter.php'
    parametros = {'i': ingrediente}
    try:
        response = requests.get(url, params=parametros)
        response.raise_for_status()
        if response.status_code == 200:
            return response.json().get('meals', [])
        else:
            print(f"Error al buscar recetas por ingrediente: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")
        return None

# Función para obtener el detalle de una receta
def obtener_detalle_receta(id_receta):
    url = f'{BASE_URL_RECETAS}lookup.php'
    parametros = {'i': id_receta}
    try:
        response = requests.get(url, params=parametros)
        response.raise_for_status()
        if response.status_code == 200:
            return response.json().get('meals', [])[0]
        else:
            print(f"Error al obtener detalle de la receta: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")
        return None

# Función para obtener los ingredientes de una receta
def obtener_ingredientes(receta):
    ingredientes = []
    for i in range(1, 21):
        ingrediente = receta.get(f'strIngredient{i}')
        medida = receta.get(f'strMeasure{i}')
        if ingrediente and ingrediente.strip():
            ingredientes.append(f"{ingrediente} - {medida}")
    return ingredientes

# Función para mostrar ventana con ingredientes e instrucciones
def mostrar_ventana_ingredientes_instrucciones(nombre_receta, ingredientes, instrucciones):
    ventana = Toplevel()
    ventana.title(f"Detalles de {nombre_receta}")

    text_area = Text(ventana, wrap=tk.WORD)
    text_area.pack(expand=True, fill='both')

    text_area.insert(END, f"Ingredientes:\n")
    for ingrediente in ingredientes:
        text_area.insert(END, f"{ingrediente}\n")

    text_area.insert(END, "\nInstrucciones:\n")
    text_area.insert(END, instrucciones)

# Función principal para mostrar la ventana principal
def main():
    root = tk.Tk()
    root.title("Sistema de Recomendación")

    messagebox.showinfo("Bienvenido", "Bienvenido al Sistema de Recomendación.\n\n"
                                      "Para comenzar, puedes seleccionar una de las siguientes opciones:\n"
                                      "- 'Mostrar Juegos Mejor Calificados': Muestra los juegos mejor calificados.\n"
                                      "- 'Mostrar Recetas Populares': Muestra las recetas populares.\n"
                                      "- 'Salir': Cierra la aplicación.")

    # Función para mostrar la interfaz de juegos
    def mostrar_interfaz_juegos():
        root.withdraw()
        root_juegos = Toplevel()
        root_juegos.title("Sistema de Recomendación de Juegos")
        root_juegos.geometry('600x600')

        messagebox.showinfo("Instrucciones de Juegos", "En esta sección puedes ver los juegos mejor calificados.\n"
                                                       "También puedes buscar juegos por categoría ingresando el nombre de la categoría y presionando 'Buscar'.\n\n"
                                                       "Para volver al menú principal, simplemente cierra esta ventana.")

        text_area = tk.Text(root_juegos, wrap=tk.WORD)
        text_area.pack(expand=True, fill='both')

        frame_categoria = tk.Frame(root_juegos)
        frame_categoria.pack(pady=10)
        etiqueta_categoria = tk.Label(frame_categoria, text="Buscar por Categoría:")
        etiqueta_categoria.pack(side=tk.LEFT)
        entrada_categoria = tk.Entry(frame_categoria)
        entrada_categoria.pack(side=tk.LEFT, padx=5)
        boton_buscar = tk.Button(frame_categoria, text="Buscar", command=buscar_por_categoria)
        boton_buscar.pack(side=tk.LEFT)

        juegos_mejor_calificados = obtener_juegos_mejor_calificados()
        if juegos_mejor_calificados:
            mostrar_juegos(juegos_mejor_calificados, text_area)
        else:
            messagebox.showerror("Error", "No se pudo obtener la lista de juegos mejor calificados.")

        # Botón para volver al menú principal
        boton_volver = tk.Button(root_juegos, text="Volver al Menú Principal", command=lambda: [root_juegos.destroy(), main()])
        boton_volver.pack(pady=10)

    # Función para buscar juegos por categoría
    def buscar_por_categoria():
        categoria = entrada_categoria.get().strip().lower()
        if categoria:
            juegos_categoria = obtener_juegos_por_categoria(categoria)
            if juegos_categoria:
                mostrar_juegos(juegos_categoria, text_area)
            else:
                messagebox.showinfo("Sin Resultados", f"No se encontraron juegos en la categoría '{categoria}'.")
        else:
            messagebox.showwarning("Campo Vacío", "Por favor ingrese una categoría.")

    # Función para mostrar la interfaz de recetas
    def mostrar_interfaz_recetas():
        root.withdraw()
        recetas_populares = obtener_recetas_populares()
        if recetas_populares:
            mostrar_recetas_en_gui(recetas_populares)
        else:
            messagebox.showerror("Error", "No se pudo obtener la lista de recetas populares.")

    # Botones del menú principal
    boton_juegos = tk.Button(root, text="Mostrar Juegos Mejor Calificados", command=mostrar_interfaz_juegos)
    boton_juegos.pack(pady=10)

    boton_recetas = tk.Button(root, text="Mostrar Recetas Populares", command=mostrar_interfaz_recetas)
    boton_recetas.pack(pady=10)

    boton_salir = tk.Button(root, text="Salir", command=root.quit)
    boton_salir.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
