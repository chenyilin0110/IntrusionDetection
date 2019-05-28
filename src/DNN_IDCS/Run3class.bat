set finder=3
set outputLayer=3
set testing=20
set hiddenLayer=5
set hiddenNeural=64
set iteration=100
del result/%finder%/data*.txt

SETLOCAL ENABLEDELAYEDEXPANSION
for /L %%q in (1,1,3) do (
    for /L %%d in (1,1,15) do (
    set filename=data%%d.csv
    python main.py %finder% !filename! %outputLayer% %hiddenLayer% %hiddenNeural% %testing% %iteration% >> result/%finder%/data%%d.txt
    )
)

pause