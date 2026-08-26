# -*- coding: utf-8 -*-
import os
import re

# Unsplash Photo ID -> 로컬 이미지 매핑
PHOTO_ID_MAPPING = {
    "photo-1544161515-4ab6ce6db874": "/images/vendor1.jpg",
    "photo-1519823551278-64ac92734fb1": "/images/vendor2.jpg",
    "photo-1570172619644-dfd03ed5d881": "/images/vendor3.jpg",
    "photo-1600334089648-b0d9d3028eb2": "/images/vendor4.jpg",
    "photo-1515377905703-c4788e51af15": "/images/vendor5.jpg",
}

count = 0

for root, dirs, files in os.walk("."):
    # 숨김 폴더(.git 등) 제외
    if any(part.startswith(".") for part in root.split(os.sep)):
        continue

    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(file_path, ".").replace("\\", "/")

            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

            new_content = content

            # 1. 히어로 배너 배경 이미지 Unsplash URL 정규식 치환
            new_content = re.sub(
                r'https://images\.unsplash\.com/photo-[0-9a-f\-]+\?[^"\'\)\s]+',
                lambda m: next((local for pid, local in PHOTO_ID_MAPPING.items() if pid in m.group(0)), "/images/main-banner.jpg"),
                new_content
            )

            # 2. 히어로 배너 CSS 배경 기본값 보정
            new_content = re.sub(
                r'url\([\'"]?/images/vendor[0-9]\.jpg[\'"]?\)',
                "url('/images/main-banner.jpg')",
                new_content
            )

            if new_content != content:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                count += 1
                print(f"✔ [{rel_path}] 로컬 이미지 경로 치환 완료")

print(f"\n🎉 총 {count}개의 HTML 파일 이미지 경로가 성공적으로 변경되었습니다!")