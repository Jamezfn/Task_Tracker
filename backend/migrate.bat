@echo off
REM Script to generate migrations for Flask

echo Initializing database migrations (run only once)...
flask db init

REM Prompt user for migration message
set /p message="Enter migration message: "

echo Creating migration scripts for current models...
flask db migrate -m "%message%"

echo Applying migrations...
flask db upgrade

echo Migrations completed.
pause
