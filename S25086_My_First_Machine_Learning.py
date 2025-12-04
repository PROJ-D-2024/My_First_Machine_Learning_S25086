from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

#for tree visualisation
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

def linear_regression_model():
    print("Linear Regression" + "\n")

    data = fetch_california_housing()
    X, y = data.data, data.target

    # Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict
    y_pred = model.predict(X_test)

    # Evaluate
    print("R²:", r2_score(y_test, y_pred))
    print("MSE:", mean_squared_error(y_test, y_pred))
    print("Coefficients:", model.coef_)

def tree_based_model():
    print("\n" + "Random Forest Classifier" + "\n")

    # Load
    data = load_iris()
    X, y = data.data, data.target

    # Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Predict
    y_pred = model.predict(X_test)

    # Evaluate
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))

    # Visualisation of a tree
    plt.figure(figsize=(20, 10))

    plot_tree(model.estimators_[0],
              feature_names=data.feature_names,
              class_names=data.target_names,
              filled=True,
              rounded=True,
              fontsize=10)

    plt.title("Visualisation of a first tree from all generated trees")
    plt.show()

def native_bayes_model():
    print("Naive Bayes Classifier" + "\n")

    # Load text data
    categories = ["sci.space", "comp.graphics", "rec.sport.hockey"]
    data = fetch_20newsgroups(subset="all", categories=categories)

    # Vectorize text
    vectorizer = TfidfVectorizer(stop_words="english")
    X = vectorizer.fit_transform(data.data)
    y = data.target

    # Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Split only text
    _, X_test_text, _, _ = train_test_split(data.data, data.target, test_size=0.2, random_state=42)

    # Model
    model = MultinomialNB()
    model.fit(X_train, y_train)

    # Predict
    y_pred = model.predict(X_test)

    # Evaluate
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))

    # Printing first 5 predicted labels
    for i in range(5):
        true_label_name = data.target_names[y_test[i]]
        pred_label_name = data.target_names[y_pred[i]]

        text_sample = X_test_text[i][:80]

        print(f"Text: '{text_sample}...'")
        print(f"Real state: {true_label_name} | Prediction: {pred_label_name}")

if __name__ == '__main__':
    linear_regression_model()
    tree_based_model()
    native_bayes_model()