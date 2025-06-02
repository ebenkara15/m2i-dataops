from evidently import Report
from evidently.presets import DataDriftPreset
from sklearn import datasets
from sklearn.model_selection import train_test_split

# Load the Iris dataset
X, y = datasets.load_iris(return_X_y=True, as_frame=True)

# Split the data into training and test sets
X_train, X_test, _, _ = train_test_split(X, y, test_size=0.2, random_state=42)

report = Report(metrics=[DataDriftPreset()])
evaluated = report.run(reference_data=X_train, current_data=X_test)

evaluated.save_html("drift_report.html")
