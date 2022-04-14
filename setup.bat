
@echo off
rd /S /Q venv

echo Creating new virtual environment...
py -m venv venv
echo Created virtual environment.

echo Activating virtual environment...
call venv\Scripts\activate
echo Activated.

echo Installing dependencies...
venv\Scripts\pip install -r requirements.txt --upgrade
echo Dependencies installed.

echo Deactivating virtual environment...
call venv\Scripts\deactivate
echo Deactivated.

echo Setup complete.