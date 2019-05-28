set trainData=train.txt
set testData=test.txt
set testData_21=test-21.txt
set hiddenLayer=1
set outputLayer=5
set iteration=40
set epoch=80
set population=20
set F=0.5
set CR=0.3

SETLOCAL ENABLEDELAYEDEXPANSION
for /L %%d in (1,1,3) do (
	python main.py %trainData% %testData_21% %testData% %hiddenLayer% %outputLayer% %iteration% %epoch% %population% %F% %CR% >> result/%outputLayer%class/%%dtest_21.txt
)

pause