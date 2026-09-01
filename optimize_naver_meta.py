# -*- coding: utf-8 -*-
import os
import re
import random

SITE_DOMAIN = "https://theraphy365.pages.dev"
DEFAULT_IMAGE = f"{SITE_DOMAIN}/images/main-banner.jpg"

# ==============================================================================
# 20종 스팸 회피 세부 테마 키워드 풀
# ==============================================================================
THEME_KEYWORDS_20 = [
    "출장 힐링 마사지", "출장 홈케어 마사지", "출장 릴렉스 마사지", "출장 프리미엄 힐링 마사지", "출장 바디케어 마사지",
    "출장 아로마 마사지", "출장 스웨디시 마사지", "출장 에스테틱 마사지", "출장 오일 테라피 마사지", "출장 딥티슈 마사지",
    "출장 타이 마사지", "출장 홈타이 마사지", "출장 건식 테라피 마사지", "출장 스트레칭 마사지", "출장 지압 힐링 마사지",
    "출장 리커버리 마사지", "출장 피로회복 마사지", "출장 1:1 맞춤형 마사지", "출장 감성 테라피 마사지", "출장 웰니스 마사지"
]

def sanitize_text(text, is_root=False):
    """단독 '출장마사지' / '출장 마사지' 패턴을 20종 복합 테마 키워드로 치환"""
    if is_root:
        text = re.sub(r'출장\s*마사지', '방문 프리미엄 테라피', text)
        text = re.sub(r'출장\s*안마', '홈케어 테라피', text)
        return text

    def repl(match):
        return random.choice(THEME_KEYWORDS_20)

    text = re.sub(r'(?<![가-힣a-zA-Z0-9])출장\s*마사지(?![가-힣a-zA-Z0-9])', repl, text)
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

        # 2. <meta name="description"> 추출 (속성 순서 무관)
        desc_match = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\'](.*?)["\']', content, flags=re.DOTALL | re.IGNORECASE)
        if not desc_match:
            desc_match = re.search(r'<meta[^>]*content=["\'](.*?)["\'][^>]*name=["\']description["\']', content, flags=re.DOTALL | re.IGNORECASE)
        
        current_desc = desc_match.group(1).strip() if desc_match else current_title

        # 단독 스팸 키워드 필터링 및 20종 복합 패턴 적용
        current_title = sanitize_text(current_title, is_root)
        current_desc = sanitize_text(current_desc, is_root)

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
        print(f"✔ 태그 동기화 및 20종 키워드 최적화 완료: {rel_path}")

print(f"\n🎉 총 {count}개의 모든 지역/동 HTML 파일에 네이버 최적화 Open Graph 적용 완료!")