import gzip
import shutil
import os

BASE_DIR    = r'C:\Users\Casper\Desktop\各種程式相關\爬蟲\備份'
DROPBOX_DIR = r'C:\Users\Casper\Dropbox'

FILES = [
    'setlist_cache.txt',
    'cover_cache.txt',
    'vtuber_list.txt',
]

for dir_name, dir_path in [('備份目錄', BASE_DIR), ('Dropbox', DROPBOX_DIR)]:
    print(f'\n--- {dir_name} ---')
    for fname in FILES:
        src = os.path.join(dir_path, fname)
        dst = src + '.gz'
        if not os.path.exists(src):
            print(f'  ⚠️  找不到 {fname}，略過')
            continue
        with open(src, 'rb') as f_in, gzip.open(dst, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
        orig_kb = os.path.getsize(src) / 1024
        gz_kb   = os.path.getsize(dst) / 1024
        print(f'  ✅ {fname}  ({orig_kb:.0f} KB → {gz_kb:.0f} KB, {gz_kb/orig_kb*100:.0f}%)')

print('\n✅ 全部完成！')
