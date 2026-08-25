# -*- coding: utf-8 -*-
import os
import re

count = 0
for root, dirs, files in os.walk("."):
    # 숨김 폴더(.git 등) 제외
    if any(part.startswith(".") for part in root.split(os.sep)):
        continue

    for file in files:
        if not file.endswith(".html"):
            continue

        file_path = os.path.join(root, file)

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # 1. 파일 내의 title 및 description 추출
        title_match = re.search(r'<title>(.*?)</title>', content, flags=re.DOTALL)
        desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']\s*/?>', content, flags=re.DOTALL)

        current_title = title_match.group(1).strip() if title_match else "테라피365 | 프리미엄 테라피"
        current_desc = desc_match.group(1).strip() if desc_match else "테라피365 24시 홈케어 안내"

        # 2. og:title 수정 또는 삽입
        if re.search(r'<meta\s+property=["\']og:title["\']', content):
            content = re.sub(r'<meta\s+property=["\']og:title["\']\s+content=["\'].*?["\']\s*/?>',
                             f'<meta property="og:title" content="{current_title}">', content, flags=re.DOTALL)
        else:
            content = re.sub(r'(</head>)', rf'    <meta property="og:title" content="{current_title}">\n\1', content, count=1, flags=re.IGNORECASE)

        # 3. og:description 수정 또는 삽입
        if re.search(r'<meta\s+property=["\']og:description["\']', content):
            content = re.sub(r'<meta\s+property=["\']og:description["\']\s+content=["\'].*?["\']\s*/?>',
                             f'<meta property="og:description" content="{current_desc}">', content, flags=re.DOTALL)
        else:
            content = re.sub(r'(</head>)', rf'    <meta property="og:description" content="{current_desc}">\n\1', content, count=1, flags=re.IGNORECASE)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        count += 1

print(f"✔ 총 {count}개 모든 HTML 파일에 og:title 및 og:description 적용이 완료되었습니다!")