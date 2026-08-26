# -*- coding: utf-8 -*-
import os
import re

# 1. 영문 구/동 완벽 매핑 딕셔너리
NAME_MAP = {
    # 서울 구
    "seoul": "서울", "gangnam": "강남구", "seocho": "서초구", "songpa": "송파구", "gangdong": "강동구",
    "mapo": "마포구", "yongsan": "용산구", "seodaemun": "서대문구", "eunpyeong": "은평구",
    "jongno": "종로구", "junggu": "중구", "jungnang": "중랑구", "seongbuk": "성북구",
    "gangbuk": "강북구", "dobong": "도봉구", "nowon": "노원구", "seongdong": "성동구",
    "gwangjin": "광진구", "dongdaemun": "동대문구", "yeongdeungpo": "영등포구",
    "guro": "구로구", "geumcheon": "금천구", "yangcheon": "양천구", "gangse": "강서구",
    "gangseo": "강서구", "dongjak": "동작구", "gwanak": "관악구",

    # 서울 동
    "bangbae": "방배동", "banpo": "반포동", "yangjae": "양재동", "jamwon": "잠원동", "naegok": "내곡동",
    "mia": "미아동", "suyu": "수유동", "beon": "번동", "beondong": "번동", "ui": "우이동", "samgaksan": "삼각산동",
    "ichon": "이촌동", "itaewon": "이태원동", "hannam": "한남동", "huam": "후암동", "cheongpa": "청파동", "wonhyo": "원효로동",
    "yeoksam": "역삼동", "samseong": "삼성동", "cheongdam": "청담동", "sinsa": "신사동", "nonhyeon": "논현동", "daechi": "대치동", "dogok": "도곡동", "apgujeong": "압구정동", "gaepo": "개포동", "segok": "세곡동", "irwon": "일원동", "suseo": "수서동",
    "jamsil": "잠실동", "sincheon": "신천동", "munjeong": "문정동", "garak": "가락동", "bangi": "방이동", "ogum": "오금동", "geoyeo": "거여동", "macheon": "마천동", "pungnap": "풍납동", "jangji": "장지동",
    "cheonho": "천호동", "gildong": "길동", "dunchon": "둔촌동", "myeongil": "명일동", "godeok": "고덕동", "amasa": "암사동", "gangil": "강일동", "seongnae": "성내동",
    "hongdae": "홍대", "seogyo": "서교동", "hapjeong": "합정동", "sangam": "상암동", "gongdeok": "공덕동", "yeonnam": "연남동", "mangwon": "망원동", "ahyeon": "아현동",
    "yeouido": "여의도동", "yeongdeungpodong": "영등포동", "dangsan": "당산동", "mullae": "문래동", "singil": "신길동", "daerim": "대림동", "yangpyeong": "양평동",
    "sanggye": "상계동", "junggye": "중계동", "hagye": "하계동", "gongneung": "공릉동", "wolgye": "월계동",
    "magok": "마곡동", "hwagok": "화곡동", "gayang": "가양동", "balsan": "발산동", "banghwa": "방화동", "deungchon": "등촌동", "yeomchang": "염창동",
    "gurodong": "구로동", "sindorim": "신도림동", "gaebong": "개봉동", "oryu": "오류동", "hangdong": "항동", "gocheok": "고척동",
    "sillim": "신림동", "bongcheon": "봉천동", "nakseongdae": "낙성대동",
    "guui": "구의동", "jayang": "자양동", "gunja": "군자동", "junggok": "중곡동", "hwayang": "화양동",
    "seongsu": "성수동", "wangsimni": "왕십리동", "haengdang": "행당동", "geumho": "금호동", "oksu": "옥수동",
    "cheongnyangni": "청량리동", "dapsimni": "답십리동", "jangan": "장안동", "jeonnong": "전농동", "hoegi": "회기동", "imun": "이문동",
    "noryangjin": "노량진동", "sangdo": "상도동", "sadang": "사당동", "heukseok": "흑석동", "daebang": "대방동", "sindaebang": "신대방동",
    "sinchon": "신촌동", "yeonhui": "연희동", "hongje": "홍제동", "bukgajwa": "북가좌동", "namgajwa": "남가좌동", "hongun": "홍은동",
    "bulgwang": "불광동", "galhyeon": "갈현동", "eungam": "응암동", "yeonsinnae": "연신내", "nokbeon": "녹번동", "daejo": "대조동", "susaek": "수색동", "jingwan": "진관동",
    "jongno_dong": "종로", "hyehwa": "혜화동", "pyeongchang": "평창동", "samcheong": "삼청동", "muak": "무악동",
    "myeongdong": "명동", "euljiro": "을지로", "sindang": "신당동", "hoehyeon": "회현동",
    "gireum": "길음동", "donam": "돈암동", "anam": "안암동", "jangwi": "장위동", "seokgwan": "석관동",
    "myeonmok": "면목동", "sangbong": "상봉동", "junghwa": "중화동", "mukdong": "묵동", "sinnae": "신내동",
    "changdong": "창동", "ssangmun": "쌍문동", "banghak": "방학동", "dobong_dong": "도봉동",
    "mokdong": "목동", "sinjeong": "신정동", "sinwol": "신월동",
    "gasan": "가산동", "doksan": "독산동",

    # 인천 / 경기
    "incheon_bupyeong": "인천 부평구", "incheon_namdong": "인천 남동구", "incheon_yeonsu": "인천 연수구",
    "incheon_michuhol": "인천 미추홀구", "incheon_seogu": "인천 서구", "incheon_gyeyang": "인천 계양구",
    "incheon_junggu": "인천 중구", "incheon_donggu": "인천 동구",
    "suwon": "수원시", "suwon_paldal": "수원 팔달구", "suwon_yeongtong": "수원 영통구", "suwon_jangan": "수원 장안구", "suwon_gwonseon": "수원 권선구",
    "seongnam": "성남시", "seongnam_bundang": "성남 분당구", "seongnam_sujeong": "성남 수정구", "seongnam_jungwon": "성남 중원구",
    "goyang": "고양시", "goyang_ilsandong": "고양 일산동구", "goyang_ilsanseo": "고양 일산서구", "goyang_deogyang": "고양 덕양구",
    "yongin": "용인시", "yongin_suji": "용인 수지구", "yongin_giheung": "용인 기흥구", "yongin_cheoin": "용인 처인구",
    "anyang": "안양시", "ansan": "안산시", "bucheon": "부천시", "hwaseong": "화성시", "pyeongtaek": "평택시", "siheung": "시흥시",
    "gimpo": "김포시", "paju": "파주시", "namyangju": "남양주시", "uijeongbu": "의정부시", "hanam": "하남시", "gwangmyeong": "광명시",
    "gunpo": "군포시", "guri": "구리시", "osan": "오산시", "gwangju_gyeonggi": "경기 광주시", "icheon": "이천시", "yangju": "양주시", "uiwang": "의왕시", "anseong": "안성시"
}

def get_full_korean_name(rel_path):
    parts = rel_path.replace("\\", "/").split("/")
    folder = parts[0]
    file_name = parts[-1].replace(".html", "")
    
    folder_kr = NAME_MAP.get(folder, folder)
    
    if len(parts) == 2 and parts[1] == "index.html":
        return folder_kr
    
    file_kr = NAME_MAP.get(file_name, file_name)
    return f"{folder_kr} {file_kr}" if folder_kr != file_kr else folder_kr

count = 0

for root, dirs, files in os.walk("."):
    if any(part.startswith(".") for part in root.split(os.sep)):
        continue

    for file in files:
        if not file.endswith(".html"):
            continue

        file_path = os.path.join(root, file)
        rel_path = os.path.relpath(file_path, ".").replace("\\", "/")
        
        # 메인 루트 index.html만 정확히 제외 (서브 폴더 index.html은 정상 처리)
        if rel_path == "index.html":
            continue
        
        loc_name = get_full_korean_name(rel_path)
        
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        # 1. <title> 최적화 ('출장마사지' 붙여쓰기 적용)
        content = re.sub(
            r'<title>.*?</title>', 
            f'<title>{loc_name} 출장마사지 1등 홈타이 힐링 테라피 | 테라피365</title>', 
            content, flags=re.DOTALL | re.IGNORECASE
        )

        # 2. 메타 description & OpenGraph Description 최적화
        desc_text = f"{loc_name} 전지역 출장마사지 & 홈타이 24시 빠른 방문 서비스. 100% 후불제 안심 케어와 프리미엄 스파 테라피 코스 안내."
        if '<meta name="description"' in content:
            content = re.sub(r'<meta[^>]*name=["\']description["\'][^>]*content=["\'][^"\']*["\'][^>]*>', 
                             f'<meta name="description" content="{desc_text}">', content, flags=re.IGNORECASE)
        
        # 3. Open Graph Title & Description
        content = re.sub(r'<meta\s+property=["\']og:title["\'][^>]*>', 
                         f'<meta property="og:title" content="{loc_name} 출장마사지 | 24시 프리미엄 힐링 홈케어 - 테라피365">', content, flags=re.IGNORECASE)
        content = re.sub(r'<meta\s+property=["\']og:description["\'][^>]*>', 
                         f'<meta property="og:description" content="{desc_text}">', content, flags=re.IGNORECASE)

        # 4. <h1> 태그 치환 (헤더 로고 또는 메인 타이틀)
        content = re.sub(
            r'<h1>.*?</h1>', 
            f'<h1>{loc_name} 출장마사지 <span>프리미엄 24시 방문 케어</span></h1>', 
            content, flags=re.DOTALL | re.IGNORECASE
        )

        # 5. 히어로 배너 <h2> 치환
        content = re.sub(
            r'<h2>(?:.*?맞춤 프라이빗 힐링 서비스|365일 지친 일상 속.*?)</h2>', 
            f'<h2>{loc_name} 맞춤 프라이빗 힐링 서비스</h2>', 
            content, flags=re.DOTALL | re.IGNORECASE
        )

        # 6. 추천 매장 섹션 제목 치환
        content = re.sub(
            r'<h2>(?:테라피365 엄선 제휴 매장 TOP 5|.*?추천.*?TOP 5.*?)</h2>', 
            f'<h2>{loc_name} 출장마사지 & 홈타이 추천 제휴처 TOP 5</h2>', 
            content, flags=re.DOTALL | re.IGNORECASE
        )

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

        count += 1
        print(f"✔ [{rel_path}] -> {loc_name} 완벽 한글화 및 출장마사지 SEO 키워드 적용")

print(f"\n🎉 총 {count}개 서브페이지의 헤더, 타이틀, 메타태그가 네이버 검색 로직에 맞게 완벽 한글화되었습니다!")