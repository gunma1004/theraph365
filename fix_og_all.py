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
        if not file.endswith(".html"):
            continue

        file_path = os.path.join(root, file)
        rel_path = os.path.relpath(file_path, current_dir).replace("\\", "/")
        is_root = (rel_path == "index.html")

        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        # 1. <title> 추출
        title_match = re.search(r'<title>(.*?)</title>', content, flags=re.IGNORECASE | re.DOTALL)
        page_title = title_match.group(1).strip() if title_match else "테라피365 | 서울 경기 인천 24시 프리미엄 테라피"

        # 2. <meta name="description"> 추출
        desc_match = re.search(r'<meta\s+[^>]*name=["\']description["\'][^>]*content=["\'](.*?)["\'][^>]*>', content, flags=re.IGNORECASE | re.DOTALL)
        if not desc_match:
            desc_match = re.search(r'<meta\s+[^>]*content=["\'](.*?)["\'][^>]*name=["\']description["\'][^>]*>', content, flags=re.IGNORECASE | re.DOTALL)
        page_desc = desc_match.group(1).strip() if desc_match else page_title

        # 메인 index.html 예외 처리: '출장마사지' 키워드 원천 차단
        if is_root:
            page_title = page_title.replace("출장마사지", "방문 테라피").replace("출장 마사지", "방문 테라피")
            page_desc = page_desc.replace("출장마사지", "방문 테라피").replace("출장 마사지", "방문 테라피")

        # 3. 고유 URL & Canonical 링크 생성
        if is_root:
            page_url = f"{SITE_DOMAIN}/"
        else:
            clean_path = rel_path.replace("index.html", "")
            page_url = f"{SITE_DOMAIN}/{clean_path}"

        # 4. 기존 og 및 canonical 태그 완전 제거 (중복 누적 방지)
        content = re.sub(r'<meta\s+property=["\']og:[^"\']+["\'][^>]*>\s*', '', content, flags=re.IGNORECASE)
        content = re.sub(r'<link\s+rel=["\']canonical["\'][^>]*>\s*', '', content, flags=re.IGNORECASE)

        # 5. 삽입할 정돈된 SEO / Open Graph 태그 블록
        og_block = (
            f'\n    <link rel="canonical" href="{page_url}">'
            f'\n    <meta property="og:type" content="website">'
            f'\n    <meta property="og:title" content="{page_title}">'
            f'\n    <meta property="og:description" content="{page_desc}">'
            f'\n    <meta property="og:url" content="{page_url}">'
            f'\n    <meta property="og:image" content="{DEFAULT_IMAGE}">\n'
        )

        # 6. <head> 태그 바로 뒤에 주입
        if re.search(r'<head.*?>', content, flags=re.IGNORECASE):
            content = re.sub(r'(<head.*?>)', rf'\1{og_block}', content, count=1, flags=re.IGNORECASE)
            
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            count += 1
            print(f"✔ [{count}] SEO/OG 태그 주입 완료 -> {rel_path}")

print(f"\n🎉 총 {count}개의 HTML 파일에 네이버 SEO 맞춤 Open Graph 및 Canonical 태그가 적용되었습니다.")