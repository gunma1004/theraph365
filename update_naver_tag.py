# -*- coding: utf-8 -*-
import os
import re

count = 0
current_dir = os.path.abspath(".")

for root, dirs, files in os.walk(current_dir):
    # 숨김 폴더(.git 등) 제외
    if any(part.startswith(".") for part in root.split(os.sep)):
        continue

    for file in files:
        if not file.endswith(".html"):
            continue

        file_path = os.path.join(root, file)
        rel_path = os.path.relpath(file_path, current_dir).replace("\\", "/")
        is_root = (rel_path == "index.html")

        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        # 1. 파일 내의 title 및 description 정밀 추출
        title_match = re.search(r'<title>(.*?)</title>', content, flags=re.DOTALL | re.IGNORECASE)
        desc_match = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\'](.*?)["\']', content, flags=re.DOTALL | re.IGNORECASE)
        if not desc_match:
            desc_match = re.search(r'<meta[^>]*content=["\'](.*?)["\'][^>]*name=["\']description["\']', content, flags=re.DOTALL | re.IGNORECASE)

        current_title = title_match.group(1).strip() if title_match else "테라피365 | 서울 경기 인천 24시 프리미엄 테라피"
        current_desc = desc_match.group(1).strip() if desc_match else current_title

        # 메인 index.html 예외 필터: '출장마사지' 키워드 원천 차단
        if is_root:
            current_title = current_title.replace("출장마사지", "방문 테라피").replace("출장 마사지", "방문 테라피")
            current_desc = current_desc.replace("출장마사지", "방문 테라피").replace("출장 마사지", "방문 테라피")

        # 2. og:title 수정 또는 새로 추가
        if re.search(r'<meta\s+[^>]*property=["\']og:title["\']', content, flags=re.IGNORECASE):
            content = re.sub(
                r'<meta\s+[^>]*property=["\']og:title["\'][^>]*>',
                f'<meta property="og:title" content="{current_title}">',
                content, flags=re.IGNORECASE
            )
        else:
            content = re.sub(r'(</head>)', rf'    <meta property="og:title" content="{current_title}">\n\1', content, count=1, flags=re.IGNORECASE)

        # 3. og:description 수정 또는 새로 추가
        if re.search(r'<meta\s+[^>]*property=["\']og:description["\']', content, flags=re.IGNORECASE):
            content = re.sub(
                r'<meta\s+[^>]*property=["\']og:description["\'][^>]*>',
                f'<meta property="og:description" content="{current_desc}">',
                content, flags=re.IGNORECASE
            )
        else:
            content = re.sub(r'(</head>)', rf'    <meta property="og:description" content="{current_desc}">\n\1', content, count=1, flags=re.IGNORECASE)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        count += 1
        print(f"✔ [{rel_path}] og:title & og:description 동기화 완료")

print(f"\n🎉 총 {count}개 모든 HTML 파일에 Open Graph 메타태그 동기화가 완료되었습니다!")