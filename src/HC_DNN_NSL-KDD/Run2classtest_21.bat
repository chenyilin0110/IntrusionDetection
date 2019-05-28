set trainData=train.txt
set testData=test.txt
set testData_21=test-21.txt
set hiddenLayer=1
set outputLayer=2
set iteration=40
set epoch=80

SETLOCAL ENABLEDELAYEDEXPANSION
for /L %%d in (1,1,5) do (
	python main.py %trainData% %testData_21% %testData% %hiddenLayer% %outputLayer% %iteration% %epoch% >> result/%outputLayer%class/%%dtest_21.txt
)

pause