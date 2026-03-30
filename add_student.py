import pandas as pd
import os

def load_dataset(path):

    # Create folder if it doesn't exist
    os.makedirs("data", exist_ok=True)

    # If dataset doesn't exist, create empty one
    if not os.path.exists(path):
        df = pd.DataFrame(columns=[
            "study_hours",
            "sleep_hours",
            "attendance",
            "previous_marks",
            "final_score"
        ])
        df.to_csv(path, index=False)
        print("Dataset created:", path)

    df = pd.read_csv(path)

    print("\nDataset Loaded")
    print(df.head())

    return df