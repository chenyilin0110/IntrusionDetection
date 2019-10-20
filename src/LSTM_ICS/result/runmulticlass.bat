set finder=multi
set run=3

del Avg%finder%*.txt


SETLOCAL ENABLEDELAYEDEXPANSION
for /L %%d in (1,1,15) do (
	set filename=data%%d.txt
	>> Avg%finder%.txt set /p=DS%%d <nul
	python calAvg.py %finder% !filename! %run% >> Avg%finder%.txt
)

pause
