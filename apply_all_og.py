# -*- coding: utf-8 -*-
import os
import re

count = 0
current_dir = os.path.abspath(".")

for root, dirs, files in os.walk(current_dir):
    # 숨김 폴더 제외
    if any(part.startswith(".") for part in root.split(os.sep)):
        continue

    for file in files:
        if file.lower().endswith(".html"):
            file_path = os.path.join(root, file)

            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

            # 1. <title> 가져오기
            title_match = re.search(r'<title>(.*?)</title>', content, flags=re.IGNORECASE | re.DOTALL)
            title = title_match.group(1).strip() if title_match else "테라피365 | 서울 경기 인천 24시 프리미엄 테라피"

            # 2. description 가져오기
            desc_match = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\'](.*?)["\']', content, flags=re.IGNORECASE | re.DOTALL)
            if not desc_match:
                desc_match = re.search(r'<meta[^>]*content=["\'](.*?)["\'][^>]*name=["\']description["\']', content, flags=re.IGNORECASE | re.DOTALL)
            desc = desc_match.group(1).strip() if desc_match else title

            # 3. 기존 og 태그 정리
            content = re.sub(r'<meta\s+property=["\']og:[^"\']+["\'][^>]*>\s*', '', content, flags=re.IGNORECASE)

            # 4. <head> 바로 뒤에 새 Open Graph 삽입
            og_block = (
                f'\n    <meta property="og:type" content="website">'
                f'\n    <meta property="og:title" content="{title}">'
                f'\n    <meta property="og:description" content="{desc}">'
                f'\n    <meta property="og:image" content="/images/main-banner.jpg">\n'
            )

            if "<head>" in content.lower():
                content = re.sub(r'(<head[^>]*>)', rf'\1{og_block}', content, count=1, flags=re.IGNORECASE)

                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                count += 1
                print(f"[{count}] 적용 완료 -> {file_path}")

print(f"\n 총 {count}개의 HTML 파일에 Open Graph가 성공적으로 삽입되었습니다!")