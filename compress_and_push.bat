@echo off
chcp 65001 > nul
cd /d "C:\Users\Casper\Desktop\各種程式相關\爬蟲\備份"

echo --- 壓縮快取檔案 ---
python compress_cache.py
if errorlevel 1 (
    echo ❌ 壓縮失敗
    pause
    exit /b 1
)

echo.
echo --- git push ---
git add .
git commit -m "add compressed cache files"
git push

echo.
echo ✅ 完成！
pause
