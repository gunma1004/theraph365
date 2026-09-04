# -*- coding: utf-8 -*-
import os
import re

SITE_DOMAIN = "https://theraphy365.pages.dev"
DEFAULT_IMAGE = f"{SITE_DOMAIN}/images/main-banner.jpg"

def sanitize_to_fixed(text):
    """'출장마사지' 관련 문구를 고정된 형태로 깔끔하게 정돈"""
    # 이미 '지역명 출장마사지' 형태가 포함되어 있다면 유지하고, 불필요한 단독 키워드만 정리
    text = re.sub(r'출장\s*안마', '홈케어 테라피', text)
    return text

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

        # 2. <meta name="description"> 추출
        desc_match = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\'](.*?)["\']', content, flags=re.DOTALL | re.IGNORECASE)
        if not desc_match:
            desc_match = re.search(r'<meta[^>]*content=["\'](.*?)["\'][^>]*name=["\']description["\']', content, flags=re.DOTALL | re.IGNORECASE)
        
        current_desc = desc_match.group(1).strip() if desc_match else current_title

        current_title = sanitize_to_fixed(current_title)
        current_desc = sanitize_to_fixed(current_desc)

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
        print(f"✔ 태그 동기화 및 고정 키워드 최적화 완료: {rel_path}")

print(f"\n🎉 총 {count}개의 모든 지역/동 HTML 파일에 출장마사지 고정형 Open Graph 적용 완료!")