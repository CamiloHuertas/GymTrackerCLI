def calculate_set_volume(exercise_set):
  reps = exercise_set['reps']
  peso = exercise_set['peso']
  
  return reps * peso

def calculate_exercise_volume(item):
  exercise_volume = 0
  exercise_sets = item['sets']
 
  for exercise_set in exercise_sets:
    set_volume = calculate_set_volume(exercise_set)
    exercise_volume += set_volume

  return exercise_volume


def calculate_workout_volume(workout_exercises):
  workout_volume = 0
  
  for item in workout_exercises:
    workout_volume += calculate_exercise_volume(item)
  
  return workout_volume