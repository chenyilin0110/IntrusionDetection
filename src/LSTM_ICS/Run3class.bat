set finder=3
set outputLayer=3
set testing=20
set iteration=80
set batchsize=100

cd result/%finder%
del *.txt
cd ../../


SETLOCAL ENABLEDELAYEDEXPANSION
for /L %%q in (1,1,3) do (
	for /L %%d in (1,1,15) do (
		set filename=data%%d.csv
		python main.py %finder% !filename! %outputLayer% %testing% %iteration% %batchsize% %%d >> result/%finder%/data%%d.txt
	)
)

pause