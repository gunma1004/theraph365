# -*- coding: utf-8 -*-
import os
import re

new_tag = '<meta name="naver-site-verification" content="ea5d5bcbb8e89d68a085335222a35108757097f5" />'

if os.path.exists("index.html"):
    with open("index.html", "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # 기존 네이버 인증 태그가 있으면 교체 또는 함께 추가
    if 'name="naver-site-verification"' in content:
        if 'ea5d5bcbb8e89d68a085335222a35108757097f5' not in content:
            content = re.sub(
                r'(<meta\s+name=["\']naver-site-verification["\'][^>]*>)',
                rf'\1\n    {new_tag}',
                content, count=1, flags=re.IGNORECASE
            )
    else:
        content = re.sub(r'(<head[^>]*>)', rf'\1\n    {new_tag}', content, count=1, flags=re.IGNORECASE)

    # Netlify canonical/og:url 도메인 동기화
    content = content.replace("https://theraphy365.pages.dev", "https://theraphy365.netlify.app")

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content)
    print("✔ index.html 에 네이버 웹마스터 소유확인 태그 적용 완료!")
