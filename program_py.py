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

#Crear funcion que muestra en pantalla que accedes al configurador del motor
def configurar_motor():
    limpiar()

    print("\n")
    print("=" * 60)
    print("              CONFIGURADOR DEL MOTOR")
    print("=" * 60)

    #Le pedimos al usuario el nombre de su configuracion
    nombre_configuracion_str = input("\nEscribe el nombre para tu configuración: ")

    #Mostramos al usuario las opciones de calidad
    print("\n" + "-" * 60)
    print("              NIVEL DE CALIDAD GRÁFICA")
    print("-" * 60)
    print("  [1] Baja   - Mejor rendimiento")
    print("  [2] Media  - Calidad equilibrada")
    print("  [3] Alta   - Calidad ultra, bajo rendimiento")
    print("-" * 60)

    opcion_usuario_int = 0
    #Bucle para dar a elegir las 3 opciones
    while opcion_usuario_int not in (1, 2, 3):
        opcion_usuario_int = int(input("\nEscribe 1, 2 o 3: "))

    #Aqui se ejecutan los diferentes casos dependiendo la entrada del usuario
    if opcion_usuario_int == 1:
        resultado_dict = {
            "nombre": nombre_configuracion_str,
            "calidad": "baja",
            "resolucion": "720p",
            "fps": 144,
            "sombras": "apagadas",
            "trazado_de_rayos": "apagado",
            "brillo": "apagado",
            "enfoque_de_lente": "apagado"
        }

    elif opcion_usuario_int == 2:
        resultado_dict = {
            "nombre": nombre_configuracion_str,
            "calidad": "media",
            "resolucion": "1080p",
            "fps": 90,
            "sombras": "medias",
            "trazado_de_rayos": "apagado",
            "brillo": "encendido",
            "enfoque_de_lente": "encendido"
        }

    else:
        resultado_dict = {
            "nombre": nombre_configuracion_str,
            "calidad": "alta",
            "resolucion": "4K",
            "fps": 30,
            "sombras": "ultra",
            "trazado_de_rayos": "ultra",
            "brillo": "encendido",
            "enfoque_de_lente": "encendido"
        }
    #Limpiamos panatalla
    limpiar()
    #Muestra al usuario el comienzo de la configuracion
    print("\n" + "=" * 60)
    print("          INICIALIZANDO HERRAMIENTAS GRÁFICAS")
    print("=" * 60)
    #Insertamos retraso para que parezca que carga
    time.sleep(1)
    #Un bucle for para que repase 1 a 1 todas las cargas y muestre al usuario
    for elemento_str in AJUSTES_MOTOR_LIST:
        print(f"  -> Configurando: {elemento_str:<25} [OK]")
        time.sleep(1.5)
    #Se le muestra al usuario
    print("=" * 60)
    print("[OK] Configuración completada correctamente.")
    print("=" * 60)

    return resultado_dict

def mostrar_configuracion(configuracion_dict):  # creamos funcion para mostrar la configuracion
    limpiar()

    print("\n")
    print("=" * 60)
    print("                 CONFIGURACIÓN ACTUAL")
    print("=" * 60)

    if configuracion_dict["calidad"] == "baja":      #ponemos las diferentees opciones de caliad
        print("Calidad:           ▱▱▱▱▱▱▱▱")

    elif configuracion_dict["calidad"] == "media":
        print("Calidad:           ▰▰▰▰▱▱▱▱")

    else:
        print("Calidad:           ▰▰▰▰▰▰▰▰")  #si elige alguna otra opcion no disponible 

    print("-" * 60)
    print(f"Proyecto:          {configuracion_dict['nombre']}")
    print(f"Resolución:        {configuracion_dict['resolucion']}")
    print(f"Límite de FPS:     {configuracion_dict['fps']}")
    print(f"Sombras:            {configuracion_dict['sombras']}")
    print(f"Trazado de rayos:  {configuracion_dict['trazado_de_rayos']}")
    print(f"Brillo:             {configuracion_dict['brillo']}")
    print(f"Enfoque de lente:  {configuracion_dict['enfoque_de_lente']}")
    print("=" * 60)


# ============================================================
#                       SISTEMA PRINCIPAL
# ============================================================

while not usuario_actual_str:
    limpiar()

    print("\n" + "-" * 60)                                 
    print("                    MENÚ PRINCIPAL")
    print("-" * 60)
    print("  [1] Iniciar sesión")
    print("  [2] Registrarse")
    print("  [3] Salir")
    print("-" * 60)

    opcion_str = input("Selecciona una opción: ")            

    if opcion_str == "1":  #opcion para iniciar sesion si el usuario ya tiene cuenta
        nombre_usuario_str = input("usuario: ")
        contraseña_str = input("contraseña: ")

        limpiar()

        iniciar_sesion(
            nombre_usuario_str,
            contraseña_str
        )

    elif opcion_str == "2":  #opcion para registrarse si el usuario no tiene cuenta
        nombre_usuario_str = input("usuario: ")
        contraseña_str = input("contraseña: ")

        limpiar()

        registrar(
            nombre_usuario_str,
            contraseña_str
        )

    elif opcion_str == "3":  #opcion para salir del programa 
        limpiar()                            

        print("\nSaliendo del programa...")
        print("¡Hasta luego!")
        exit()

limpiar()
# Bucle principal del panel de control. Se repetirá hasta que el usuario decida salir
print("\n")
print("=" * 60)
print(f"             SESIÓN ACTIVA: {usuario_actual_str}")
print("=" * 60)

configuracion_dict = configuraciones_dict.get(usuario_actual_str)


while True:
    limpiar()
     # Mostramos las diferentes opciones disponibles en el panel de control
    print("\n" + "-" * 60)
    print("                PANEL DE CONTROL")
    print("-" * 60)
    print("  [1] Configurar motor")
    print("  [2] Mostrar configuración")
    print("  [3] Salir")
    print("-" * 60)
    
     # Pedimos al usuario que seleccione una de las opciones
    opcion_str = input("Selecciona una opción: ")
    
    # Si el usuario selecciona la opcion 1, se crea una nueva configuracion del motor
    if opcion_str == "1":
        configuracion_dict = configurar_motor()
        # Guardamos la configuracion asociada al usuario que tiene la sesion iniciada
        configuraciones_dict[usuario_actual_str] = configuracion_dict
        # Guardamos todas las configuraciones en el archivo JSON
        guardar_json(ARCHIVO_CONFIG_STR, configuraciones_dict)

        print("\n[OK] Configuración guardada correctamente.")

    # Si el usuario selecciona la opcion 2, mostramos su configuracion actual
    elif opcion_str == "2":
        
        # Comprobamos si el usuario todavía no tiene ninguna configuracion creada
        if configuracion_dict is None:
            limpiar()
            print("\n[!] Todavía no hay ninguna configuración.")
        # Si existe una configuracion, la mostramos por pantalla
        else:
            mostrar_configuracion(configuracion_dict)
            input("\nPresiona ENTER para volver al panel...")

    # Si el usuario selecciona la opcion 3, cerramos la sesion y salimos del bucle
    elif opcion_str == "3":
        limpiar()

        print("\n" + "=" * 60)
        print("              CERRANDO SESIÓN...")
        print("=" * 60)

        # Salimos del bucle principal del panel de control
        break