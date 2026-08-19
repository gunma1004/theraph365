# -*- coding: utf-8 -*-
import os
import re

NEW_TAG = '<meta name="naver-site-verification" content="345750987cf9afb615eee935f0cb912be0dafeb5" />'

count = 0
for root, dirs, files in os.walk("."):
    for file in files:
        if not file.endswith(".html"):
            continue
        
        file_path = os.path.join(root, file)
        
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # 기존 naver-site-verification 메타태그가 있으면 새 태그로 치환
        if 'name="naver-site-verification"' in content or "name='naver-site-verification'" in content:
            content = re.sub(r'<meta\s+name=["\']naver-site-verification["\']\s+content=["\'].*?["\']\s*/?>', NEW_TAG, content)
        else:
            # 없으면 <head> 바로 아래에 삽입
            content = re.sub(r'(<head.*?>)', rf'\1\n    {NEW_TAG}', content, count=1, flags=re.IGNORECASE)
            
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        count += 1

print(f"✔ 총 {count}개 모든 HTML 파일에 새로운 네이버 소유확인 태그가 완벽하게 적용되었습니다.")
