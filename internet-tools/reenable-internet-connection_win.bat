@echo off

:: Re-enable internet connection
echo [!] Re-enabling internet connection...

ipconfig /renew
ipconfig /flushdns

echo.
echo [#] Internet connection re-enabled!
echo.

pause
