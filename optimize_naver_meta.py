# -*- coding: utf-8 -*-
import os
import re

count = 0

for root, dirs, files in os.walk("."):
    # .git, .vscode 등 숨김 폴더 제외
    if any(part.startswith(".") for part in root.split(os.sep)):
        continue

    for file in files:
        if not file.endswith(".html"):
            continue

        file_path = os.path.join(root, file)

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # 1. 파일에서 현재 <title>과 <meta name="description"> 추출
        title_match = re.search(r'<title>(.*?)</title>', content, flags=re.DOTALL | re.IGNORECASE)
        desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']\s*/?>', content, flags=re.DOTALL | re.IGNORECASE)

        if not title_match:
            continue

        current_title = title_match.group(1).strip()
        current_desc = desc_match.group(1).strip() if desc_match else current_title

        # 2. 기존 og:title, og:description 태그가 있다면 제거 (중복 방지)
        content = re.sub(r'<meta\s+property=["\']og:title["\'].*?>\n?', '', content, flags=re.IGNORECASE)
        content = re.sub(r'<meta\s+property=["\']og:description["\'].*?>\n?', '', content, flags=re.IGNORECASE)
        content = re.sub(r'<meta\s+property=["\']og:type["\'].*?>\n?', '', content, flags=re.IGNORECASE)

        # 3. 새 Open Graph 메타 태그 블록 생성
        og_block = (
            f'    <meta property="og:type" content="website">\n'
            f'    <meta property="og:title" content="{current_title}">\n'
            f'    <meta property="og:description" content="{current_desc}">\n'
        )

        # 4. </head> 바로 위에 태그 삽입
        if "</head>" in content:
            content = re.sub(r'(</head>)', rf'{og_block}\1', content, count=1, flags=re.IGNORECASE)
        elif "</HEAD>" in content:
            content = re.sub(r'(</HEAD>)', rf'{og_block}\1', content, count=1, flags=re.IGNORECASE)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

        count += 1
        print(f"✔ 태그 생성 완료: {file_path}")

print(f"\n🎉 총 {count}개의 모든 지역/동 HTML 파일에 Open Graph 적용 완료!")