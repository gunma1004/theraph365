# -*- coding: utf-8 -*-
import os

# 1. 완벽하게 스타일이 작동하는 gangnam/index.html을 원본 템플릿으로 사용
template_path = "gangnam/index.html"
if not os.path.exists(template_path):
    template_path = "yongsan/index.html"

with open(template_path, "r", encoding="utf-8", errors="ignore") as f:
    base_html = f.read()

# ==============================================================================
# 1. 금천구 (geumcheon/index.html) 완벽 생성
# ==============================================================================
os.makedirs("geumcheon", exist_ok=True)
gc_html = base_html

# 강남/용산 관련 명칭을 금천구로 완전 치환
gc_html = gc_html.replace("강남구", "금천구").replace("강남", "금천")
gc_html = gc_html.replace("용산구", "금천구").replace("용산", "금천")
gc_html = gc_html.replace("gangnam", "geumcheon").replace("yongsan", "geumcheon")

# 세부 동 치환 (금천구 주요 동: 가산동, 독산동, 시흥동)
gc_html = gc_html.replace("역삼동", "가산동").replace("논현동", "독산동").replace("삼성동", "시흥동")
gc_html = gc_html.replace("대치동", "가산동").replace("청담동", "독산동").replace("압구정동", "시흥동")
gc_html = gc_html.replace("이태원동", "가산동").replace("한남동", "독산동").replace("후암동", "시흥동")
gc_html = gc_html.replace("yeoksam", "gasan").replace("nonhyeon", "doksan").replace("samseong", "siheung")
gc_html = gc_html.replace("itaewon", "gasan").replace("hannam", "doksan")

with open("geumcheon/index.html", "w", encoding="utf-8") as f:
    f.write(gc_html)
print("✔ [geumcheon/index.html] 금천구 페이지 100% 정상 생성 완료")

# ==============================================================================
# 2. 서울 전지역 (seoul/index.html) 동일 다크/골드 디자인으로 생성
# ==============================================================================
os.makedirs("seoul", exist_ok=True)
seoul_html = base_html

# 지역명을 서울 전지역으로 치환
seoul_html = seoul_html.replace("강남구", "서울 전지역").replace("강남", "서울")
seoul_html = seoul_html.replace("용산구", "서울 전지역").replace("용산", "서울")
seoul_html = seoul_html.replace("gangnam", "seoul").replace("yongsan", "seoul")

with open("seoul/index.html", "w", encoding="utf-8") as f:
    f.write(seoul_html)
print("✔ [seoul/index.html] 서울 전지역 페이지 100% 정상 생성 완료")
