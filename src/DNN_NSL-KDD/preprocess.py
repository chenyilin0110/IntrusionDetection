from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import numpy as np     
import math

def loadDataset(x):
    temp = np.loadtxt('dataSet/NSL-KDD/' + x +'.txt', dtype=np.str, delimiter=',')
    temp = temp[0:,:-1] # rempve final column
    return temp

def saveProtocal_typeOrder(noStringTemp_X):
    protocal_type_list = []
    for i in range(np.size(noStringTemp_X, 0)):
        flag = 0
        if len(protocal_type_list) == 0:
            protocal_type_list.append(noStringTemp_X[i][1])
        else:
            for j in range(len(protocal_type_list)):
                if protocal_type_list[j] == noStringTemp_X[i][1]:
                    flag = 1
            if flag == 0:
                protocal_type_list.append(noStringTemp_X[i][1])
    return protocal_type_list

def saveServiceOrder(noStringTemp_X):
    service_list = []
    for i in range(np.size(noStringTemp_X, 0)):
        flag = 0
        if len(service_list) == 0:
            service_list.append(noStringTemp_X[i][2])
        else:
            for j in range(len(service_list)):
                if service_list[j] == noStringTemp_X[i][2]:
                    flag = 1
            if flag == 0:
                service_list.append(noStringTemp_X[i][2])
    return service_list

def saveFlagOrder(noStringTemp_X):
    flag_list = []
    for i in range(np.size(noStringTemp_X, 0)):
        flag = 0
        if len(flag_list) == 0:
            flag_list.append(noStringTemp_X[i][3])
        else:
            for j in range(len(flag_list)):
                if flag_list[j] == noStringTemp_X[i][3]:
                    flag = 1
            if flag == 0:
                flag_list.append(noStringTemp_X[i][3])
    return flag_list

def onehotencoded(x):
    # word to number
    x_labelEncoder = LabelEncoder()
    x_integerLabelEncoded = x_labelEncoder.fit_transform(x)
    
    # number to binary number
    onehotencoder = OneHotEncoder(sparse=False)
    x_integerLabelEncodedReshape = x_integerLabelEncoded.reshape(len(x_integerLabelEncoded),1)
    onehotencoded = onehotencoder.fit_transform(x_integerLabelEncodedReshape)
    return onehotencoded

def distinguishNaturalAttack(original, y, outputLayer):
    # label name transform number
    if outputLayer == 2: # 2 classification
        for i in range(np.size(original,0)):
            if original[i,-1] == 'normal':
                y.append(0)
            else:
                y.append(1)
    else: # 5 classification
        for i in range(np.size(original,0)):
            if original[i,-1] == 'normal':
                y.append(0)
            elif original[i,-1] == 'PROBE' or original[i,-1] == 'ipsweep' or original[i,-1] == 'mscan' or original[i,-1] == 'nmap' \
                or original[i,-1] == 'portsweep' or original[i,-1] == 'saint' or original[i,-1] == 'satan':
                y.append(1)
            elif original[i,-1] == 'DOS' or original[i,-1] == 'apache2' or original[i,-1] == 'back' or original[i,-1] == 'land'\
                or original[i,-1] == 'mailbomb' or original[i,-1] == 'neptune' or original[i,-1] == 'pod' or original[i,-1] == 'processtable'\
                    or original[i,-1] == 'smurf' or original[i,-1] == 'teardrop' or original[i,-1] == 'udpstorm':
                y.append(2)
            elif original[i,-1] == 'U2R' or original[i,-1] == 'buffer_overflow' or original[i,-1] == 'httptunnel' or original[i,-1] == 'loadmodule'\
                or original[i,-1] == 'perl' or original[i,-1] == 'ps' or original[i,-1] == 'rootkit' or original[i,-1] == 'sqlattack'\
                    or original[i,-1] == 'xterm':
                y.append(3)
            elif original[i,-1] == 'R2L' or original[i,-1] == 'ftp_write' or original[i,-1] == 'guess_passwd' or original[i,-1] == 'imap'\
                or original[i,-1] == 'multihop' or original[i,-1] == 'named' or original[i,-1] == 'phf' or original[i,-1] == 'sendmail'\
                    or original[i,-1] == 'snmpgetattack' or original[i,-1] == 'snmpguess' or original[i,-1] == 'spy' or original[i,-1] == 'warezclient'\
                        or original[i,-1] == 'warezmaster' or original[i,-1] == 'worm' or original[i,-1] == 'xlock' or original[i,-1] == 'xsnoop':
                y.append(4)
    return y

def replace(x, protocal_type_list, service_list, flag_list, protocal_type_onehotencoded, service_list_onehotencoded, flag_list_onehotencoded):
    # replace protocal_type
    for i in range(len(x)):
        for eachprotocal_type in range(len(protocal_type_list)):
            if x[i][1] == protocal_type_list[eachprotocal_type]:
                del x[i][1]
                nextIndex = 1
                for q in range(len(protocal_type_list)):
                    x[i].insert(nextIndex, protocal_type_onehotencoded[eachprotocal_type][q])
                    nextIndex += 1

    # replace service
    service = 2 + len(protocal_type_list) -1
    for i in range(len(x)):
        for eachservice in range(len(service_list)):
            if x[i][service] == service_list[eachservice]: # 2 + len(protocal_type_list) -1 because protocal insert so service address change
                del x[i][service]
                nextIndex = service
                for q in range(len(service_list)):
                    x[i].insert(nextIndex, service_list_onehotencoded[eachservice][q])
                    nextIndex += 1

    # replace flag
    flag = service + len(service_list)
    for i in range(len(x)):    
        for eachflag in range(len(flag_list)):
            if x[i][flag] == flag_list[eachflag]:
                del x[i][flag]
                nextIndex = flag
                for q in range(len(flag_list)):
                    x[i].insert(nextIndex, flag_list_onehotencoded[eachflag][q])
                    nextIndex += 1

def log(x):
    x = x.astype(float)
    if x != 0:
        x = math.log10(x)
    return x

def normalize(x):
    x = x.astype(float)
    minmax = preprocessing.MinMaxScaler()
    # result = preprocessing.scale(x)
    result = minmax.fit_transform(x)
    return result