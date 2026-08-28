# -*- coding: utf-8 -*-
import os
import re
import random

# ==============================================================================
# 1. 은평구 및 서울/경기/인천 누락 동 매핑 딕셔너리 완벽 보강
# ==============================================================================
EXTENDED_MAP = {
    # 은평구
    "eunpyeong": "은평구",
    "eungam": "응암동",
    "bulgwang": "불광동",
    "galhyeon": "갈현동",
    "gusan": "구산동",
    "daejo": "대조동",
    "yeokchon": "역촌동",
    "sinsa_ep": "신사동",
    "jeungsan": "증산동",
    "susaek": "수색동",
    "nokbeon": "녹번동",
    "jingwan": "진관동",

    # 금천구
    "geumcheon": "금천구",
    "gasan": "가산동",
    "doksan": "독산동",
    "siheung": "시흥동",

    # 구로구
    "guro": "구로구",
    "guro_dong": "구로동",
    "sindorim": "신도림동",
    "gaebong": "개봉동",
    "gocheok": "고척동",
    "oryu": "오류동",

    # 양천구
    "yangcheon": "양천구",
    "mokdong": "목동",
    "sinjeong": "신정동",
    "sinwol": "신월동",

    # 강서구
    "gangseo": "강서구",
    "gangse": "강서구",
    "hwagok": "화곡동",
    "magok": "마곡동",
    "balsan": "발산동",
    "gayang": "가양동",
    "banghwa": "방화동",
    "deungchon": "등촌동",

    # 마포구
    "mapo": "마포구",
    "hongdae": "홍대",
    "hapjeong": "합정동",
    "sinchon": "신촌",
    "yeonnam": "연남동",
    "mangwon": "망원동",
    "sangam": "상암동",
    "gongdeok": "공덕동",
    "seogyo": "서교동",

    # 서대문구
    "seodaemun": "서대문구",
    "sinchon_sdm": "신촌",
    "yeonhui": "연희동",
    "hongje": "홍제동",
    "hongeun": "홍은동",
    "namgajwa": "남가좌동",
    "bukgajwa": "북가좌동",

    # 종로/중구/용산
    "jongno": "종로구",
    "hyehwa": "혜화동",
    "pyeongchang": "평창동",
    "junggu": "중구",
    "myeongdong": "명동",
    "euljiro": "을지로",
    "dongdaemun_jg": "동대문",
    "yongsan": "용산구",
    "itaewon": "이태원",
    "hannam": "한남동",
    "huam": "후암동",
    "ichon": "이촌동",

    # 강남 3구 & 강동
    "gangnam": "강남구",
    "yeoksam": "역삼동",
    "nonhyeon": "논현동",
    "samseong": "삼성동",
    "daechi": "대치동",
    "cheongdam": "청담동",
    "apgujeong": "압구정동",
    "seocho": "서초구",
    "seocho_dong": "서초동",
    "banpo": "반포동",
    "bangbae": "방배동",
    "yangjae": "양재동",
    "jamwon": "잠원동",
    "songpa": "송파구",
    "jamsil": "잠실동",
    "garak": "가락동",
    "munjeong": "문정동",
    "bangi": "방이동",
    "gangdong": "강동구",
    "cheonho": "천호동",
    "gil": "길동",
    "amsa": "암사동",
    "myeongil": "명일동",
    "seongnae": "성내동",

    # 영등포/동작/관악
    "yeongdeungpo": "영등포구",
    "yeouido": "여의도",
    "dangsan": "당산동",
    "mullae": "문래동",
    "dongjak": "동작구",
    "noryangjin": "노량진",
    "sangdo": "상도동",
    "sadang": "사당동",
    "gwanak": "관악구",
    "sillim": "신림동",
    "bongcheon": "봉천동"
}

# 템플릿 로드 (gangnam/index.html 기준)
template_file = "gangnam/index.html"
if not os.path.exists(template_file):
    template_file = "yongsan/index.html"

with open(template_file, "r", encoding="utf-8", errors="ignore") as f:
    base_template = f.read()

# ==============================================================================
# 2. 각 구 디렉토리 내에 빠진 동 HTML 파일 자동 생성
# ==============================================================================
# 각 구별 주요 동 리스트 정의
GU_DONG_MAP = {
    "eunpyeong": [("eungam", "응암동"), ("bulgwang", "불광동"), ("galhyeon", "갈현동"), ("daejo", "대조동"), ("yeokchon", "역촌동"), ("nokbeon", "녹번동"), ("jingwan", "진관동")],
    "geumcheon": [("gasan", "가산동"), ("doksan", "독산동"), ("siheung", "시흥동")],
    "guro": [("guro_dong", "구로동"), ("sindorim", "신도림동"), ("gaebong", "개봉동"), ("gocheok", "고척동"), ("oryu", "오류동")],
    "yangcheon": [("mokdong", "목동"), ("sinjeong", "신정동"), ("sinwol", "신월동")],
    "gangseo": [("hwagok", "화곡동"), ("magok", "마곡동"), ("balsan", "발산동"), ("gayang", "가양동"), ("banghwa", "방화동"), ("deungchon", "등촌동")],
    "seodaemun": [("sinchon_sdm", "신촌"), ("yeonhui", "연희동"), ("hongje", "홍제동"), ("hongeun", "홍은동"), ("namgajwa", "남가좌동")],
    "mapo": [("hongdae", "홍대"), ("hapjeong", "합정동"), ("sinchon", "신촌"), ("yeonnam", "연남동"), ("mangwon", "망원동"), ("sangam", "상암동"), ("gongdeok", "공덕동")],
    "yongsan": [("itaewon", "이태원"), ("hannam", "한남동"), ("huam", "후암동"), ("ichon", "이촌동")],
    "gangnam": [("yeoksam", "역삼동"), ("nonhyeon", "논현동"), ("samseong", "삼성동"), ("daechi", "대치동"), ("cheongdam", "청담동"), ("apgujeong", "압구정동")],
    "seocho": [("seocho_dong", "서초동"), ("banpo", "반포동"), ("bangbae", "방배동"), ("yangjae", "양재동"), ("jamwon", "잠원동")],
    "songpa": [("jamsil", "잠실동"), ("garak", "가락동"), ("munjeong", "문정동"), ("bangi", "방이동")],
    "gangdong": [("cheonho", "천호동"), ("gil", "길동"), ("amsa", "암사동"), ("myeongil", "명일동"), ("seongnae", "성내동")],
    "yeongdeungpo": [("yeouido", "여의도"), ("dangsan", "당산동"), ("mullae", "문래동")],
    "dongjak": [("noryangjin", "노량진"), ("sangdo", "상도동"), ("sadang", "사당동")],
    "gwanak": [("sillim", "신림동"), ("bongcheon", "봉천동")]
}

created_count = 0
for gu_folder, dongs in GU_DONG_MAP.items():
    os.makedirs(gu_folder, exist_ok=True)
    gu_name = EXTENDED_MAP.get(gu_folder, gu_folder)
    
    for dong_key, dong_name in dongs:
        dong_file_path = os.path.join(gu_folder, f"{dong_key}.html")
        
        # 동 전용 페이지 생성
        dong_html = base_template
        dong_html = dong_html.replace("강남구", f"{gu_name} {dong_name}").replace("강남", f"{gu_name} {dong_name}")
        dong_html = dong_html.replace("gangnam", gu_folder)
        
        # 제목 및 타이틀 교체
        full_loc = f"{gu_name} {dong_name}"
        dong_html = re.sub(r'<title>.*?</title>', f'<title>{full_loc} 출장마사지 24시 VIP 홈케어 & 프리미엄 스파 - 테라피365</title>', dong_html, flags=re.IGNORECASE)
        dong_html = re.sub(r'<h2>.*?</h2>', f'<h2>{full_loc} 출장마사지 & 홈타이 추천 제휴처 TOP 5</h2>', dong_html, count=1, flags=re.IGNORECASE)
        
        with open(dong_file_path, "w", encoding="utf-8") as f:
            f.write(dong_html)
        created_count += 1

print(f"✔ 총 {created_count}개 세부 동 HTML 파일 생성/복구 완료")

# ==============================================================================
# 3. 전체 사이트 내 영문 표기 한글로 일괄 치환 및 메타태그 재적용
# ==============================================================================
for root, dirs, files in os.walk("."):
    if any(part.startswith(".") for part in root.split(os.sep)):
        continue
    for file in files:
        if not file.endswith(".html"):
            continue
        file_path = os.path.join(root, file)
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            c = f.read()
        
        # 잘못 표기된 영문 동 이름 한글 치환
        for eng_k, kor_v in EXTENDED_MAP.items():
            c = c.replace(f"Eunpyeong {eng_k.capitalize()}", f"은평구 {kor_v}")
            c = c.replace(f"eunpyeong {eng_k}", f"은평구 {kor_v}")
            c = c.replace(f"{eng_k.capitalize()} 출장마사지", f"{kor_v} 출장마사지")
            c = c.replace(f">{eng_k.capitalize()}<", f">{kor_v}<")
            c = c.replace(f">{eng_k}<", f">{kor_v}<")
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(c)

print("✔ 전체 HTML 내 영문 지역명 한글 정규화 완료")
