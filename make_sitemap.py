# -*- coding: utf-8 -*-
import os

BASE_DOMAIN = "https://theraphy365.pages.dev"

# 1. 경기/인천 지역 데이터 (build_capital_area.py와 동일한 구조)
DETAILED_REGIONS = {
    "incheon_bupyeong": [
        "bupyeong", "sanggok", "cheongcheon", "galsan", "sipjeong", "bugae", "samsan"
    ],
    "incheon_namdong": [
        "guwol", "ganseok", "mansu", "nonhyeon_incheon", "seochang", "dorim"
    ],
    "incheon_yeonsu": [
        "songdo", "yeonsu", "dongchun", "cheonghak", "okryeon", "seonhak"
    ],
    "incheon_michuhol": [
        "juan", "yonghyeon", "hakik", "dohwa", "sungui", "gwangyo"
    ],
    "incheon_seogu": [
        "cheongna", "geomdan", "luwon", "gajeong", "seoknam", "yeonhui", "dangha", "majeon"
    ],
    "incheon_gyeyang": [
        "gyeyang", "jakjeon", "hyoseong", "gyesan", "seoun"
    ],
    "incheon_junggu": [
        "yeongjong", "unseo", "jungsan", "sinpo", "dongincheon"
    ],
    "incheon_donggu": [
        "songhyeon", "songrim", "manseok", "hwasu"
    ],
    "suwon_paldal": [
        "ingye", "haenggung", "hwaseo", "ji-dong", "maesan"
    ],
    "suwon_yeongtong": [
        "gwanggyo", "yeongtong", "mangpo", "maetan", "woncheon"
    ],
    "suwon_jangan": [
        "jeongja", "jo-won", "yuljeon", "cheoncheon", "yeonmu"
    ],
    "suwon_gwonseon": [
        "gwonseon", "gosaek", "homaesil", "seriu", "geumgok"
    ],
    "seongnam_bundang": [
        "seohyeon", "yatap", "jeongja", "pangyo", "baekhyeon", "sunae", "ime", "gumi", "unjoong"
    ],
    "seongnam_sujeong": [
        "wirye", "sinheung", "taepyeong", "sanseong", "bokjeong", "sujin"
    ],
    "seongnam_jungwon": [
        "moran", "seongnam_dong", "sangdaewon", "hagdaewon", "geumgwang", "bank"
    ],
    "goyang_ilsandong": [
        "baekseok", "madu", "janghang", "jeongbalsan", "siksa", "pungsan"
    ],
    "goyang_ilsanseo": [
        "juyeop", "daehwa", "tanhyun", "ilsan", "songsan", "deogi"
    ],
    "goyang_deogyang": [
        "hwajeong", "haengsin", "samsong", "wonheung", "hyangdong", "deogeun", "wondang"
    ],
    "yongin_suji": [
        "pungdeokcheon", "jookjeon", "dongcheon", "sanghyeon", "shinbong", "sungbok"
    ],
    "yongin_giheung": [
        "dongbaek", "singal", "gugal", "bora", "seonong", "guseong", "mabuk"
    ],
    "yongin_cheoin": [
        "kimryangjang", "yeokbuk", "samga", "pogok", "mohan", "yangji"
    ],
    "anyang_dongan": [
        "pyeongchon", "beomgye", "indeogwon", "gwanyang", "hogye", "bisan"
    ],
    "anyang_manan": [
        "anyang_dong", "seoksu", "bakdal"
    ],
    "ansan_danwon": [
        "gojan", "jungang", "chogi", "wongok", "seonbu", "daebu"
    ],
    "ansan_sangnok": [
        "bono", "sadong", "wolpi", "seongpo", "il-dong", "i-dong"
    ],
    "bucheon": [
        "jungdong", "sangdong", "sinjungdong", "sosa", "wonmi", "ojeong", "yeokgok", "gogang"
    ],
    "hwaseong": [
        "dongtan", "dongtan2", "byeongjeom", "hyangnam", "bongdam", "namyang", "saesol", "jinjoo"
    ],
    "pyeongtaek": [
        "godeok", "bijeon", "songtan", "anjeong", "anseok", "poseung", "cheongbuk", "sejeong"
    ],
    "siheung": [
        "baegot", "jeongwang", "eunhaeng", "mokgam", "daeya", "sinhyeon", "neunggok", "janghyeon"
    ],
    "gimpo": [
        "gurae", "unyang", "janggi", "pungmu", "sau", "masan", "gochon", "tongjin"
    ],
    "paju": [
        "unjeong", "geumchon", "munsan", "gyoha", "yadang", "dongpae"
    ],
    "namyangju": [
        "dasang", "byeolnae", "pyeongnae", "hopyeong", "jinjeop", "wabu", "onam", "hwado"
    ],
    "uijeongbu": [
        "uijeongbu_dong", "howon", "singok", "minrak", "gosan", "ganeung", "geumo"
    ],
    "hanam": [
        "misa", "wirye_hanam", "gamil", "deokpung", "sinjang", "pungcheon"
    ],
    "gwangmyeong": [
        "cheolsan", "gwangmyeong_dong", "soha", "iljik", "haan"
    ],
    "gunpo": [
        "sanbon", "geumjeong", "dang-dong", "daeyami", "bugok"
    ],
    "guri": [
        "sutaek", "inmae", "galmae", "gyomun", "achasan"
    ],
    "osan": [
        "won-dong", "seggyo", "gweol", "osandong", "eunjeong"
    ],
    "gwangju_gyeonggi": [
        "gyeongan", "taejeon", "opocheup", "sinhyun", "neungpyeong", "tanbeol"
    ],
    "icheon": [
        "changjeon", "jeungpo", "bubal", "majung", "anheung"
    ],
    "yangju": [
        "okjeong", "goeup", "deokgye", "baekseok_yangju"
    ],
    "uiwang": [
        "poil", "naeson", "gojeon", "sam-dong"
    ],
    "anseong": [
        "gongdo", "daedeok", "anseong_dong", "boggae"
    ]
}

CITY_LIST = ["suwon", "seongnam", "goyang", "yongin", "anyang", "ansan"]

urls = []

# 1. 메인 홈페이지 추가
urls.append(f"{BASE_DOMAIN}/")

# 2. 서울 전지역 및 금천구(-massage 적용) 추가
urls.append(f"{BASE_DOMAIN}/seoul/")
urls.append(f"{BASE_DOMAIN}/geumcheon-massage/")

# 3. 경기 주요 시 폴더 추가
for city in CITY_LIST:
    urls.append(f"{BASE_DOMAIN}/{city}/")

# 4. 경기/인천 구 폴더 및 세부 동 페이지 (-massage 적용) 추가
for gu_folder, dongs in DETAILED_REGIONS.items():
    gu_url_folder = f"{gu_folder}-massage"
    # 구 index 페이지
    urls.append(f"{BASE_DOMAIN}/{gu_url_folder}/")
    # 세부 동 페이지
    for dong in dongs:
        urls.append(f"{BASE_DOMAIN}/{gu_url_folder}/{dong}.html")

# ==============================================================================
# A. sitemap.xml 생성
# ==============================================================================
sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
sitemap_xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

for url in urls:
    sitemap_xml += '  <url>\n'
    sitemap_xml += f'    <loc>{url}</loc>\n'
    sitemap_xml += '    <changefreq>daily</changefreq>\n'
    sitemap_xml += '    <priority>0.8</priority>\n'
    sitemap_xml += '  </url>\n'

sitemap_xml += '</urlset>'

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap_xml)

# ==============================================================================
# B. urllist.txt 생성
# ==============================================================================
with open("urllist.txt", "w", encoding="utf-8") as f:
    for url in urls:
        f.write(url + "\n")

print(f"🎉 총 {len(urls)}개의 URL이 포함된 새로운 sitemap.xml 및 urllist.txt가 완벽히 생성되었습니다!")