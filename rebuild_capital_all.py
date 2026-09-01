# -*- coding: utf-8 -*-
import os
import random

BASE_DOMAIN = "https://theraphy365.pages.dev"

# ==============================================================================
# 20종 스팸 회피 세부 테마 키워드 풀
# ==============================================================================
THEME_KEYWORDS_20 = [
    "출장 힐링 마사지", "출장 홈케어 마사지", "출장 릴렉스 마사지", "출장 프리미엄 힐링 마사지", "출장 바디케어 마사지",
    "출장 아로마 마사지", "출장 스웨디시 마사지", "출장 에스테틱 마사지", "출장 오일 테라피 마사지", "출장 딥티슈 마사지",
    "출장 타이 마사지", "출장 홈타이 마사지", "출장 건식 테라피 마사지", "출장 스트레칭 마사지", "출장 지압 힐링 마사지",
    "출장 리커버리 마사지", "출장 피로회복 마사지", "출장 1:1 맞춤형 마사지", "출장 감성 테라피 마사지", "출장 웰니스 마사지"
]

DETAILED_REGIONS = {
    # -------------------------------------------------------------
    # [인천광역시 8개 구]
    # -------------------------------------------------------------
    "incheon_bupyeong": ("인천 부평구", [
        ("bupyeong", "부평동"), ("sanggok", "산곡동"), ("cheongcheon", "청천동"),
        ("galsan", "갈산동"), ("sipjeong", "십정동"), ("bugae", "부개동"), ("samsan", "삼산동")
    ]),
    "incheon_namdong": ("인천 남동구", [
        ("guwol", "구월동"), ("ganseok", "간석동"), ("mansu", "만수동"),
        ("nonhyeon_incheon", "논현동"), ("seochang", "서창동"), ("dorim", "도림동")
    ]),
    "incheon_yeonsu": ("인천 연수구", [
        ("songdo", "송도동"), ("yeonsu", "연수동"), ("dongchun", "동춘동"),
        ("cheonghak", "청학동"), ("okryeon", "옥련동"), ("seonhak", "선학동")
    ]),
    "incheon_michuhol": ("인천 미추홀구", [
        ("juan", "주안동"), ("yonghyeon", "용현동"), ("hakik", "학익동"),
        ("dohwa", "도화동"), ("sungui", "숭의동"), ("gwangyo", "관교동")
    ]),
    "incheon_seogu": ("인천 서구", [
        ("cheongna", "청라동"), ("geomdan", "검단"), ("luwon", "루원시티"),
        ("gajeong", "가정동"), ("seoknam", "석남동"), ("yeonhui", "연희동"),
        ("dangha", "당하동"), ("majeon", "마전동")
    ]),
    "incheon_gyeyang": ("인천 계양구", [
        ("gyeyang", "계양"), ("jakjeon", "작전동"), ("hyoseong", "효성동"),
        ("gyesan", "계산동"), ("seoun", "서운동")
    ]),
    "incheon_junggu": ("인천 중구", [
        ("yeongjong", "영종도"), ("unseo", "운서동"), ("jungsan", "중산동"),
        ("sinpo", "신포동"), ("dongincheon", "동인천")
    ]),
    "incheon_donggu": ("인천 동구", [
        ("songhyeon", "송현동"), ("songrim", "송림동"), ("manseok", "만석동"), ("hwasu", "화수동")
    ]),

    # -------------------------------------------------------------
    # [수원시 4개 구]
    # -------------------------------------------------------------
    "suwon_paldal": ("수원 팔달구", [
        ("ingye", "인계동"), ("haenggung", "행궁동"), ("hwaseo", "화서동"), ("ji-dong", "지동"), ("maesan", "매산동")
    ]),
    "suwon_yeongtong": ("수원 영통구", [
        ("gwanggyo", "광교"), ("yeongtong", "영통동"), ("mangpo", "망포동"), ("maetan", "매탄동"), ("woncheon", "원천동")
    ]),
    "suwon_jangan": ("수원 장안구", [
        ("jeongja", "정자동"), ("jo-won", "조원동"), ("yuljeon", "율전동"), ("cheoncheon", "천천동"), ("yeonmu", "연무동")
    ]),
    "suwon_gwonseon": ("수원 권선구", [
        ("gwonseon", "권선동"), ("gosaek", "고색동"), ("homaesil", "호매실동"), ("seriu", "세류동"), ("geumgok", "금곡동")
    ]),

    # -------------------------------------------------------------
    # [성남시 3개 구]
    # -------------------------------------------------------------
    "seongnam_bundang": ("성남 분당구", [
        ("seohyeon", "서현동"), ("yatap", "야탑동"), ("jeongja", "정자동"), ("pangyo", "판교"),
        ("baekhyeon", "백현동"), ("sunae", "수내동"), ("ime", "이매동"), ("gumi", "구미동"), ("unjoong", "운중동")
    ]),
    "seongnam_sujeong": ("성남 수정구", [
        ("wirye", "위례"), ("sinheung", "신흥동"), ("taepyeong", "태평동"),
        ("sanseong", "산성동"), ("bokjeong", "복정동"), ("sujin", "수진동")
    ]),
    "seongnam_jungwon": ("성남 중원구", [
        ("moran", "모란"), ("seongnam_dong", "성남동"), ("sangdaewon", "상대원동"),
        ("hagdaewon", "하대원동"), ("geumgwang", "금광동"), ("bank", "은행동")
    ]),

    # -------------------------------------------------------------
    # [고양시 3개 구]
    # -------------------------------------------------------------
    "goyang_ilsandong": ("고양 일산동구", [
        ("baekseok", "백석동"), ("madu", "마두동"), ("janghang", "장항동"),
        ("jeongbalsan", "정발산동"), ("siksa", "식사동"), ("pungsan", "풍산동")
    ]),
    "goyang_ilsanseo": ("고양 일산서구", [
        ("juyeop", "주엽동"), ("daehwa", "대화동"), ("tanhyun", "탄현동"),
        ("ilsan", "일산동"), ("songsan", "송산동"), ("deogi", "덕이동")
    ]),
    "goyang_deogyang": ("고양 덕양구", [
        ("hwajeong", "화정동"), ("haengsin", "행신동"), ("samsong", "삼송"),
        ("wonheung", "원흥"), ("hyangdong", "향동"), ("deogeun", "덕은"), ("wondang", "원당")
    ]),

    # -------------------------------------------------------------
    # [용인시 3개 구]
    # -------------------------------------------------------------
    "yongin_suji": ("용인 수지구", [
        ("pungdeokcheon", "풍덕천동"), ("jookjeon", "죽전동"), ("dongcheon", "동천동"),
        ("sanghyeon", "상현동"), ("shinbong", "신봉동"), ("sungbok", "성복동")
    ]),
    "yongin_giheung": ("용인 기흥구", [
        ("dongbaek", "동백동"), ("singal", "신갈동"), ("gugal", "구갈동"),
        ("bora", "보라동"), ("seonong", "서농동"), ("guseong", "구성"), ("mabuk", "마북동")
    ]),
    "yongin_cheoin": ("용인 처인구", [
        ("kimryangjang", "김량장동"), ("yeokbuk", "역북동"), ("samga", "삼가동"),
        ("pogok", "포곡"), ("mohan", "모현"), ("yangji", "양지")
    ]),

    # -------------------------------------------------------------
    # [안양시 / 안산시]
    # -------------------------------------------------------------
    "anyang_dongan": ("안양 동안구", [
        ("pyeongchon", "평촌동"), ("beomgye", "범계"), ("indeogwon", "인덕원"),
        ("gwanyang", "관양동"), ("hogye", "호계동"), ("bisan", "비산동")
    ]),
    "anyang_manan": ("안양 만안구", [
        ("anyang_dong", "안양동"), ("seoksu", "석수동"), ("bakdal", "박달동")
    ]),
    "ansan_danwon": ("안산 단원구", [
        ("gojan", "고잔동"), ("jungang", "중앙동"), ("chogi", "초지동"),
        ("wongok", "원곡동"), ("seonbu", "선부동"), ("daebu", "대부도")
    ]),
    "ansan_sangnok": ("안산 상록구", [
        ("bono", "본오동"), ("sadong", "사동"), ("wolpi", "월피동"),
        ("seongpo", "성포동"), ("il-dong", "일동"), ("i-dong", "이동")
    ]),

    # -------------------------------------------------------------
    # [경기도 주요 시 단위]
    # -------------------------------------------------------------
    "bucheon": ("부천시", [
        ("jungdong", "중동"), ("sangdong", "상동"), ("sinjungdong", "신중동"),
        ("sosa", "소사동"), ("wonmi", "원미동"), ("ojeong", "오정동"), ("yeokgok", "역곡동"), ("gogang", "고강동")
    ]),
    "hwaseong": ("화성시", [
        ("dongtan", "동탄1"), ("dongtan2", "동탄2"), ("byeongjeom", "병점"),
        ("hyangnam", "향남"), ("bongdam", "봉담"), ("namyang", "남양"), ("saesol", "새솔동"), ("jinjoo", "진안동")
    ]),
    "pyeongtaek": ("평택시", [
        ("godeok", "고덕"), ("bijeon", "비전동"), ("songtan", "송탄"),
        ("anjeong", "안정리"), ("anseok", "안중"), ("poseung", "포승"), ("cheongbuk", "청북"), ("sejeong", "세교동")
    ]),
    "siheung": ("시흥시", [
        ("baegot", "배곧동"), ("jeongwang", "정왕동"), ("eunhaeng", "은행동"),
        ("mokgam", "목감동"), ("daeya", "대야동"), ("sinhyeon", "신현동"), ("neunggok", "능곡동"), ("janghyeon", "장현동")
    ]),
    "gimpo": ("김포시", [
        ("gurae", "구래동"), ("unyang", "운양동"), ("janggi", "장기동"),
        ("pungmu", "풍무동"), ("sau", "사우동"), ("masan", "마산동"), ("gochon", "고촌"), ("tongjin", "통진")
    ]),
    "paju": ("파주시", [
        ("unjeong", "운정"), ("geumchon", "금촌동"), ("munsan", "문산"),
        ("gyoha", "교하"), ("yadang", "야당동"), ("dongpae", "동패동")
    ]),
    "namyangju": ("남양주시", [
        ("dasang", "다산동"), ("byeolnae", "별내동"), ("pyeongnae", "평내동"),
        ("hopyeong", "호평동"), ("jinjeop", "진접"), ("wabu", "와부"), ("onam", "오남"), ("hwado", "화도")
    ]),
    "uijeongbu": ("의정부시", [
        ("uijeongbu_dong", "의정부동"), ("howon", "호원동"), ("singok", "신곡동"),
        ("minrak", "민락동"), ("gosan", "고산동"), ("ganeung", "가능동"), ("geumo", "금오동")
    ]),
    "hanam": ("하남시", [
        ("misa", "미사"), ("wirye_hanam", "위례"), ("gamil", "감일"),
        ("deokpung", "덕풍동"), ("sinjang", "신장동"), ("pungcheon", "풍산동")
    ]),
    "gwangmyeong": ("광명시", [
        ("cheolsan", "철산동"), ("gwangmyeong_dong", "광명동"), ("soha", "소하동"), ("iljik", "일직동"), ("haan", "하안동")
    ]),
    "gunpo": ("군포시", [
        ("sanbon", "산본동"), ("geumjeong", "금정동"), ("dang-dong", "당동"), ("daeyami", "대야미"), ("bugok", "부곡동")
    ]),
    "guri": ("구리시", [
        ("sutaek", "수택동"), ("inmae", "인창동"), ("galmae", "갈매동"), ("gyomun", "교문동"), ("achasan", "아천동")
    ]),
    "osan": ("오산시", [
        ("won-dong", "원동"), ("seggyo", "세교"), ("gweol", "궐동"), ("osandong", "오산동"), ("eunjeong", "은계동")
    ]),
    "gwangju_gyeonggi": ("경기 광주시", [
        ("gyeongan", "경안동"), ("taejeon", "태전동"), ("opocheup", "오포"),
        ("sinhyun", "신현동"), ("neungpyeong", "능평동"), ("tanbeol", "탄벌동")
    ]),
    "icheon": ("이천시", [
        ("changjeon", "창전동"), ("jeungpo", "증포동"), ("bubal", "부발"), ("majung", "마장"), ("anheung", "안흥동")
    ]),
    "yangju": ("양주시", [
        ("okjeong", "옥정동"), ("goeup", "고읍동"), ("deokgye", "덕계동"), ("baekseok_yangju", "백석")
    ]),
    "uiwang": ("의왕시", [
        ("poil", "포일동"), ("naeson", "내손동"), ("gojeon", "고천동"), ("sam-dong", "삼동")
    ]),
    "anseong": ("안성시", [
        ("gongdo", "공도"), ("daedeok", "대덕"), ("anseong_dong", "안성동"), ("boggae", "보개")
    ])
}

CITY_MAP = {
    "suwon": ("수원시", [
        ("../suwon_paldal/index.html", "팔달구"), ("../suwon_yeongtong/index.html", "영통구"),
        ("../suwon_jangan/index.html", "장안구"), ("../suwon_gwonseon/index.html", "권선구")
    ]),
    "seongnam": ("성남시", [
        ("../seongnam_bundang/index.html", "분당구"), ("../seongnam_sujeong/index.html", "수정구"),
        ("../seongnam_jungwon/index.html", "중원구")
    ]),
    "goyang": ("고양시", [
        ("../goyang_ilsandong/index.html", "일산동구"), ("../goyang_ilsanseo/index.html", "일산서구"),
        ("../goyang_deogyang/index.html", "덕양구")
    ]),
    "yongin": ("용인시", [
        ("../yongin_suji/index.html", "수지구"), ("../yongin_giheung/index.html", "기흥구"),
        ("../yongin_cheoin/index.html", "처인구")
    ]),
    "anyang": ("안양시", [
        ("../anyang_dongan/index.html", "동안구"), ("../anyang_manan/index.html", "만안구")
    ]),
    "ansan": ("안산시", [
        ("../ansan_danwon/index.html", "단원구"), ("../ansan_sangnok/index.html", "상록구")
    ])
}

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{loc_full} {k1} & {k2} 1등 힐링 테라피 | 테라피365</title>
    <link rel="canonical" href="{canonical_url}">
    <meta name="description" content="{loc_full} 전지역 24시간 {k1} 및 {k2} 추천 TOP 5 안내. 30분 내 신속 방문 및 100% 후불제 안심 케어.">
    <meta name="keywords" content="{loc_full} {k1}, {loc_full} {k2}, {loc_full} {k3}, 테라피365, {k4}">
    <meta name="robots" content="index, follow">
    
    <meta property="og:type" content="website">
    <meta property="og:title" content="{loc_full} {k1} | 24시 프리미엄 힐링 홈케어 - 테라피365">
    <meta property="og:description" content="{loc_full} 전지역 24시간 {k1} 및 {k2} 추천 TOP 5 안내. 30분 내 신속 방문.">
    <meta property="og:url" content="{canonical_url}">
    <meta property="og:image" content="{base_domain}/images/main-banner.jpg">

    <style>
        :root {{
            --bg-dark: #0a0c10;
            --card-bg: #12151e;
            --card-hover: #181c28;
            --accent-gold: #e5b567;
            --accent-gold-light: #fbe3ad;
            --accent-red: #e74c3c;
            --accent-cyan: #00d2d3;
            --text-main: #f0f2f5;
            --text-sub: #9aa0a6;
            --border-color: #232938;
        }}

        * {{ margin: 0; padding: 0; box-sizing: border-box; font-family: 'Pretendard', 'Noto Sans KR', -apple-system, sans-serif; }}
        body {{ background-color: var(--bg-dark); color: var(--text-main); line-height: 1.65; padding-bottom: 50px; overflow-x: hidden; }}
        a {{ text-decoration: none; color: inherit; }}

        header {{
            background: rgba(18, 21, 30, 0.95);
            backdrop-filter: blur(10px);
            padding: 16px 20px;
            text-align: center;
            border-bottom: 1px solid rgba(229, 181, 103, 0.3);
            position: sticky;
            top: 0;
            z-index: 1000;
            box-shadow: 0 4px 20px rgba(0,0,0,0.6);
        }}
        .header-wrap {{ max-width: 900px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center; }}
        .logo-text {{ font-size: 1.4rem; font-weight: 800; color: #ffffff; }}
        .logo-text span {{ color: var(--accent-gold); }}
        .header-call {{
            background: linear-gradient(135deg, #e5b567, #c49746);
            color: #0a0c10;
            font-weight: 800;
            font-size: 0.85rem;
            padding: 7px 14px;
            border-radius: 20px;
        }}

        .hero-banner {{
            background: linear-gradient(180deg, rgba(10, 12, 16, 0.6) 0%, rgba(10, 12, 16, 0.95) 100%),
                        url('/images/main-banner.jpg') center/cover no-repeat;
            padding: 60px 20px 45px;
            text-align: center;
            border-bottom: 1px solid var(--border-color);
        }}
        .hero-badge {{
            display: inline-block;
            background: rgba(229, 181, 103, 0.15);
            border: 1px solid var(--accent-gold);
            color: var(--accent-gold-light);
            font-size: 0.78rem;
            font-weight: 700;
            padding: 4px 12px;
            border-radius: 20px;
            margin-bottom: 12px;
        }}
        .hero-banner h1 {{
            font-size: 1.85rem;
            font-weight: 800;
            line-height: 1.35;
            margin-bottom: 10px;
            background: linear-gradient(135deg, #ffffff 40%, var(--accent-gold-light) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        .hero-banner p {{ font-size: 0.95rem; color: var(--text-sub); }}

        .container {{ max-width: 900px; margin: 0 auto; padding: 20px 15px; }}
        .nav-bar {{ display: flex; gap: 10px; margin-bottom: 25px; }}
        .home-btn {{ background: #161a25; border: 1px solid var(--border-color); color: #e1e3e8; padding: 8px 14px; border-radius: 6px; font-size: 0.85rem; font-weight: 600; }}
        .home-btn:hover {{ border-color: var(--accent-gold); color: var(--accent-gold); }}

        .section-header {{
            margin: 30px 0 20px;
            border-left: 4px solid var(--accent-gold);
            padding-left: 12px;
        }}
        .section-header h2 {{ font-size: 1.3rem; color: #ffffff; font-weight: 800; }}
        .section-header p {{ font-size: 0.85rem; color: var(--text-sub); }}

        .vendor-card {{
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 14px;
            overflow: hidden;
            margin-bottom: 24px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.35);
        }}
        .vendor-thumb-wrap {{ position: relative; width: 100%; height: 220px; overflow: hidden; }}
        .vendor-img {{ width: 100%; height: 100%; object-fit: cover; }}
        .vendor-tag-float {{
            position: absolute;
            top: 14px;
            left: 14px;
            background: rgba(10, 12, 16, 0.85);
            backdrop-filter: blur(5px);
            border: 1px solid var(--accent-gold);
            color: var(--accent-gold);
            font-size: 0.75rem;
            font-weight: bold;
            padding: 4px 8px;
            border-radius: 6px;
        }}
        .vendor-body {{ padding: 20px; }}
        .vendor-header-flex {{ display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border-color); padding-bottom: 12px; margin-bottom: 15px; flex-wrap: wrap; gap: 8px; }}
        .vendor-title-group {{ display: flex; align-items: center; gap: 8px; }}
        .vendor-rank {{ background: linear-gradient(135deg, var(--accent-red), #c0392b); color: #fff; font-size: 0.75rem; font-weight: 800; padding: 4px 8px; border-radius: 6px; }}
        .vendor-title {{ font-size: 1.25rem; color: #ffffff; font-weight: 800; }}
        .vendor-tagline {{ color: var(--accent-cyan); font-size: 0.85rem; font-weight: 600; width: 100%; margin-top: 4px; }}

        .info-grid {{ display: grid; grid-template-columns: 1fr; gap: 8px; margin-bottom: 18px; }}
        .info-row {{ display: flex; font-size: 0.9rem; }}
        .info-label {{ width: 90px; color: var(--accent-gold); font-weight: 700; flex-shrink: 0; }}
        .info-content {{ color: #c3c7d2; }}

        .btn-call {{
            background: linear-gradient(135deg, #e5b567 0%, #b88628 100%);
            color: #0a0c10;
            font-weight: 800;
            font-size: 1rem;
            padding: 13px;
            border-radius: 8px;
            text-align: center;
            display: block;
        }}

        .gu-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(110px, 1fr)); gap: 8px; margin-top: 15px; }}
        .gu-item {{ background: #161a25; border: 1px solid var(--border-color); padding: 10px 6px; text-align: center; border-radius: 6px; font-size: 0.85rem; color: #e1e3e8; font-weight: 600; display: block; }}
        .gu-item:hover {{ border-color: var(--accent-gold); color: var(--accent-gold); }}

        footer {{ text-align: center; padding: 25px 20px; font-size: 0.8rem; color: #7f8c8d; border-top: 1px solid var(--border-color); margin-top: 30px; }}
    </style>
</head>
<body>
    <header>
        <div class="header-wrap">
            <div class="logo-text">테라피<span>365</span></div>
            <a href="tel:0507-1280-3223" class="header-call">📞 24시 실시간 예약</a>
        </div>
    </header>

    <div class="hero-banner">
        <div class="hero-badge">PREMIUM HOME HEALING CARE</div>
        <h1>{loc_full} {k1} & {k2}</h1>
        <p>{loc_full} 전 지역 30분 안심 빠른 방문 테라피 서비스</p>
    </div>

    <div class="container">
        <div class="nav-bar">
            <a href="../index.html" class="home-btn">🏠 전체 메인</a>
            <a href="index.html" class="home-btn">📍 {parent_kr} 메인</a>
        </div>

        <div class="section-header">
            <h2>{loc_full} {k1} & {k2} 추천 TOP 5</h2>
            <p>엄선된 프리미엄 관리사 100% 후불제 힐링 서비스</p>
        </div>

        <!-- 1번 업체: 기쁨조 테라피 -->
        <div class="vendor-card">
            <div class="vendor-thumb-wrap">
                <img src="/images/vendor1.jpg" alt="{loc_full} {k1} 기쁨조 테라피" class="vendor-img">
                <div class="vendor-tag-float">👑 최우수 만족도 매장</div>
            </div>
            <div class="vendor-body">
                <div class="vendor-header-flex">
                    <div class="vendor-title-group">
                        <span class="vendor-rank">추천 01</span>
                        <span class="vendor-title">기쁨조 테라피</span>
                    </div>
                    <div class="vendor-tagline">★ {loc_full} 전 지역 30분 내 초고속 방문</div>
                </div>
                <div class="info-grid">
                    <div class="info-row">
                        <div class="info-label">제공 코스</div>
                        <div class="info-content">시그니처 건식 타이, 감성 아로마 릴렉싱, 딥티슈 집중 케어</div>
                    </div>
                    <div class="info-row">
                        <div class="info-label">매장 특징</div>
                        <div class="info-content">전문 자격 테라피스트 구성, 천연 에센셜 오일 사용, 맞춤 컨디셔닝</div>
                    </div>
                </div>
                <a href="tel:0507-1280-3223" class="btn-call">📞 기쁨조 테라피 예약 : 0507-1280-3223</a>
            </div>
        </div>

        <!-- 2번 업체: 한국미인 홈케어 -->
        <div class="vendor-card">
            <div class="vendor-thumb-wrap">
                <img src="/images/vendor2.jpg" alt="{loc_full} {k2} 한국미인 홈케어" class="vendor-img">
                <div class="vendor-tag-float">✨ 야간/새벽 집중 힐링</div>
            </div>
            <div class="vendor-body">
                <div class="vendor-header-flex">
                    <div class="vendor-title-group">
                        <span class="vendor-rank">추천 02</span>
                        <span class="vendor-title">한국미인 홈케어</span>
                    </div>
                    <div class="vendor-tagline">★ {loc_full} 직장인 피로회복 & 림프 순환 케어 전문</div>
                </div>
                <div class="info-grid">
                    <div class="info-row">
                        <div class="info-label">제공 코스</div>
                        <div class="info-content">프리미엄 스웨디시, 림프 드레니쉬, 전신 바디 밸런싱 케어</div>
                    </div>
                    <div class="info-row">
                        <div class="info-label">매장 특징</div>
                        <div class="info-content">24시간 운영, 투명한 정찰제 요금 시스템, 철저한 후불제</div>
                    </div>
                </div>
                <a href="tel:0507-1280-3303" class="btn-call">📞 한국미인 홈케어 예약 : 0507-1280-3303</a>
            </div>
        </div>

        <!-- 3번 업체: 미인클럽 스파 & 테라피 -->
        <div class="vendor-card">
            <div class="vendor-thumb-wrap">
                <img src="/images/vendor3.jpg" alt="{loc_full} {k3} 미인클럽 스파" class="vendor-img">
                <div class="vendor-tag-float">💎 호텔식 VIP 프로그램</div>
            </div>
            <div class="vendor-body">
                <div class="vendor-header-flex">
                    <div class="vendor-title-group">
                        <span class="vendor-rank">추천 03</span>
                        <span class="vendor-title">미인클럽 스파 & 테라피</span>
                    </div>
                    <div class="vendor-tagline">★ 1회용 청결 소독용품 완비 & 감성 힐링</div>
                </div>
                <div class="info-grid">
                    <div class="info-row">
                        <div class="info-label">제공 코스</div>
                        <div class="info-content">타이 + 아로마 스페셜 콤보 코스 (90분/120분)</div>
                    </div>
                    <div class="info-row">
                        <div class="info-label">매장 특징</div>
                        <div class="info-content">위생 소독 관리 철저, 일대일 맞춤 힐링 프로그램 지원</div>
                    </div>
                </div>
                <a href="tel:0507-1280-3193" class="btn-call">📞 미인클럽 테라피 예약 : 0507-1280-3193</a>
            </div>
        </div>

        <!-- 4번 업체: 퀸즈홈테라피 -->
        <div class="vendor-card">
            <div class="vendor-thumb-wrap">
                <img src="/images/vendor4.jpg" alt="{loc_full} {k4} 퀸즈홈테라피" class="vendor-img">
                <div class="vendor-tag-float">🌿 감성 바디 스트레칭</div>
            </div>
            <div class="vendor-body">
                <div class="vendor-header-flex">
                    <div class="vendor-title-group">
                        <span class="vendor-rank">추천 04</span>
                        <span class="vendor-title">퀸즈홈테라피</span>
                    </div>
                    <div class="vendor-tagline">★ {loc_full} 섬세한 압 조절 & 체형 맞춤 솔루션</div>
                </div>
                <div class="info-grid">
                    <div class="info-row">
                        <div class="info-label">제공 코스</div>
                        <div class="info-content">감성 로드 스웨디시, 전신 릴렉싱 스트레칭, 스페셜 풋 케어</div>
                    </div>
                    <div class="info-row">
                        <div class="info-label">매장 특징</div>
                        <div class="info-content">프리미엄 힐링 솔루션 제공, 신속한 1:1 테라피스트 배정</div>
                    </div>
                </div>
                <a href="tel:0507-1280-3334" class="btn-call">📞 퀸즈홈테라피 예약 : 0507-1280-3334</a>
            </div>
        </div>

        <!-- 5번 업체: 한국골든테라피 -->
        <div class="vendor-card">
            <div class="vendor-thumb-wrap">
                <img src="/images/vendor5.jpg" alt="{loc_full} {k1} 한국골든테라피" class="vendor-img">
                <div class="vendor-tag-float">🏷️ 가성비 정찰제 1위</div>
            </div>
            <div class="vendor-body">
                <div class="vendor-header-flex">
                    <div class="vendor-title-group">
                        <span class="vendor-rank">추천 05</span>
                        <span class="vendor-title">한국골든테라피</span>
                    </div>
                    <div class="vendor-tagline">★ {loc_full} 합리적인 정찰제 가격 & 1:1 바디 케어</div>
                </div>
                <div class="info-grid">
                    <div class="info-row">
                        <div class="info-label">제공 코스</div>
                        <div class="info-content">오리지널 정통 타이, 등/어깨 집중 케어, 전신 아로마 힐링</div>
                    </div>
                    <div class="info-row">
                        <div class="info-label">매장 특징</div>
                        <div class="info-content">합리적인 가격 구성, 친절한 바디 케어 상담, 단골 재이용률 상위</div>
                    </div>
                </div>
                <a href="tel:0507-1280-3361" class="btn-call">📞 한국골든테라피 예약 : 0507-1280-3361</a>
            </div>
        </div>

        <!-- 세부 동 바로가기 UI -->
        <div class="section-header">
            <h2>{parent_kr} 세부 동 바로가기</h2>
            <p>원하시는 동네를 선택하시면 상세 안내를 확인하실 수 있습니다.</p>
        </div>
        <div class="gu-grid">
            {sub_links_html}
        </div>

    </div>
    <footer>
        <p>© 테라피365 (Theraphy365). {loc_full} 프리미엄 홈케어 All rights reserved.</p>
    </footer>
</body>
</html>
"""

total_count = 0

# 1. 경기/인천 구 및 세부 동 파일 전체 생성
for folder, (kr_gu_name, dongs) in DETAILED_REGIONS.items():
    os.makedirs(folder, exist_ok=True)
    
    # 세부 동 버튼 링크 HTML 생성
    dong_links_html = "".join([f'<a href="{f}.html" class="gu-item">{name}</a>\n            ' for f, name in dongs])
    
    # 1-1. 구 index.html 생성
    index_file = os.path.join(folder, "index.html")
    canonical_url = f"{BASE_DOMAIN}/{folder}/"
    k_samples = random.sample(THEME_KEYWORDS_20, 4)
    with open(index_file, "w", encoding="utf-8") as f:
        f.write(HTML_TEMPLATE.format(
            base_domain=BASE_DOMAIN,
            canonical_url=canonical_url,
            loc_full=kr_gu_name,
            parent_kr=kr_gu_name,
            sub_links_html=dong_links_html,
            k1=k_samples[0], k2=k_samples[1], k3=k_samples[2], k4=k_samples[3]
        ))
    total_count += 1

    # 1-2. 각 세부 동 html 생성
    for dong_file_key, dong_name in dongs:
        file_path = os.path.join(folder, f"{dong_file_key}.html")
        dong_canonical = f"{BASE_DOMAIN}/{folder}/{dong_file_key}.html"
        k_samples = random.sample(THEME_KEYWORDS_20, 4)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(HTML_TEMPLATE.format(
                base_domain=BASE_DOMAIN,
                canonical_url=dong_canonical,
                loc_full=f"{kr_gu_name} {dong_name}",
                parent_kr=kr_gu_name,
                sub_links_html=dong_links_html,
                k1=k_samples[0], k2=k_samples[1], k3=k_samples[2], k4=k_samples[3]
            ))
        total_count += 1

# 2. 수원/성남/고양/용인/안양/안산 등 시 단위 대표 index.html 생성
for city_folder, (city_kr, gus) in CITY_MAP.items():
    os.makedirs(city_folder, exist_ok=True)
    gu_links_html = "".join([f'<a href="{link}" class="gu-item">{name}</a>\n            ' for link, name in gus])
    
    file_path = os.path.join(city_folder, "index.html")
    city_canonical = f"{BASE_DOMAIN}/{city_folder}/"
    k_samples = random.sample(THEME_KEYWORDS_20, 4)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(HTML_TEMPLATE.format(
            base_domain=BASE_DOMAIN,
            canonical_url=city_canonical,
            loc_full=city_kr,
            parent_kr=city_kr,
            sub_links_html=gu_links_html,
            k1=k_samples[0], k2=k_samples[1], k3=k_samples[2], k4=k_samples[3]
        ))
    total_count += 1

print(f"🎉 총 {total_count}개 경기/인천 전체 서브페이지(20종 스팸 회피 키워드 패턴 + 5개 업체 + 테라피365 브랜드) 빌드 완료!")