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

        # 1. <title> 추출
        title_match = re.search(r'<title>(.*?)</title>', content, flags=re.IGNORECASE)
        page_title = title_match.group(1).strip() if title_match else "테라피365 | 서울 경기 인천 24시 프리미엄 테라피"

        # 2. <meta name="description"> 추출
        desc_match = re.search(r'<meta\s+[^>]*name=["\']description["\'][^>]*content=["\'](.*?)["\'][^>]*>', content, flags=re.IGNORECASE)
        if not desc_match:
            desc_match = re.search(r'<meta\s+[^>]*content=["\'](.*?)["\'][^>]*name=["\']description["\'][^>]*>', content, flags=re.IGNORECASE)
        page_desc = desc_match.group(1).strip() if desc_match else page_title

        # 3. 기존 og 태그가 혹시 있다면 완전 제거
        content = re.sub(r'<meta\s+property=["\']og:title["\'][^>]*>', '', content, flags=re.IGNORECASE)
        content = re.sub(r'<meta\s+property=["\']og:description["\'][^>]*>', '', content, flags=re.IGNORECASE)
        content = re.sub(r'<meta\s+property=["\']og:type["\'][^>]*>', '', content, flags=re.IGNORECASE)

        # 4. 삽입할 Open Graph 블록
        og_tags = f'<meta property="og:type" content="website"><meta property="og:title" content="{page_title}"><meta property="og:description" content="{page_desc}">'

        # 5. <head> 바로 뒤에 강제 주입
        if re.search(r'<head.*?>', content, flags=re.IGNORECASE):
            content = re.sub(r'(<head.*?>)', rf'\1{og_tags}', content, count=1, flags=re.IGNORECASE)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            count += 1
            print(f"✔ 적용 성공: {file_path}")

print(f"\n 총 {count}개의 HTML 파일에 Open Graph가 강제 주입되었습니다.")