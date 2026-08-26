# -*- coding: utf-8 -*-
import os

print("🚀 테라피365 브랜드명 완벽 정제 및 통일 작업 시작...")

count = 0
for root, dirs, files in os.walk("."):
    # .git 등 숨김 폴더 제외
    if any(part.startswith(".") for part in root.split(os.sep)):
        continue

    for file in files:
        if not file.endswith(".html"):
            continue
        
        file_path = os.path.join(root, file)
        rel_path = os.path.relpath(file_path, ".").replace("\\", "/")
        is_root = (rel_path == "index.html")
        
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        
        # 1. 과거 브랜드명(스파루나, 마사지몽) -> '테라피365'로 일괄 교체
        content = content.replace("마사지몽", "테라피365")
        content = content.replace("스파루나", "테라피365")
        content = content.replace("MassageMong", "Theraphy365")
        content = content.replace("SpaLuna", "Theraphy365")
        content = content.replace("massagemong.pages.dev", "theraphy365.pages.dev")
        content = content.replace("spaluna.pages.dev", "theraphy365.pages.dev")
        content = content.replace("massagemong", "theraphy365")
        content = content.replace("spaluna", "theraphy365")
        
        # 2. 메인 페이지 전용 키워드 필터링 (출장마사지 절대 배제)
        if is_root:
            content = content.replace("출장마사지", "방문 테라피")
            content = content.replace("출장 마사지", "방문 테라피")
            content = content.replace("출장안마", "홈케어 테라피")
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        count += 1
        print(f"✔ [{rel_path}] 테라피365 브랜드 적용 완료")

print(f"\n🎉 총 {count}개 페이지가 '테라피365'로 완벽하게 정제되었습니다!")