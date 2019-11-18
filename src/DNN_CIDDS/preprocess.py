from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import numpy as np
import pandas as pd

def load(week):
    Original_data = pd.read_csv('dataSet/OpenStack/CIDDS-001-internal-week' + week + '.csv')
    data = Original_data.drop(columns=['Date first seen', 'Flows', 'Tos', 'attackType', 'attackID', 'attackDescription'])
    return data

def onehotencoding(data, protocal_list, source_ip_list, \
    distination_ip_list, flag_list):
    
    labelEncoder = LabelEncoder()
    onehotencoder = OneHotEncoder(sparse=False)

    # date = data['Date first seen'].unique()
    # print(date)
    # for i in range(len(date)):
    #     date_first_seen_list.append(date[i])
    # integerLabelEncoded = labelEncoder.fit_transform(date_first_seen_list)
    # integerLabelEncodedReshape = integerLabelEncoded.reshape(len(integerLabelEncoded),1)
    # date_onehotencoded = onehotencoder.fit_transform(integerLabelEncodedReshape)
    
    # duration = data['Duration'].unique()
    # for i in range(len(duration)):
    #     duration_list.append(duration[i])
    # integerLabelEncoded = labelEncoder.fit_transform(duration_list)
    # integerLabelEncodedReshape = integerLabelEncoded.reshape(len(integerLabelEncoded),1)
    # duration_onehotencoded = onehotencoder.fit_transform(integerLabelEncodedReshape)

    protocal = data['Proto'].unique()
    for i in range(len(protocal)):
        protocal_list.append(protocal[i])
    integerLabelEncoded = labelEncoder.fit_transform(protocal_list)
    integerLabelEncodedReshape = integerLabelEncoded.reshape(len(integerLabelEncoded),1)
    protocal_onehotencoded = onehotencoder.fit_transform(integerLabelEncodedReshape)

    source_ip = data['Src IP Addr'].unique()
    for i in range(len(source_ip)):
        source_ip_list.append(source_ip[i])
    integerLabelEncoded = labelEncoder.fit_transform(source_ip_list)
    integerLabelEncodedReshape = integerLabelEncoded.reshape(len(integerLabelEncoded),1)
    srcip_onehotencoded = onehotencoder.fit_transform(integerLabelEncodedReshape)

    # source_port = data['Src Pt'].unique()
    # for i in range(len(source_port)):
    #     source_port_list.append(source_port[i])
    # integerLabelEncoded = labelEncoder.fit_transform(source_port_list)
    # integerLabelEncodedReshape = integerLabelEncoded.reshape(len(integerLabelEncoded),1)
    # srcpt_onehotencoded = onehotencoder.fit_transform(integerLabelEncodedReshape)

    distination_ip = data['Dst IP Addr'].unique()
    for i in range(len(distination_ip)):
        distination_ip_list.append(distination_ip[i])
    integerLabelEncoded = labelEncoder.fit_transform(distination_ip_list)
    integerLabelEncodedReshape = integerLabelEncoded.reshape(len(integerLabelEncoded),1)
    dstip_onehotencoded = onehotencoder.fit_transform(integerLabelEncodedReshape)
    
    # distination_port = data['Dst Pt'].unique()
    # for i in range(len(distination_port)):
    #     distination_port_list.append(distination_port[i])
    # integerLabelEncoded = labelEncoder.fit_transform(distination_port_list)
    # integerLabelEncodedReshape = integerLabelEncoded.reshape(len(integerLabelEncoded),1)
    # dstpt_onehotencoded = onehotencoder.fit_transform(integerLabelEncodedReshape)

    # packet = data['Packets'].unique()
    # for i in range(len(packet)):
    #     packets_list.append(packet[i])
    # integerLabelEncoded = labelEncoder.fit_transform(packets_list)
    # integerLabelEncodedReshape = integerLabelEncoded.reshape(len(integerLabelEncoded),1)
    # packet_onehotencoded = onehotencoder.fit_transform(integerLabelEncodedReshape)
    
    # byte = data['Bytes'].unique()
    # for i in range(len(byte)):
    #     byte_list.append(byte[i])
    # integerLabelEncoded = labelEncoder.fit_transform(byte_list)
    # integerLabelEncodedReshape = integerLabelEncoded.reshape(len(integerLabelEncoded),1)
    # byte_onehotencoded = onehotencoder.fit_transform(integerLabelEncodedReshape)
    
    flag = data['Flags'].unique()
    for i in range(len(flag)):
        flag_list.append(flag[i])
    integerLabelEncoded = labelEncoder.fit_transform(flag_list)
    integerLabelEncodedReshape = integerLabelEncoded.reshape(len(integerLabelEncoded),1)
    flag_onehotencoded = onehotencoder.fit_transform(integerLabelEncodedReshape)

    return protocal_onehotencoded, srcip_onehotencoded, dstip_onehotencoded, flag_onehotencoded

def replace(data, protocal_list, protocal, source_ip_list, source_ip, \
distination_ip_list, distination_ip, flag_list, flag):
    # numpy cannot delete element, so numpy to list
    data = data.tolist()
    
    for i in range(len(data)):
        # replace protocal
        for each_protocal in range(len(protocal_list)):
            if data[i][1] == protocal_list[each_protocal]:
                del data[i][1]
                next_index =1
                for add in range(len(protocal_list)):
                    data[i].insert(next_index, protocal[each_protocal][add])
                    next_index += 1
                break
        
        # replace source ip
        source_index = 1 + len(protocal_list)
        for each_source_ip in range(len(source_ip_list)):
            if data[i][source_index] == source_ip_list[each_source_ip]:
                del data[i][source_index]
                next_index = source_index
                for add in range(len(source_ip_list)):
                    data[i].insert(next_index, source_ip[each_source_ip][add])
                    next_index += 1
                break
        
        # replace distination ip
        # 1(tcp index) + len(prottocal_list) + len(source_ip_list) + source ip port 
        distination_index = 1 + len(protocal_list) + len(source_ip_list) + 1
        for each_distination_ip in range(len(distination_ip_list)):
            if data[i][distination_index] == distination_ip_list[each_distination_ip]:
                del data[i][distination_index]
                next_index = distination_index
                for add in range(len(distination_ip_list)):
                    data[i].insert(next_index, distination_ip[each_distination_ip][add])
                    next_index += 1
                break
        
        # replace flags
        # 1(tcp index) + len(prottocal_list) + len(source_ip_list) + 1(source ip port) + len(distination_ip_list) +
        # 1(distination ip port) + 1(packets) + 1(bytes)
        flag_index = 1 + len(protocal_list) + len(source_ip_list) + 1 + len(distination_ip_list) +\
            1 + 1 + 1
        for each_flag in range(len(flag_list)):
            if data[i][flag_index] == flag_list[each_flag]:
                del data[i][flag_index]
                next_index = flag_index
                for add in range(len(flag_list)):
                    data[i].insert(next_index, flag[each_flag][add])
                    next_index += 1
                break

def missingValue(x):
    for i in range(np.size(x,0)):
        for j in range(np.size(x,1)):
            if x[i][j] == 'inf':
                x[i][j] = 0
            elif x[i][j] == 'nan':
                x[i][j] = 0
    return x        
        
def distinguishNaturalAttack(original, y):
# Natural->0 Attack->1
    for i in range(np.size(original,0)):
        if original[i,-1] == '1.000000':
            y.append(0)
        elif original[i,-1] == '2.000000':
            y.append(1)
        elif original[i,-1] == '3.000000':
            y.append(2)
        elif original[i,-1] == '4.000000':
            y.append(3)
        elif original[i,-1] == '5.000000':
            y.append(4)
    return y

def normalize(x):
    temp = x    
    temp = temp.astype(float)
    result = preprocessing.scale(temp)    
    return result