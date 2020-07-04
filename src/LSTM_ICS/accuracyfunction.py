from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import classification_report

def accuracy(y_test_ture, y_test_predic):
    # accuarcy
    accuracyValue = accuracy_score(y_test_ture, y_test_predic)

    # f1_score
    # print("The testing f1_score is", f1_score(y_test_ture, y_test_predic, average='micro'))

    # precision_score
    precision = precision_score(y_test_ture, y_test_predic, average='micro')

    # recall_score
    recall = recall_score(y_test_ture, y_test_predic, average='micro')

    # classification_report
    # print("The testing classification_report is")
    # print(classification_report(y_test_ture, y_test_predic))
    return accuracyValue, precision, recall