# -*- coding: utf-8 -*-
import os
import re

SITE_DOMAIN = "https://theraphy365.pages.dev"
DEFAULT_IMAGE = f"{SITE_DOMAIN}/images/main-banner.jpg"

count = 0
current_dir = os.path.abspath(".")

for root, dirs, files in os.walk(current_dir):
    # .git, .vscode 등 숨김 폴더 제외
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
        title_match = re.search(r'<title>(.*?)</title>', content, flags=re.DOTALL | re.IGNORECASE)
        if not title_match:
            continue

        current_title = title_match.group(1).strip()

        # 2. <meta name="description"> 추출 (속성 순서 무관)
        desc_match = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\'](.*?)["\']', content, flags=re.DOTALL | re.IGNORECASE)
        if not desc_match:
            desc_match = re.search(r'<meta[^>]*content=["\'](.*?)["\'][^>]*name=["\']description["\']', content, flags=re.DOTALL | re.IGNORECASE)
        
        current_desc = desc_match.group(1).strip() if desc_match else current_title

        # 메인 index.html 예외 필터: '출장마사지' 키워드 원천 차단
        if is_root:
            current_title = current_title.replace("출장마사지", "방문 테라피").replace("출장 마사지", "방문 테라피")
            current_desc = current_desc.replace("출장마사지", "방문 테라피").replace("출장 마사지", "방문 테라피")

        # 3. Canonical 및 og:url 경로 구성
        if is_root:
            page_url = f"{SITE_DOMAIN}/"
        else:
            clean_path = rel_path.replace("index.html", "")
            page_url = f"{SITE_DOMAIN}/{clean_path}"

        # 4. 기존 Open Graph 및 Canonical 태그 전체 정리 (중복 생성 방지)
        content = re.sub(r'<meta\s+property=["\']og:[^"\']+["\'][^>]*>\s*\n?', '', content, flags=re.IGNORECASE)
        content = re.sub(r'<link\s+rel=["\']canonical["\'][^>]*>\s*\n?', '', content, flags=re.IGNORECASE)

        # 5. 완성형 SEO 및 Open Graph 태그 블록 생성
        og_block = (
            f'    <link rel="canonical" href="{page_url}">\n'
            f'    <meta property="og:type" content="website">\n'
            f'    <meta property="og:title" content="{current_title}">\n'
            f'    <meta property="og:description" content="{current_desc}">\n'
            f'    <meta property="og:url" content="{page_url}">\n'
            f'    <meta property="og:image" content="{DEFAULT_IMAGE}">\n'
        )

        # 6. </head> 바로 위에 태그 삽입
        if re.search(r'</head>', content, flags=re.IGNORECASE):
            content = re.sub(r'(</head>)', rf'{og_block}\1', content, count=1, flags=re.IGNORECASE)
        elif "<body" in content.lower():
            content = re.sub(r'(<body[^>]*>)', rf'{og_block}\1', content, count=1, flags=re.IGNORECASE)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

        count += 1
        print(f"✔ 태그 생성 완료: {rel_path}")

print(f"\n🎉 총 {count}개의 모든 지역/동 HTML 파일에 네이버 최적화 Open Graph 적용 완료!")