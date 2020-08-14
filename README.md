# Intrusion Detection System

## Dataset Online：
* This is [Industrial Control System(ICS)](https://sites.google.com/a/uah.edu/tommy-morris-uah/ics-data-sets "ICS") inline link.
* This is [KDD99](http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html "KDD Cup 1999") inline link.
* This is [NSL-KDD](https://www.unb.ca/cic/datasets/nsl.html "NSL-KDD") inline link.
* This is [CIDDS-001](https://www.hs-coburg.de/forschung-kooperation/forschungsprojekte-oeffentlich/informationstechnologie/cidds-coburg-intrusion-detection-data-sets.html "CIDDS-001") inline link.


## Hyper Parameters：

> ### Dataset：
>> #### Industrial Control System (ICS)：
>>> * finder：dataSet/IndustrialControlSystem 中哪個資料夾 ex:2->2class, 3->3class, multi->multiclass
>>> * filename：dataSet/IndustrialControlSystem/finder/ 中哪個資料集 ex:data1.csv
>>> * testing(IDCS資料集專屬)：資料分割成training data 以及 testing data ex:20->testing佔20%

>> #### KDD Cup 1999 (KDD99)：
>> KDD99 已經將資料分割成兩個檔案，因此這邊只需指定訓練資料以及測試資料。
>>> * trainData：訓練資料 ex:train
>>> * testData：測試資料 ex:test

>> #### NSL-KDD：
>> NSL-KDD 已經將資料分割成 **三** 個檔案，分別為一個訓練資料和兩個測試資料。
>>> * trainData：訓練資料 ex:train
>>> * testData：測試資料 ex:test or test-21(A subset of the KDDTest+)

>> #### CIDDS-001：
>> CIDDS-001 已經將資料分割成 **三** 個檔案，分別為一個訓練資料和兩個測試資料。
>>> * trainData：訓練資料 ex:train
>>> * testData：測試資料 ex:test

> ### Deep Learning Model：
>* outputLayer(== finder)：將資料分為幾類 ex:2class->2, 5class-> 5, multiclass->41
>* hiddenLayer：幾層隱藏層 ex:3->3個隱藏層
>* hiddenNeural：隱藏層中幾個神經元 ex:64->在隱藏層中有64個神經元
>* epoch：深度學習模型學習次數 ex:100->100次，越多執行速度越慢且易overfitting，越少則無法完整學習資料間的關聯
>* batchSize(LSTM專屬)：一次完整訓練多少筆資料 ex:10000->10000筆/次

> ### Metaheuristic：
>* iteration：迭帶次數
>* population：幾個搜尋者 ex:20->20個搜尋者，越多執行速度越慢但較可能找到更佳解
>* F：縮放因子，通常是介於0-1中間的浮點數 ex:0.5
>* CR： 交叉機率，通常是介於0-1中間的浮點數 ex:0.8

## Abbreviation Name：
* DNN -> Deep Neural Network
* LSTM -> Long-Short-Term Memory
* CNN -> Convolution Neural Network
* HC -> Hill Climbing
* DE -> Differential Evolution
* DAE -> Deep Auto Encoder
* SNDAE -> Stacked Non-symmetric Deep Auto Encoder