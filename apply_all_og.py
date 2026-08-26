# -*- coding: utf-8 -*-
import os
import re

SITE_DOMAIN = "https://theraphy365.pages.dev"
DEFAULT_IMAGE = f"{SITE_DOMAIN}/images/main-banner.jpg"

count = 0
current_dir = os.path.abspath(".")

for root, dirs, files in os.walk(current_dir):
    # 숨김 폴더(.git 등) 제외
    if any(part.startswith(".") for part in root.split(os.sep)):
        continue

    for file in files:
        if file.lower().endswith(".html"):
            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(file_path, current_dir).replace("\\", "/")
            is_root = (rel_path == "index.html")

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

            # 메인 index.html 예외 처리: '출장마사지' 키워드 절대 배제
            if is_root:
                title = title.replace("출장마사지", "방문 테라피")
                desc = desc.replace("출장마사지", "방문 테라피")

            # 3. Canonical 및 Page URL 구성
            if is_root:
                page_url = f"{SITE_DOMAIN}/"
            else:
                clean_path = rel_path.replace("index.html", "")
                page_url = f"{SITE_DOMAIN}/{clean_path}"

            # 4. 기존 Open Graph 및 Canonical 태그 정리
            content = re.sub(r'<meta\s+property=["\']og:[^"\']+["\'][^>]*>\s*', '', content, flags=re.IGNORECASE)
            content = re.sub(r'<link\s+rel=["\']canonical["\'][^>]*>\s*', '', content, flags=re.IGNORECASE)

            # 5. 완성형 Open Graph & Canonical 블록 생성
            og_block = (
                f'\n    <!-- SEO & Open Graph (네이버/구글 검색 최적화) -->'
                f'\n    <link rel="canonical" href="{page_url}">'
                f'\n    <meta property="og:type" content="website">'
                f'\n    <meta property="og:title" content="{title}">'
                f'\n    <meta property="og:description" content="{desc}">'
                f'\n    <meta property="og:url" content="{page_url}">'
                f'\n    <meta property="og:image" content="{DEFAULT_IMAGE}">\n'
            )

            # 6. <head> 태그 바로 뒤에 삽입
            if "<head" in content.lower():
                content = re.sub(r'(<head[^>]*>)', rf'\1{og_block}', content, count=1, flags=re.IGNORECASE)

                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                count += 1
                print(f"[{count}] SEO/OG 태그 적용 완료 -> {rel_path}")

print(f"\n✔ 총 {count}개 HTML 파일에 Canonical 및 Open Graph 태그 최적화 적용 완료!")