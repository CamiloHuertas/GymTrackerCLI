def show_main_menu():
  print("---------------------------------------")
  print("Bienvenido a tu Gym tracker")
  print(" Elije una de las siguientes opciones:")
  print("---------------------------------------")
  print("1. Agregar Workout")
  print("2. Editar Workout")
  print("3. Visualizar Workouts")
  print("4. Eliminar workout")
  print("5. Salir")


# SHOW MENU FUNCTIONS

def show_names_menu(prompt, data):
    print("----------------------------------------------------")
    print(prompt)
    print("----------------------------------------------------")
    for i, workout in enumerate(data):
      print(f"{i + 1}: {workout['name']}")
    print(f"{i + 2}: Volver al menu anterior")


def show_keys_menu(prompt, data):
  print("---------------------------------------------------")
  print(prompt)
  print("---------------------------------------------------")
  for i, key in enumerate(data):
    print(f"{i + 1}: {key}")
  print(f"{i + 2}: Volver al menu anterior")

# SELECT MENU OPTION FUNCTION

def select_menu_option(min_option, max_option):
  while True:
    try:
      option = int(input("Selecciona una de las opciones disponibles: ")) 
      if min_option <= option <= max_option:
        break
      else: 
        print(f"Debe ser de {min_option} a {max_option}")
    except ValueError:
      print("Debes ingresar un numero entero")

  return option

# VALIDATION FUNCTIONS

def is_valid_name(name):
  name = name.strip()
  if not name:
    print("No puede estar vacio")
    return False
  
  for l in name:
    if l.isdigit():
      print("Nombre invalido")
      return False

  return True

def is_valid_integer(number):
  if not number:
    print("No puede estar vacio")
    return False
  
  try:
    if int(number) <= 0:
      print("Debe ser mayor que cero")
      return False
    
  except ValueError:
    print("Debe ser un numero valido y positivo") 
    return False
  return True
  

def is_valid_float(number):
  if not number:
    print("No puede estar vacio")
    return False
  
  try:
    if float(number) <= 0:
      print("Debe ser mayor a cero")
      return False
  
  except ValueError:
    print("No es float")
    return False
  
  return True
  
def is_valid_str(value):
  value = value.strip()

  if not value:
    print("Tienes que ingresar una respuesta! ")
    return False
  
  if value.isdigit():
    print("No puede ser numero")
    return False
  
  if len(value) > 1:
    print("Solo debe contener una letra")
    return False
  
  if value.lower() != "n" and value.lower() != "y":
    print("Debe ser Y o N")
    return False
  
  return True

def no_data_response(data, message):
  if len(data) == 0:
    print(message)
    return True
  return False

# ASK FOR FUNCTIONS
def ask_for_name(prompt):
  value = input(prompt).strip()

  while True:
    if is_valid_name(value):
      return value
    else:
      value = input(prompt)


def ask_for_integer(prompt):
  number = input(prompt)
  while True: 
    if is_valid_integer(number):
      return int(number)
    else:
      number = input(prompt)


def ask_for_float(prompt):
  number = input(prompt)
  while True:
    if is_valid_float(number):
      return float(number)
    else:
      number = input(prompt)



def ask_yes_no(prompt):
  response = input(prompt)
  while True:
    if is_valid_str(response):
      return response.lower()
    else:
      response = input(prompt)


def ask_for_exercises(prompt):
  workout_exercises = []

  while True:
    value = input(prompt).strip()
    if not value:
      return workout_exercises
    elif is_valid_name(value):
      workout_exercises.append({
        "name": value,
        "sets": []
      })

