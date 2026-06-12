# Gym Tracker CLI 

A lightweight, robust command-line application built with Python to track workouts, exercises, and sets with local data persistence.

## Tech Stack

- **Language:** Python 3.14.3
- **Storage:** JSON Fily System

## Features

- **Full CRUD operations:** Add, edit, view, delete all your workouts, individual exercises, and specific sets.
- **Robust Error Handling:** It includes robust `try-except` blocks in order to ensure appropiate running of the CLI.

## Data Structure (JSON Schema)

```json
{
  "workouts": [
    {
      "name": "Push day",
      "exercises": [
        {
          "name": "Bench Press",
          "sets": [
            {
              "reps": 10,
              "peso": 100.0
            },
            {
              "reps": 8,
              "peso": 120.0
            }
          ]
        },
        {
          "name": "Inclined Bench Press",
          "sets": []
        },
        {
          "name": "Declined Bench Press",
          "sets": []
        }
      ]
    }
  ]
}
```
## Installation & Usage

To run this command-line application locally, you just need to make sure to have *Python* and *Git* installed.
 
> No dependencies are required

1. Clone the repository  
```bash
git clone https://github.com/CamiloHuertas/GymTrackerCLI.git
cd GymTrackerCLI
```

2. Run the application
```bash
python main.py
```

> The `workouts.json` file will be automatically created if it doesn't exist

