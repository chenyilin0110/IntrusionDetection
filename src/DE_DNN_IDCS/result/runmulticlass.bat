set finder=multi
set run=3
set output=accuracy
del Avg%finder%*.txt


SETLOCAL ENABLEDELAYEDEXPANSION
for /L %%d in (1,1,15) do (
set filename=data%%d.txt
>> Avg%finder%%output%.txt set /p=DS%%d <nul
python calAvg.py %finder% !filename! %run% %output% >> Avg%finder%%output%.txt
)

set output=f1score

SETLOCAL ENABLEDELAYEDEXPANSION
for /L %%d in (1,1,15) do (
set filename=data%%d.txt
>> Avg%finder%%output%.txt set /p=DS%%d <nul
python calAvg.py %finder% !filename! %run% %output% >> Avg%finder%%output%.txt
)

set output=precision
SETLOCAL ENABLEDELAYEDEXPANSION
for /L %%d in (1,1,15) do (
set filename=data%%d.txt
>> Avg%finder%%output%.txt set /p=DS%%d <nul
python calAvg.py %finder% !filename! %run% %output% >> Avg%finder%%output%.txt
)

set output=recall
SETLOCAL ENABLEDELAYEDEXPANSION
for /L %%d in (1,1,15) do (
set filename=data%%d.txt
>> Avg%finder%%output%.txt set /p=DS%%d <nul
python calAvg.py %finder% !filename! %run% %output% >> Avg%finder%%output%.txt
)

pause
