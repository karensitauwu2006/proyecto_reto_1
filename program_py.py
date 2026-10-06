import time
import json
import os  # importacion de librerias

ARCHIVO_USUARIOS_STR = "usuarios.json"
ARCHIVO_CONFIG_STR = "configuraciones.json"  #  archivos de configuracion

AJUSTES_MOTOR_LIST = [  # lista de las configuraciones graficas
    "Límite de FPS",
    "Resolución",
    "Sombras",
    "Trazado de rayos",
    "Brillo",
    "Enfoque de lente"
]


def limpiar():
    os.system("cls")


def cargar_json(archivo_str, por_defecto_dict):
    if not os.path.exists(archivo_str):
        return por_defecto_dict
    with open(archivo_str, "r", encoding="utf-8") as f:
        return json.load(f)


def guardar_json(archivo_str, datos_dict):
    with open(archivo_str, "w", encoding="utf-8") as f:
        json.dump(datos_dict, f, indent=4, ensure_ascii=False)


usuarios_dict = cargar_json(ARCHIVO_USUARIOS_STR, {"karen": "1234"})
configuraciones_dict = cargar_json(ARCHIVO_CONFIG_STR, {})
usuario_actual_str = None
configuracion_dict = None


def registrar(nombre_usuario_str, contraseña_str):
    print("\n" + "=" * 50)
    print("                 REGISTRO DE USUARIO")
    print("=" * 50)

    if nombre_usuario_str in usuarios_dict:
        print("\n[!] El usuario ya está registrado.")  # si el usario esta en el archivo, no registrar
        print("=" * 50)
        return

    usuarios_dict[nombre_usuario_str] = contraseña_str
    guardar_json(ARCHIVO_USUARIOS_STR, usuarios_dict)

    print("\n[OK] Registro exitoso.")
    print(f"[+] Usuario creado: {nombre_usuario_str}")
    print("=" * 50)


def iniciar_sesion(nombre_usuario_str, contraseña_str):
    global usuario_actual_str  # importante hacer global la variable

    print("\n" + "=" * 50)
    print("                 INICIO DE SESIÓN")
    print("=" * 50)

    if nombre_usuario_str not in usuarios_dict:   # si no esta no iniciar sesion
        print("\n[!] El usuario no está registrado.")
        print("=" * 50)
        return

    if usuarios_dict[nombre_usuario_str] != contraseña_str:
        print("\n[!] Contraseña incorrecta.")
        print("=" * 50)
        return

    usuario_actual_str = nombre_usuario_str

    print("\n[OK] Inicio de sesión exitoso.")
    print(f"[+] Bienvenido, {nombre_usuario_str}.")
    print("=" * 50)
