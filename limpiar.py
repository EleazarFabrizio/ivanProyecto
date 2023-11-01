import tkinter as tk

# Función para crear y mostrar un Toplevel
def show_toplevel():
    toplevel = tk.Toplevel(root)
    toplevel.title("Toplevel Window")
    label = tk.Label(toplevel, text="Esta es una ventana Toplevel")
    label.pack()

# Crear la ventana principal
root = tk.Tk()

# Configurar la ventana principal en modo de pantalla completa
root.attributes('-fullscreen', True)

# Configurar un botón para mostrar el Toplevel
button = tk.Button(root, text="Mostrar Toplevel", command=show_toplevel)
button.pack()

# Iniciar el bucle principal de la aplicación
root.mainloop()