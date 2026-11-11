import os
import tkinter as tk

from dotenv import load_dotenv

load_dotenv()


def capturar_credenciales(entry_usuario, entry_password):
    Usuario = entry_usuario.get().strip()
    Password = entry_password.get()
    return Usuario, Password


def validar_credenciales(usuario, password):
    EMAIL_USER = os.getenv("EMAIL_USER") 
    PASSWORD_USER = os.getenv("PASSWORD_USER")

    if EMAIL_USER is None or PASSWORD_USER is None:
        return False

    return usuario == EMAIL_USER and password == PASSWORD_USER


def mostrar_mensaje(label_resultado, es_correcto):
    if es_correcto:
        label_resultado.config(text="Acceso correcto", fg="green",)
    else:
        label_resultado.config(text="Usuario o contraseña incorrectos", fg="red") 
        return ("Usuario")


def iniciar_sesion(entry_usuario, entry_password, label_resultado):
    usuario, password = capturar_credenciales(entry_usuario, entry_password)
    es_correcto = validar_credenciales(usuario, password)
    mostrar_mensaje(label_resultado, es_correcto)


def main():
    ventana = tk.Tk()
    ventana.title("Validar credenciales")
    ventana.geometry("360x260")
    ventana.resizable(False, False)

    tk.Label(ventana, text="Usuario:").pack(pady=(20, 2))
    entry_usuario = tk.Entry(ventana, width=30)
    entry_usuario.pack()

    tk.Label(ventana, text="Contraseña:").pack(pady=(12, 2))
    entry_password = tk.Entry(ventana, width=30, show="*")
    entry_password.pack()

    label_resultado = tk.Label(ventana, text="", font=("Arial", 11, "bold"))
    
    
    tk.Button(
        ventana,
        text="Ingresar",
        width=15,
        command=lambda: iniciar_sesion(entry_usuario, entry_password, label_resultado),
    ).pack(pady=18)

    label_resultado.pack()

    ventana.mainloop()


if __name__ == "__main__":
    main()
