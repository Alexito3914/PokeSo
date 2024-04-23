import tkinter as tk
from tkinter import messagebox
import os
import subprocess

def reescalar_imagen(ruta, width, height):
    imagen_original = tk.PhotoImage(file=ruta)
    imagen_reescalada = imagen_original.subsample(imagen_original.width() // width, imagen_original.height() // height)
    return imagen_reescalada

def terminal():
    ruta_script = "./launcher.sh"  # Ruta al archivo de Bash que deseas ejecutar
    subprocess.run(['bash', '-c', f'chmod +x {ruta_script} && ./{ruta_script}'])
    return "Se ejecuto la terminal"

def tresenraya():
    ruta_script = "./launcher2.sh"
    subprocess.run(['bash', '-c', f'chmod +x {ruta_script} && ./{ruta_script}'])
    return "Se ejecuto el tres en raya"
def nano():
    ruta_script = "./launchernano.sh"
    subprocess.run(['bash', '-c', f'chmod +x {ruta_script} && ./{ruta_script}'])
    return "Se ejecuto el nano"
def archivos():
    ruta_script = "./launcherarchivos.sh"
    subprocess.run(['bash', '-c', f'chmod +x {ruta_script} && ./{ruta_script}'])
    return "Se ejecuto el explorador de archivos"
def escritorio():
    escritorio = tk.Tk()
    escritorio.title("PokeSO")
    escritorio.geometry(f"{escritorio.winfo_screenwidth()}x{escritorio.winfo_screenheight()}")
    #DEFINIR TAMANIO DE CADA ICONO
    tamanio_app_en_x = int(0.07*escritorio.winfo_screenheight())
    tamanio_app_en_y = int(0.07*escritorio.winfo_screenheight())
    
    ruta_fondo_escritorio = "Fondo2.png"
    fondo_escritorio = reescalar_imagen(ruta_fondo_escritorio, escritorio.winfo_screenwidth(), escritorio.winfo_screenheight())

    label_fondo = tk.Label(escritorio, image=fondo_escritorio)
    label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
    color_fondo = escritorio.cget("background")
    #TERMINAL
    icono_terminal = reescalar_imagen("Ultraball.png",tamanio_app_en_x, tamanio_app_en_y)
    boton_terminal = tk.Button(escritorio, image=icono_terminal, compound=tk.BOTTOM, borderwidth=0, highlightthickness=0, bd=0, bg=color_fondo)
    boton_terminal.configure(activebackground=color_fondo, command=terminal)
    boton_terminal.pack(side="top", anchor="nw")
    #NAVEGADOR ARCHIVOS
    icono_navegador_archivos = reescalar_imagen("Superball.png", tamanio_app_en_x, tamanio_app_en_y)
    boton_navegador_archivos = tk.Button(escritorio, image=icono_navegador_archivos, compound=tk.BOTTOM, borderwidth=0, highlightthickness=0, bd=0, bg=color_fondo, command=archivos)
    boton_navegador_archivos.pack(side="top", anchor="nw")
    #TRES EN RAYA
    icono_3_en_raya = reescalar_imagen("Tresraya.png", tamanio_app_en_x, tamanio_app_en_y)
    boton_3_en_raya = tk.Button(escritorio, image=icono_3_en_raya, compound=tk.BOTTOM, borderwidth=0, highlightthickness=0, bd=0, bg=color_fondo, command=tresenraya)
    boton_3_en_raya.pack(side="top", anchor="nw")
    #NANO
    icono_editor_texto = reescalar_imagen("Nano.png", tamanio_app_en_x, tamanio_app_en_y)
    boton_nano = tk.Button(escritorio, image=icono_editor_texto, compound=tk.BOTTOM, borderwidth=0, highlightthickness=0, command=nano, bd=0, bg=color_fondo)
    boton_nano.pack(side="top", anchor="nw")
    #SALIDA
    icono_salida = reescalar_imagen("Pokeball1.png", tamanio_app_en_x, tamanio_app_en_y)
    boton_salida = tk.Button(escritorio, image=icono_salida, compound=tk.BOTTOM, borderwidth=0, highlightthickness=0, command=escritorio.quit, bd=0, bg=color_fondo)
    boton_salida.pack(side="top", anchor="nw")
    
    return escritorio.mainloop()

escritorio()
