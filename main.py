import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# CSV file
DATA_FILE = "student_data.csv"

# Create CSV if it doesn't exist
def create_csv_if_not_exists():
    if not os.path.exists(DATA_FILE):
        df = pd.DataFrame(columns=[
            "study_hours",
            "sleep_hours",
            "attendance_percent",
            "assignment_score",
            "exam_result"
        ])
        df.to_csv(DATA_FILE, index=False)

# Add new student(s)
def add_student():
    while True:
        print("\nEnter Student Details:")
        study_hours = round(float(input("Hours studied per day: ")), 2)
        sleep_hours = round(float(input("Sleep hours per day: ")), 2)
        attendance = round(float(input("Attendance percentage (0-100): ")), 2)
        assignment_score = round(float(input("Average assignment marks: ")), 2)
        exam_result = round(float(input("Actual exam marks: ")), 2)

        new_data = pd.DataFrame([{
            "study_hours": study_hours,
            "sleep_hours": sleep_hours,
            "attendance_percent": attendance,
            "assignment_score": assignment_score,
            "exam_result": exam_result
        }])

        df = pd.read_csv(DATA_FILE)
        df = pd.concat([df, new_data], ignore_index=True)
        df.to_csv(DATA_FILE, index=False)

        print("\nStudent data saved to CSV.")
        print(f"Total students in dataset: {len(df)}")

        more = input("\nAdd another student? (y/n): ")
        if more.lower() != "y":
            break

# Load and display dataset
def load_dataset():
    df = pd.read_csv(DATA_FILE)
    print("\nCurrent Dataset:")
    print(df)
    return df

# Train model
def train_model(df):
    if len(df) < 3:
        print("\nNeed at least 3 students to train the model.")
        return None

    X = df[[
        "study_hours",
        "sleep_hours",
        "attendance_percent",
        "assignment_score"
    ]]
    y = df["exam_result"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor()
    model.fit(X_train, y_train)

    print("\nModel trained successfully.")
    return model

# Predict exam result
def predict_student(model):
    print("\nEnter student details for prediction:")
    study_hours = float(input("Hours studied per day: "))
    sleep_hours = float(input("Sleep hours per day: "))
    attendance = float(input("Attendance percentage: "))
    assignment_score = float(input("Average assignment marks: "))

    # Use DataFrame with column names to avoid sklearn warning
    input_data = pd.DataFrame([{
        "study_hours": study_hours,
        "sleep_hours": sleep_hours,
        "attendance_percent": attendance,
        "assignment_score": assignment_score
    }])

    prediction = model.predict(input_data)
    print(f"\nPredicted Exam Result: {round(prediction[0], 2)}")

# Main program
def main():
    create_csv_if_not_exists()

    while True:
        print("\n====== Student Performance ML System ======")
        print("1. Add student data")
        print("2. View dataset")
        print("3. Train model and predict exam result")
        print("4. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            load_dataset()
        elif choice == "3":
            df = load_dataset()
            model = train_model(df)
            if model:
                predict_student(model)
        elif choice == "4":
            print("\nProgram exited.")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()