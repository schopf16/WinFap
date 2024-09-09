@echo off

cd ..

ECHO --------------------------
ECHO Clear old venv
ECHO --------------------------
ECHO.
IF EXIST .venv (
    rmdir /S /Q .venv
)

ECHO.
ECHO.
ECHO --------------------------
ECHO Create new venv
ECHO --------------------------
ECHO.
python -m venv .venv
call .venv\Scripts\activate.bat


ECHO.
ECHO.
ECHO --------------------------
ECHO Install requirements
ECHO --------------------------
ECHO.
pip install -r requirements.txt

ECHO done
pause