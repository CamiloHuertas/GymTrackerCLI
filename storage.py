import json

def load_json():
  try:
    with open("workouts.json", "r", encoding='utf-8') as file:
      data = json.load(file)
  except FileNotFoundError:
    data = {
      "workouts": []
    }
  except json.JSONDecodeError:
    data = {
      "workouts": []
    }

  return data


def save_json(data):
  with open('workouts.json', 'w', encoding="utf-8") as file:
    json.dump(data, file, indent=2, ensure_ascii=False)