import os
import pickle

from sklearn import datasets
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

data = datasets.load_iris()
X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=33
)


estimator = GridSearchCV(
    estimator=Pipeline(
        [
            ("scaler", StandardScaler()),
            ("sgdclassifier", SGDClassifier(max_iter=1000, tol=None)),
        ]
    ),
    param_grid=[
        {
            "sgdclassifier__loss": ["hinge", "log"],
            "sgdclassifier__penalty": ["l2", "l1", "elasticnet"],
        }
    ],
    cv=5,
    scoring="accuracy",
    refit=True,
)


estimator.fit(X_train, y_train)

module_path = os.path.dirname(__file__)
file_name = os.path.join(module_path, "..", "estimator.pickle")
with open(file_name, "wb") as f:
    pickle.dump(estimator, f, pickle.HIGHEST_PROTOCOL)
