class Workout():
  def __init__(self, name, exercises):
    self.name = name
    self.exercises = exercises

  def to_dict(self):
    return {
      "name": self.name,
      "exercises": self.exercises
    }

class ExerciseSet():
  def __init__(self, reps, peso):
    self.reps = reps
    self.peso = peso

  def to_dict(self):
    return {
      "reps": self.reps,
      "peso": self.peso
    }