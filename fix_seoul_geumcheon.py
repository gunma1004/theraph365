# -*- coding: utf-8 -*-
import os
import re

# 기준이 될 템플릿 파일(yongsan/index.html 또는 gangnam/index.html) 읽기
template_path = "yongsan/index.html"
if not os.path.exists(template_path):
    template_path = "gangnam/index.html"

with open(template_path, "r", encoding="utf-8", errors="ignore") as f:
    base_html = f.read()

# ==============================================================================
# 1. 금천구(geumcheon/index.html) 정밀 생성
# ==============================================================================
os.makedirs("geumcheon", exist_ok=True)
gc_html = base_html

# 용산 관련 키워드를 금천구로 치환
gc_html = gc_html.replace("용산구", "금천구").replace("용산", "금천")
gc_html = gc_html.replace("yongsan", "geumcheon")

# 금천구 주요 동 교체 (이태원, 한남동, 후암동 등 -> 가산동, 독산동, 시흥동)
gc_html = gc_html.replace("이태원동", "가산동").replace("이태원", "가산동")
gc_html = gc_html.replace("한남동", "독산동").replace("한남", "독산동")
gc_html = gc_html.replace("후암동", "시흥동").replace("후암", "시흥동")
gc_html = gc_html.replace("itaewon", "gasan").replace("hannam", "doksan").replace("huam", "siheung")

with open("geumcheon/index.html", "w", encoding="utf-8") as f:
    f.write(gc_html)
print("✔ [geumcheon/index.html] 금천구 페이지 생성 완료")

# ==============================================================================
# 2. 서울 전지역(seoul/index.html) 기존 테마 기반 생성
# ==============================================================================
os.makedirs("seoul", exist_ok=True)
seoul_html = base_html

# 지역명을 서울 전지역으로 치환
seoul_html = seoul_html.replace("용산구", "서울 전지역").replace("용산", "서울")
seoul_html = seoul_html.replace("yongsan", "seoul")

# 서울 25개 구 링크 그리드로 동 영역 치환 (있는 경우)
gu_list = [
    ("gangnam", "강남구"), ("seocho", "서초구"), ("songpa", "송파구"), ("gangdong", "강동구"),
    ("mapo", "마포구"), ("yongsan", "용산구"), ("seodaemun", "서대문구"), ("eunpyeong", "은평구"),
    ("jongno", "종로구"), ("junggu", "중구"), ("jungnang", "중랑구"), ("seongbuk", "성북구"),
    ("gangbuk", "강북구"), ("dobong", "도봉구"), ("nowon", "노원구"), ("seongdong", "성동구"),
    ("gwangjin", "광진구"), ("dongdaemun", "동대문구"), ("yeongdeungpo", "영등포구"),
    ("guro", "구로구"), ("geumcheon", "금천구"), ("yangcheon", "양천구"), ("gangseo", "강서구"),
    ("dongjak", "동작구"), ("gwanak": "관악구")
]

with open("seoul/index.html", "w", encoding="utf-8") as f:
    f.write(seoul_html)
print("✔ [seoul/index.html] 서울 전지역 페이지 생성 완료")
