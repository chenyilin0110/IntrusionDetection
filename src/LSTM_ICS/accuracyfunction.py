from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import classification_report

def accuracy(y_test_ture, y_test_predic):
    # accuarcy
    print(accuracy_score(y_test_ture, y_test_predic))

    # f1_score
    # print("The testing f1_score is", f1_score(y_test_ture, y_test_predic, average='micro'))

    # precision_score
    # print("The testing precision_score is", precision_score(y_test_ture, y_test_predic, average='micro'))

    # recall_score
    # print("The testing recall_score is", recall_score(y_test_ture, y_test_predic, average='micro'))    

    # classification_report
    # print("The testing classification_report is")
    # print(classification_report(y_test_ture, y_test_predic))