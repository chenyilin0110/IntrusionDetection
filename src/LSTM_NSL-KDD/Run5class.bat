set trainData=train.txt
set testData=test.txt
set testData_21=test-21.txt
set hiddenLayer=1
set outputLayer=5
set batchsize=10000
set epoch=80

SETLOCAL ENABLEDELAYEDEXPANSION
for /L %%d in (1,1,15) do (
	python main.py %trainData% %testData% %testData_21% %hiddenLayer% %outputLayer% %batchsize% %epoch% >> result/%outputLayer%class/test.txt
	python main.py %trainData% %testData_21% %testData% %hiddenLayer% %outputLayer% %batchsize% %epoch% >> result/%outputLayer%class/test21.txt
)

pause