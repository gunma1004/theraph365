# -*- coding: utf-8 -*-
import os
import re
import random

# ==============================================================================
# 20종 스팸 회피 세부 테마 키워드 풀
# ==============================================================================
SAFE_THEMES = [
    "출장 힐링 마사지", "출장 홈케어 마사지", "출장 릴렉스 마사지", "출장 프리미엄 힐링 마사지", "출장 바디케어 마사지",
    "출장 아로마 마사지", "출장 스웨디시 마사지", "출장 에스테틱 마사지", "출장 오일 테라피 마사지", "출장 딥티슈 마사지",
    "출장 타이 마사지", "출장 홈타이 마사지", "출장 건식 테라피 마사지", "출장 스트레칭 마사지", "출장 지압 힐링 마사지",
    "출장 리커버리 마사지", "출장 피로회복 마사지", "출장 1:1 맞춤형 마사지", "출장 감성 테라피 마사지", "출장 웰니스 마사지"
]

def sanitize_spam_keywords(text, is_root=False):
    """단독 '출장마사지' / '출장 마사지' 패턴을 20종 복합 테마 키워드로 치환"""
    if is_root:
        # 루트 index.html은 완전 배제
        text = re.sub(r'출장\s*마사지', '방문 프리미엄 테라피', text)
        return text

    # 서브페이지: 단독 출장마사지 형태를 안전한 20종 패턴 중 무작위 치환
    def repl(match):
        return random.choice(SAFE_THEMES)

    text = re.sub(r'(?<![가-힣a-zA-Z0-9])출장\s*마사지(?![가-힣a-zA-Z0-9])', repl, text)
    return text

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

        # 단독 스팸 키워드 필터링 및 20종 패턴 치환 보정
        current_title = sanitize_spam_keywords(current_title, is_root)
        current_desc = sanitize_spam_keywords(current_desc, is_root)

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
        print(f"✔ [{rel_path}] og:title & og:description 안전 동기화 완료")

print(f"\n🎉 총 {count}개 모든 HTML 파일에 20종 키워드 기반 Open Graph 메타태그 동기화가 완료되었습니다!")