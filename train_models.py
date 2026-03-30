from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor


def train_models(df):

    X = df[["study_hours", "sleep_hours", "attendance", "previous_marks"]]
    y = df["final_score"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    models = {
        "linear": LinearRegression(),
        "tree": DecisionTreeRegressor(),
        "forest": RandomForestRegressor()
    }

    for name, model in models.items():

        model.fit(X_train, y_train)

        score = model.score(X_test, y_test)

        print(name, "accuracy:", score)

    return models
