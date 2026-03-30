import pandas as pd

def predict_student(model):

    print("Enter Student Data for Prediction")

    study = float(input("Study hours: "))
    sleep = float(input("Sleep hours: "))
    attendance = float(input("Attendance: "))
    previous = float(input("Previous marks: "))

    data = pd.DataFrame([{
        "study_hours": study,
        "sleep_hours": sleep,
        "attendance_percent": attendance,
        "assignment_score": previous
    }])

    result = model.predict(data)

    print("Predicted Final Score:", round(result[0], 2))