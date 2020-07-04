from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import classification_report

def accuracy(y_test_ture, y_test_predic):
    # accuarcy
    accuracy = accuracy_score(y_test_ture, y_test_predic)

    # f1_score
    # f1score = f1_score(y_test_ture, y_test_predic, average='macro')

    # precision_score
    precision = precision_score(y_test_ture, y_test_predic, average='macro')

    # recall_score
    recall = recall_score(y_test_ture, y_test_predic, average='macro')

    # classification_report
    # print("The testing classification_report is")
    # print(classification_report(y_test_ture, y_test_predic))
    return accuracy, precision, recall