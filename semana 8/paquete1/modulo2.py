from ast import NotIn
#Diccionario para almacenar los datos del usuario
datos = {}

#Funcion para registrar los datos
def registrar():
  print("Hola! Crea un usuario y contraseña que usarás en el futuro para ingresar al programa.")
  usuario = input("Ingresa tu nombre de usuario:")
  contrasena = input("Ingresa tu contraseña:")
  datos[usuario] = contrasena
  print("Usuario registrado exitosamente.")

#Funcion para mostrar los datos registrados
def leer():
  print("Usuarios registrados:")
  for us, contra in datos.items():
      print(f"Usuario: {us} | Contraseña: {contra}")

#Funcion para ingresar al sistema
def login():
  print("Hola! Ingresa tu usuario y contraseña para ingresar al sistema!")
  uslogin = input("Ingresa tu nombre de usuario")
  if uslogin not in datos:
    print("Usuario no encontrado.")
  contralogin = input("Ingresa tu contraseña:")
  if contralogin == datos[uslogin]:
    print("Inicio de sesión exitoso! Bienvenido al programa.")
  else:
    print("Contraseña incorrecta.")

registrar()
leer()
login()