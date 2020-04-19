from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

def accuracy(y_test_ture, y_test_predic):
    # # recall_score
    # print(recall_score(y_test_ture, y_test_predic, average='macro')*100, "", end='')

    # # false_alarm_ratio
    # confusion_matrix_value = confusion_matrix(y_test_ture, y_test_predic)
    # print(confusion_matrix_value[1][0]/(confusion_matrix_value[1][0] + confusion_matrix_value[1][1])*100, "", end='')

    # # precision_score
    # print(precision_score(y_test_ture, y_test_predic, average='macro')*100, "", end='')

    # accuarcy
    accuracy = accuracy_score(y_test_ture, y_test_predic)

    # f1_score
    # print("The testing f1_score is", f1_score(y_test_ture, y_test_predic, average='micro'))

    # classification_report
    # print("The testing classification_report is")
    # print(classification_report(y_test_ture, y_test_predic))
    return accuracy