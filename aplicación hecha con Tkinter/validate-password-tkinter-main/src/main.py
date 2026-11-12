import os
from dotenv import load_dotenv
import tkinter as tk

load_dotenv()

email = os.getenv("EMAIL_USER")
password = os.getenv("PASSWORD_USER")

# === FUNCTIONS ===
def get_user_password():
    """Aquí debe validar el email del usuario y su contraseña"""
    email_ingresado = entry_email.get().strip()
    password_ingresado = entry_password.get()

    if email is None or password is None:
        label_resultado.config(text="No se encontraron las credenciales en el .env", fg="red")
    elif email_ingresado == email and password_ingresado == password:
        label_resultado.config(text="Acceso correcto", fg="green")
    else:
        label_resultado.config(text="Usuario o contraseña incorrectos", fg="red")
        
# === TKINTER ===
ventana = tk.Tk()
ventana.title("Validar contraseñas")
ventana.geometry("300x300")

# == Email ==
label_email = tk.Label(ventana, text="Ingrese su correo electrónico")
label_email.pack()

entry_email = tk.Entry(ventana)
entry_email.pack()

# == Password ==
label_password = tk.Label(ventana, text="Ingrese su contraseña")
label_password.pack()

entry_password = tk.Entry(ventana, show="*")
entry_password.pack()


# == Butón ==
button = tk.Button(ventana, text="Ingresar", command=get_user_password)
button.pack()

# == Resultado ==
label_resultado = tk.Label(ventana, text="")
label_resultado.pack()

ventana.mainloop()