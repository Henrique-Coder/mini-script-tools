@echo off

:: Ask for administrator privileges
if not "%1"=="am_admin" (
    powershell -Command "Start-Process -Verb RunAs -FilePath '%0' -ArgumentList 'am_admin'"
    exit /b
)

:: Reset internet connection
echo [!] Resetting internet connection...

ipconfig /release
ipconfig /renew
ipconfig /flushdns
ipconfig /registerdns

echo.
echo [#] Internet connection reseted!
echo.

pause
