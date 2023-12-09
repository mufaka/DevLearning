import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():
    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
       0 - Administrative, an integer
       1 - Administrative_Duration, a floating point number
       2 - Informational, an integer
       3 - Informational_Duration, a floating point number
       4 - ProductRelated, an integer
       5 - ProductRelated_Duration, a floating point number
       6 - BounceRates, a floating point number
       7 - ExitRates, a floating point number
       8 - PageValues, a floating point number
       9 - SpecialDay, a floating point number
      10 - Month, an index from 0 (January) to 11 (December)
      11 - OperatingSystems, an integer
      12 - Browser, an integer
      13 - Region, an integer
      14 - TrafficType, an integer
      15 - VisitorType, an integer 0 (not returning) or 1 (returning)
      16 - Weekend, an integer 0 (if false) or 1 (if true)

    
    Administrative,Administrative_Duration,Informational,Informational_Duration,ProductRelated,ProductRelated_Duration,BounceRates,ExitRates,PageValues,SpecialDay,Month,OperatingSystems,Browser,Region,TrafficType,VisitorType,Weekend,Revenue
    
    Administrative, Informational, ProductRelated, Month, OperatingSystems, Browser, Region, TrafficType, VisitorType, and Weekend should all be of type int
    Administrative_Duration, Informational_Duration, ProductRelated_Duration, BounceRates, ExitRates, PageValues, and SpecialDay should all be of type float.
    Month should be 0 for January, 1 for February, 2 for March, etc. up to 11 for December.
    VisitorType should be 1 for returning visitors and 0 for non-returning visitors.
    Weekend should be 1 if the user visited on a weekend and 0 otherwise.    

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)

        evidence = []
        labels = []
        for row in reader:
            evidence.append(get_evidence(row))
            labels.append(1 if row[17] == "TRUE" else 0)

            """                
            data.append({
                "evidence": get_evidence(row),
                "label": 1 if row[17] == "TRUE" else 0
            })
            """

        return evidence, labels


def get_evidence(row):
    evidence = []
    int_indexes = [0, 2, 4, 11, 12, 13, 14]
    float_indexes = [1, 3, 5, 6, 7, 8, 9]

    for i, v in enumerate(row):
        # print(f"iterating {i}, {v}")
        if i in int_indexes:
            evidence.append(int(v))
        elif i in float_indexes:
            evidence.append(float(v))
        elif i == 10:  # month index
            # style50 recommends this formatting
            months = [
                "Jan", 
                "Feb", 
                "Mar", 
                "Apr", 
                "May", 
                "Jun", 
                "Jul", 
                "Aug", 
                "Sep", 
                "Oct", 
                "Nov", 
                "Dec",
            ]

            # some data is full month name but abbreviations are just first 3 letters
            evidence.append(months.index(v[:3]))
        elif i == 15:  # visitor type
            evidence.append(1 if v == "Returning_Visitor" else 0)
        elif i == 16:
            evidence.append(1 if v == "TRUE" else 0)

    return evidence


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(evidence, labels)

    return model


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    true_count = 0
    false_count = 0

    true_positive = 0
    true_negative = 0

    for i, label in enumerate(labels):
        if label == 1:
            true_count += 1

            if predictions[i] == 1:
                true_positive += 1 
        else:
            false_count += 1

            if predictions[i] == 0:
                true_negative += 1

    # print(f"Total Correct = {true_positive + true_negative}")
    # True positive rate seems low at 37-40%

    return true_positive / true_count, true_negative / false_count 


if __name__ == "__main__":
    main()
