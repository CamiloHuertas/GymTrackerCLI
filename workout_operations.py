import models
import utils
import analytics

# MAIN FUNCTIONS
def add_workout(data):
  workout_name = utils.ask_for_name("Ingresa el nombre del Workout: ")
  workout_exercises = utils.ask_for_exercises("Ingresa los ejercicios: ")

  new_workout = models.Workout(workout_name, workout_exercises)
  data['workouts'].append(new_workout.to_dict())


def edit_workout(data):
  if utils.no_data_response(data, "No tienes ningun workout para editar"):
    return

  utils.show_names_menu("Que workout quieres editar?: ", data)
  selected_workout = select_item_from_list(data)
  edit_selected_workout(selected_workout)
  

def visualize_workouts(data):
  if utils.no_data_response(data, "No tienes ningun workout para visualizar"):
    return

  utils.show_names_menu("Cual workout quieres visualizar?: ", data)
  workout_to_visualize = select_item_from_list(data)
  display_workout_visualization(workout_to_visualize)
 

def delete_whole_workout(data):
  if utils.no_data_response(data, "No tienes ningun workout para eliminar"):
    return

  utils.show_names_menu("Cual Workout completo quieres eliminar?: ", data)
  option = utils.select_menu_option(len(data))

  confirm = utils.ask_yes_no("Seguro quieres eliminar este workout? ")
  if confirm == 'y':
    data.pop(option - 1)
    print("Workout eliminado")
  else:
    print("Cancelando...")
    return
  

# SECONDARY FUNCTIONS

def edit_selected_workout(selected_workout):
  utils.show_keys_menu("Que dato quieres editar?: ", selected_workout)
  option = utils.select_menu_option(2)
  
  if option == 1:
    edit_workout_name(selected_workout)
  else:
    edit_exercises(selected_workout)


def display_workout_visualization(workout_to_visualize):
  workout_name = workout_to_visualize['name']
  workout_exercises = workout_to_visualize['exercises']
  
  if len(workout_exercises) == 0:
    print(f"No tienes ejercicios para visualizar del siguiente workout: {workout_name}")
    return
  
  print("----------------------------------------------")
  print(f"Estas visualizando el workout: {workout_name}")
  print("----------------------------------------------")
  for item in workout_exercises:
    print(f"Ejercicio: {item['name']}")
    print(" Sets: ")
    
    if len(item['sets']) == 0:
      print("   No tienes sets para este ejercicio")
      print()
    else:
      for i, exercise_set in enumerate(item['sets']):
        set_volume = analytics.calculate_set_volume(exercise_set)
        print(f"  {i + 1}:reps: {exercise_set['reps']} - peso: {exercise_set['peso']}kg - volume: {set_volume}kg")

      exercise_volume = analytics.calculate_exercise_volume(item)
      print(f"        Volumen total del ejercicio: {exercise_volume}kg")
      print()

  workout_volume = analytics.calculate_workout_volume(workout_exercises)
  print("-------------------------------------------------------")
  print(f"      Volumen total del workout: {workout_volume}kg")
  print("-------------------------------------------------------")
  print()
  print()
      

# FUNCTIONS TO EDIT THE EXERCISES NAMES AND ADD NEW EXERCISES
def edit_exercises(selected_workout):
  print("Que quieres hacer con tus exercises?: ")
  print("1. Editar exercises existentes")
  print("2. Agregar un nuevo exercise")
  print("3. Eliminar un exercise")
  option = utils.select_menu_option(3)

  if option == 1:
    edit_existent_exercise(selected_workout)
  elif option == 2:
    add_new_exercises(selected_workout)
  else:
    delete_exercise(selected_workout)



def add_new_exercises(data):
  current_item_exercises_list = data['exercises']
  new_exercises = utils.ask_for_exercises("Ingresa los ejercicios a agregar: ")
  for exercise in new_exercises:
    current_item_exercises_list.append(exercise)


def edit_existent_exercise(selected_workout):
    if len(selected_workout['exercises']) > 0:
      utils.show_names_menu("Que ejercicio quieres editar?: ", selected_workout['exercises'])
      exercise_to_edit = select_item_from_list(selected_workout['exercises'])
      edit_selected_existent_exercise(exercise_to_edit)
    else:
      print("No tienes ejercicios que editar: ")
      
def delete_exercise(selected_workout):
  current_exercises = selected_workout['exercises']
  if len(current_exercises) == 0:
    print("No tienes ejercicios a eliminar")
    return
  else:
    print("Cual ejercicio quieres eliminar?: ")
    for i, exercise in enumerate(current_exercises):
      print(f"{i + 1}: {exercise['name']}")
    index_to_delete = utils.select_menu_option(len(current_exercises))
    exercise_name = current_exercises[index_to_delete -1]['name']

    confirm_delete = utils.ask_yes_no(f"Seguro quieres eliminar este ejercicio ({exercise_name})? ")
    if confirm_delete == 'y':
      current_exercises.pop(index_to_delete - 1)
    else:
      return


# COORDINATING FUNCTION

def edit_selected_existent_exercise(exercise_to_edit):
  utils.show_keys_menu("Que dato quieres editar del ejercicio?: ", exercise_to_edit)
  option = utils.select_menu_option(len(exercise_to_edit))
  if option == 1:
    edit_exercise_name(exercise_to_edit)
  else:
    edit_exercise_sets(exercise_to_edit)

# FUNCTION TO EDIT EXERCISES SETS
def edit_exercise_sets(exercise_to_edit):
  print("Que quieres hacer con los sets ?: ")
  print("1. Agregar un nuevo set")
  print("2. Editar un set existente")
  print("3. Eliminar un set existente")
  option = utils.select_menu_option(3)
  if option == 1:
    add_new_set(exercise_to_edit)
  elif option == 2:
    edit_existent_set(exercise_to_edit)
  else:
    delete_existent_set(exercise_to_edit)

def add_new_set(exercise_to_edit):
  while True:
    reps = utils.ask_for_integer("Ingresa la cantidad de reps: ")
    peso = utils.ask_for_float("Ingresa la cantidad de peso usado (en kg):")

    new_set = models.ExerciseSet(reps, peso)
    exercise_to_edit['sets'].append(new_set.to_dict())

    response = utils.ask_yes_no("Y para agregar | N para salir: ")

    if response == "n":
      break


def edit_existent_set(exercise_to_edit):
  existent_sets = exercise_to_edit['sets']
  if len(existent_sets) == 0:
    print("No tienes sets para editar en este ejercicio")
  else:
    print("Cual de estos sets quieres editar?: ")
    for i, exercise_set in enumerate(existent_sets):
      print(f"{i + 1}. Set | reps: {exercise_set['reps']} - peso: {exercise_set['peso']}kg")
    set_to_edit = select_item_from_list(existent_sets)
    utils.show_keys_menu("Que quieres cambiar de este set?: ", set_to_edit)
    option = utils.select_menu_option(len(set_to_edit))

    if option == 1:
      edit_set_reps(set_to_edit)
    else:
      edit_set_weight(set_to_edit)


def delete_existent_set(exercise_to_edit):
  exercise_sets = exercise_to_edit['sets']

  if len(exercise_sets) == 0:
    print("No tienes ningun set en este ejercicio")
    return
  
  print("Cual set quieres eliminar?: ")

  for i, single_set in enumerate(exercise_sets):
    print(f"{i + 1}: reps: {single_set['reps']} | peso:{single_set['peso']}")
  
  option = utils.select_menu_option(len(exercise_sets))
  confirm_delete = utils.ask_yes_no("Seguro quieres eliminar ese set?: ")

  if confirm_delete == 'y':
    exercise_sets.pop(option - 1)
    print("Eliminado con exito")
  else:
    print("Eliminacion cancelada")
    return


# HELPER FUNCTIONS
def edit_workout_name(selected_workout):
  selected_workout['name'] = utils.ask_for_name("Nuevo nombre del Workout: ")

def edit_exercise_name(selected_exercise):
  selected_exercise['name'] = utils.ask_for_name("Ingresa el nuevo nombre del ejercicio: ")

def edit_set_reps(selected_set):
  selected_set['reps'] = utils.ask_for_integer("Cuantas reps?: ")

def edit_set_weight(selected_set):
  selected_set['peso'] = utils.ask_for_float("Cuanto peso?: ")


def select_item_from_list(data):
  chosen_edit_option = utils.select_menu_option(len(data))
  item_to_edit = data[chosen_edit_option - 1]
  return item_to_edit