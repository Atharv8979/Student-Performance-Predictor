# Student Performance Predictor
## Overview

The **Student Performance Analysis & Prediction System** is a Python-based machine learning project that analyzes student academic and behavioral data and predicts exam performance.  

It allows educators or learners to understand how study habits, sleep, attendance, and assignment scores affect final exam results, and provides **predictions for new students**.

## Features

- Add multiple student records interactively.
- Dataset is automatically created if it doesn’t exist (`student_data.csv`).
- View current dataset anytime.
- Train a **Random Forest Regressor** model to predict exam scores.
- Menu-based interface for easy interaction.
- Predictions based on key features:
  - Study hours per day
  - Sleep hours per day
  - Attendance percentage
  - Average assignment marks

## AI & ML Concepts

- Supervised Learning (Regression)
- Feature representation
- Model training, evaluation, and prediction
- Random Forest ensemble method
- Handling CSV datasets with **pandas**

## Technologies Used

- Python 3.x  
- pandas  
- numpy  
- scikit-learn

## Project Structure

- `main.py`
- `add_student.py`
- `data_loader.py`
- `train_model.py`
- `predict_student.py`
- `student_data.csv`
- `requirements.txt`

## Project Modules

The project is organized into separate Python files:

| Module File           | Purpose |
|-----------------------|---------|
| `add_student.py`      | Allows entering and saving new student data into `student_data.csv`. You can add as many records as needed. |
| `data_loader.py`      | Loads the CSV dataset and displays the current student records. |
| `train_model.py`      | Trains a Random Forest model using the dataset to predict exam results. |
| `predict_student.py`  | Accepts new student data and predicts their exam results using the trained model. |
| `main.py`             | Main program that provides a menu to use all other modules interactively. |

## Sample CSV Format

The student_data.csv file stores student data in this format:

| study_hours |	sleep_hours	| attendance_percent | assignment_score	| exam_result |
|-------------|-------------|--------------------|------------------|-------------|
| 7	| 7	| 85 | 75	| 80 |
| 5	| 6	| 70 | 65	| 68 |

## Installation & Setup
1. Download the project files.  
2. Open a terminal or command prompt in the folder containing the Python files.  
3. Install dependencies using the included `requirements.txt`:

```bash
pip install -r requirements.txt
```
Run the main program:
```
python main.py
```

## Limitations
- The model requires at least 3 student records to train effectively.
- Predictions may be inaccurate with small or inconsistent datasets.
- Currently uses only Random Forest Regressor; other algorithms are not implemented.
- Inputs must be numeric; no validation for wrong formats is added.
- No GUI; interaction is only via command line.

## Future Improvements
- Add more machine learning models for comparison (Linear Regression, Decision Tree, etc.).
- Implement data validation and error handling for inputs.
- Add a graphical interface for easier use.
- Integrate visualizations for dataset exploration.
- Expand features to include participation, quizzes, or other performance indicators.
- Enable batch predictions for multiple students at once.

## 👨‍💻 Author

**Atharv Bisht**  
Registration no.: 25BCE10596  
B.Tech CSE Core  
VIT Bhopal University

