#Student performance and attendance analysis
A Python project built in Google Colab using `pandas` and `numpy` to load student records from `students_dataset_60.csv`, calculate the average marks, and search records by name or roll number.

## Repository Files
- `hcl_training_project.ipynb`: Main Python notebook containing data loading, average calculation, and interactive search.
- `students_dataset_60.csv`: Dataset containing 60 student records (`Roll No`, `Name`, and `Marks`).
- `requirements.txt`: Required Python packages (`pandas` and `numpy`).

## How It Works
1. Loads `students_dataset_60.csv` using `pandas` and displays the records and total count.
2. Calculates and rounds the average marks using `numpy`.
3. Takes user input (`Name` or `Roll No`) with `.strip()` and `.lower()` and displays matching student details.

## How to Run
1. Open `hcl_training_project.ipynb` in Google Colab or load it from GitHub (`apala338/hcl-python-project`).
2. Ensure `students_dataset_60.csv` is accessible in the working environment.
3. Run the notebook cells from top to bottom.
