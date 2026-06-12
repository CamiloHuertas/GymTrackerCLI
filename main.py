# IMPORTS
import storage
import utils
import workout_operations
    
def main():
  data = storage.load_json()

  def save():
    storage.save_json(data)
  

  while True:
    utils.show_main_menu()
    chosen_option = utils.select_menu_option(1,5)
    if chosen_option == 1:
      workout_operations.add_workout(data['workouts'], save)
    elif chosen_option == 2:
      workout_operations.edit_workout(data['workouts'], save)
    elif chosen_option == 3:
      workout_operations.visualize_workouts(data['workouts'])
    elif chosen_option == 4:
      workout_operations.delete_whole_workout(data['workouts'], save)
    else:
      print("Saliendo... Gracias!")
      return

if __name__ == "__main__":
  main()