set finder=3
set outputLayer=3
set hiddenLayer=5
set hiddenNeural=64
set testing=20
set iteration=30
set epoch=100
set population=10
set F=0.5
set CR=0.3

SETLOCAL ENABLEDELAYEDEXPANSION
for %%q in (1,1,3) do (
for /L %%d in (1,1,15) do (
set filename=data%%d.csv
python main.py %finder% !filename! %outputLayer% %hiddenLayer% %hiddenNeural% %testing% %iteration% %epoch% %population% %F% %CR% >> result/%finder%/data%%d.txt
)
)

pause