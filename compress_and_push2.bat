@echo off
chcp 65001 > nul
echo 開始執行...

cd /d "C:\Users\Casper\Desktop\各種程式相關\爬蟲\備份"
echo 目前目錄: %CD%

echo.
echo --- 壓縮檔案 ---
python compress_cache.py
echo 壓縮 errorlevel: %errorlevel%

echo.
echo --- git add ---
git add .

echo --- git commit ---
git commit -m "update index and cache"

echo --- git push ---
git push

echo.
echo 全部完成！
pause
