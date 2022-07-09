echo off

call %~dp0ChelseaTG_Bot\venv\Scripts\activate

cd %~dp0ChelseaTG_Bot

set TOKEN=5530847718:AAHSoBqj8PosgbXaJJB--3k9ut0DgSoOlOk

python cfctg_bot.py

pause
