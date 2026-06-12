import models
import utils
import analytics
import storage

# MAIN FUNCTIONS
def add_workout(data, save):
  print("--------------------------------------------------------")
  workout_name = utils.ask_for_name("Ingresa el nombre del Workout: ")
  confirm_ask_exercises = utils.ask_yes_no("Quieres ingresar ejercicios? (Y | N): ")

  if confirm_ask_exercises == 'y':
    workout_exercises = utils.ask_for_exercises("Ingresa los ejercicios (nada para salir): ")
  else:
    workout_exercises = []
  
  new_workout = models.Workout(workout_name, workout_exercises)
  data.append(new_workout.to_dict())
  print(f"Workout '{workout_name}' ha sido creado con exito!")
  save()
  return

def edit_workout(data, save):
  while True:
    if utils.no_data_response(data, "No tienes ningun workout para editar"):
      return
    
    utils.show_names_menu("Que workout quieres editar?: ", data)
    selected_workout = select_item_from_list(data)

    if selected_workout == 'v':
      print("volviendo al menu principal...")
      return

    edit_selected_workout(selected_workout, save)
  

def visualize_workouts(data):
  if utils.no_data_response(data, "No tienes ningun workout para visualizar"):
    return

  utils.show_names_menu("Cual workout quieres visualizar?: ", data)
  workout_to_visualize = select_item_from_list(data)

  if workout_to_visualize == 'v':
    print("volviendo al menu principal...")
    return 
  
  display_workout_visualization(workout_to_visualize)
 

def delete_whole_workout(data, save):
  if utils.no_data_response(data, "No tienes ningun workout para eliminar"):
    return
  while True:
    utils.show_names_menu("Cual Workout completo quieres eliminar?: ", data)
    option = utils.select_menu_option(1, len(data) + 1)

    if option == len(data) + 1:
      print("volviendo al menu principal...")
      return


    confirm = utils.ask_yes_no("Seguro quieres eliminar este workout? (Y | N) ")
    if confirm == 'y':
      data.pop(option - 1)
      print("Workout eliminado")
      save()
      return
    else:
      print("Cancelando...")
      continue
  

# SECONDARY FUNCTIONS

def edit_selected_workout(selected_workout, save):
  while True:
    utils.show_keys_menu(f"Que dato quieres editar del workout '{selected_workout['name']}'?: ", selected_workout)
    option = utils.select_menu_option(1, 3)

    if option == 3:
      print("volviendo al menu anterior ")
      return
    
    if option == 1:
      edit_workout_name(selected_workout, save)
    else:
      edit_exercises(selected_workout, save)


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
        print(f"  {i + 1}:reps: {exercise_set['reps']} - weight: {exercise_set['weight']}kg - volume: {set_volume}kg")

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
def edit_exercises(selected_workout,save):
  while True:
    print("-------------------------------------------------------")
    print("Que quieres hacer con tus exercises?: ")
    print("-------------------------------------------------------")
    print("1. Editar exercises existentes")
    print("2. Agregar un nuevo exercise")
    print("3. Eliminar un exercise")
    print("4. Volver al menu anterior")
    option = utils.select_menu_option(1, 4)

    if option == 1:
      edit_existent_exercise(selected_workout, save)
    elif option == 2:
      add_new_exercises(selected_workout, save)
    elif option == 3:
      delete_exercise(selected_workout , save)
    else:
      return


def edit_existent_exercise(selected_workout, save):
    while True:
      if len(selected_workout['exercises']) > 0:
        utils.show_names_menu("Que ejercicio quieres editar?: ", selected_workout['exercises'])
        exercise_to_edit = select_item_from_list(selected_workout['exercises'])

        if exercise_to_edit == 'v':
          print("volviendo al menu anterior...")
          return

        edit_selected_existent_exercise(exercise_to_edit, save)
      else:
        print("No tienes ejercicios que editar")
        return
    

def add_new_exercises(data, save):
  current_item_exercises_list = data['exercises']
  new_exercises = utils.ask_for_exercises("Ingresa los ejercicios a agregar: ")
  for exercise in new_exercises:
    current_item_exercises_list.append(exercise)
  save()
      
def delete_exercise(selected_workout, save):
  current_exercises = selected_workout['exercises']
  if len(current_exercises) == 0:
    print("No tienes ejercicios a eliminar")
    return
  else:
    print("--------------------------------------------------")
    print("Cual ejercicio quieres eliminar?: ")
    print("--------------------------------------------------")
    for i, exercise in enumerate(current_exercises):
      print(f"{i + 1}: {exercise['name']}")
    print(f"{i + 2}: Volver al menu anterior")
    index_to_delete = utils.select_menu_option(1, len(current_exercises)+1)

    if index_to_delete == len(current_exercises) + 1:
      print("Volviendo...")
      return

    exercise_name = current_exercises[index_to_delete -1]['name']

    confirm_delete = utils.ask_yes_no(f"Seguro quieres eliminar este ejercicio ({exercise_name})? ")
    if confirm_delete == 'y':
      current_exercises.pop(index_to_delete - 1)
      print("Ejercicio eliminado!")
      save()
    else:
      return


# COORDINATING FUNCTION

def edit_selected_existent_exercise(exercise_to_edit, save):
  while True:
    utils.show_keys_menu("Que dato quieres editar del ejercicio?: ", exercise_to_edit)
    option = utils.select_menu_option(1, len(exercise_to_edit) + 1)

    if option == 1:
      edit_exercise_name(exercise_to_edit, save)
    elif option == 2:
      edit_exercise_sets(exercise_to_edit, save)
    else:
      print("volviendo...")
      return
  
# FUNCTION TO EDIT EXERCISES SETS
def edit_exercise_sets(exercise_to_edit, save):
  while True:
    print("----------------------------------------------------")
    print("Que quieres hacer con los sets ?: ")
    print("----------------------------------------------------")
    print("1. Agregar un nuevo set")
    print("2. Editar un set existente")
    print("3. Eliminar un set existente")
    print("4. Volver al menu anterior")
    option = utils.select_menu_option(1, 4)
    if option == 1:
      add_new_set(exercise_to_edit, save)
    elif option == 2:
      edit_existent_set(exercise_to_edit, save)
    elif option == 3:
      delete_existent_set(exercise_to_edit, save)
    else: 
      print("Volviendo")
      return

def add_new_set(exercise_to_edit, save):
  while True:
    reps = utils.ask_for_integer("Ingresa la cantidad de reps: ")
    weight = utils.ask_for_float("Ingresa la cantidad de peso usado (en kg):")

    new_set = models.ExerciseSet(reps, weight)
    exercise_to_edit['sets'].append(new_set.to_dict())
    save()

    response = utils.ask_yes_no("Y para agregar otro set| N para salir: ")

    if response == "n":
      break


def edit_existent_set(exercise_to_edit, save):
  existent_sets = exercise_to_edit['sets']
  while True:
    if len(existent_sets) == 0:
      print("No tienes sets para editar en este ejercicio")
      return
    else:
        
      print("-----------------------------------------------------")
      print("Cual de estos sets quieres editar?: ")
      print("-----------------------------------------------------")
      for i, exercise_set in enumerate(existent_sets):
        print(f"{i + 1}. Set | reps: {exercise_set['reps']} - weight: {exercise_set['weight']}kg")
      print(f"f{i + 2}. Volver al menu anterior")

      set_to_edit = select_item_from_list(existent_sets)

      if set_to_edit == 'v':
        print("volviendo...")
        return

      utils.show_keys_menu("Que quieres cambiar de este set?: ", set_to_edit)
      option = utils.select_menu_option(1, len(set_to_edit) + 1)
      
      if option == 1:
        edit_set_reps(set_to_edit, save)
      elif option == 2:
        edit_set_weight(set_to_edit, save)
      else:
        print("volviendo")
        continue  

def delete_existent_set(exercise_to_edit, save):
  exercise_sets = exercise_to_edit['sets']

  while True:
    if len(exercise_sets) == 0:
      print("No tienes ningun set en este ejercicio")
      return
    
    print("-----------------------------------------------------")
    print("Cual set quieres eliminar?: ")
    print("-----------------------------------------------------")
    for i, single_set in enumerate(exercise_sets):
      print(f"{i + 1}: reps: {single_set['reps']} | weight:{single_set['weight']}")
    print(f"{i + 2}. Volver al menu anterior")

    option = utils.select_menu_option(1, len(exercise_sets) + 1)
    
    if option == len(exercise_sets) + 1:
      print("Volviendo...")
      return

    confirm_delete = utils.ask_yes_no("Seguro quieres eliminar ese set?: ")

    if confirm_delete == 'y':
      exercise_sets.pop(option - 1)
      print("Eliminado con exito")
      save()
      return
    else:
      print("Eliminacion cancelada")
      continue


# HELPER FUNCTIONS
def edit_workout_name(selected_workout, save):
  selected_workout['name'] = utils.ask_for_name("Nuevo nombre del Workout: ")
  print("Nombre cambiado con exito")
  save()

def edit_exercise_name(selected_exercise, save):
  selected_exercise['name'] = utils.ask_for_name("Ingresa el nuevo nombre del ejercicio: ")
  save()

def edit_set_reps(selected_set, save):
  selected_set['reps'] = utils.ask_for_integer("Cuantas reps?: ")
  save()

def edit_set_weight(selected_set, save):
  selected_set['weight'] = utils.ask_for_float("Cuanto peso?: ")
  save()

def select_item_from_list(data):
  chosen_edit_option = utils.select_menu_option(1, len(data) + 1)

  if chosen_edit_option == len(data) + 1:
    return 'v'
  
  item_to_edit = data[chosen_edit_option - 1]
  return item_to_edit