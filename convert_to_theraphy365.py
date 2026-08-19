# -*- coding: utf-8 -*-
import os
import re

print("🚀 테라피365 브랜드 변환 시작...")

# 1. 모든 HTML 파일 내 브랜드명을 '테라피365'로 일괄 치환
count = 0
for root, dirs, files in os.walk("."):
    for file in files:
        if not file.endswith(".html"):
            continue
        file_path = os.path.join(root, file)
        
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        content = content.replace("마사지몽", "테라피365")
        content = content.replace("스파루나", "테라피365")
        content = content.replace("MassageMong", "Theraphy365")
        content = content.replace("SpaLuna", "Theraphy365")
        content = content.replace("massagemong", "theraphy365")
        content = content.replace("spaluna", "theraphy365")
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        count += 1

print(f"✔ 총 {count}개 페이지의 브랜드명이 '테라피365'로 일괄 교체되었습니다.")
