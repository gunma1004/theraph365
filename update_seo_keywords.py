@'
# -*- coding: utf-8 -*-
import os
import re
import random

# ==============================================================================
# 1. 서울 / 경기 / 인천 전체 한글 매핑 딕셔너리
# ==============================================================================
NAME_MAP = {
    # [서울 25개 구]
    "gangnam": "강남구", "seocho": "서초구", "songpa": "송파구", "gangdong": "강동구",
    "mapo": "마포구", "yongsan": "용산구", "seodaemun": "서대문구", "eunpyeong": "은평구",
    "jongno": "종로구", "junggu": "중구", "jungnang": "중랑구", "seongbuk": "성북구",
    "gangbuk": "강북구", "dobong": "도봉구", "nowon": "노원구", "seongdong": "성동구",
    "gwangjin": "광진구", "dongdaemun": "동대문구", "yeongdeungpo": "영등포구",
    "guro": "구로구", "geumcheon": "금천구", "yangcheon": "양천구", "gangse": "강서구",
    "gangseo": "강서구", "dongjak": "동작구", "gwanak": "관악구", "seoul": "서울 전지역",

    # [인천 8개 구]
    "incheon_bupyeong": "인천 부평구", "incheon_namdong": "인천 남동구", "incheon_yeonsu": "인천 연수구",
    "incheon_michuhol": "인천 미추홀구", "incheon_seogu": "인천 서구", "incheon_gyeyang": "인천 계양구",
    "incheon_junggu": "인천 중구", "incheon_donggu": "인천 동구",

    # [경기 주요 시/구]
    "suwon": "수원시", "suwon_paldal": "수원 팔달구", "suwon_yeongtong": "수원 영통구", "suwon_jangan": "수원 장안구", "suwon_gwonseon": "수원 권선구",
    "seongnam": "성남시", "seongnam_bundang": "성남 분당구", "seongnam_sujeong": "성남 수정구", "seongnam_jungwon": "성남 중원구",
    "goyang": "고양시", "goyang_ilsandong": "고양 일산동구", "goyang_ilsanseo": "고양 일산서구", "goyang_deogyang": "고양 덕양구",
    "yongin": "용인시", "yongin_suji": "용인 수지구", "yongin_giheung": "용인 기흥구", "yongin_cheoin": "용인 처인구",
    "anyang": "안양시", "anyang_dongan": "안양 동안구", "anyang_manan": "안양 만안구",
    "ansan": "안산시", "ansan_danwon": "안산 단원구", "ansan_sangnok": "안산 상록구",
    "bucheon": "부천시", "hwaseong": "화성시", "pyeongtaek": "평택시", "siheung": "시흥시",
    "gimpo": "김포시", "paju": "파주시", "namyangju": "남양주시", "uijeongbu": "의정부시",
    "hanam": "하남시", "gwangmyeong": "광명시", "gunpo": "군포시", "guri": "구리시",
    "osan": "오산시", "gwangju_gyeonggi": "경기 광주시", "icheon": "이천시", "yangju": "양주시",
    "uiwang": "의왕시", "anseong": "안성시",

    # [서울 세부 동]
    "yeoksam": "역삼동", "nonhyeon": "논현동", "apgujeong": "압구정동", "cheongdam": "청담동", "samseong": "삼성동",
    "seocho_dong": "서초동", "banpo": "반포동", "bangbae": "방배동", "yangjae": "양재동", "jamwon": "잠원동",
    "jamsil": "잠실동", "garak": "가락동", "munjeong": "문정동", "bangi": "방이동", "ogeum": "오금동",
    "gongneung": "공릉동", "sanggye": "상계동", "junggye": "중계동", "hagye": "하계동", "wolgye": "월계동",
    "hongdae": "홍대", "hapjeong": "합정동", "sinchon": "신촌", "yeonnam": "연남동", "mangwon": "망원동",
    "yeouido": "여의도", "dangsan": "당산동", "mullae": "문래동", "sillim": "신림동", "bongcheon": "봉천동",
    "noryangjin": "노량진", "sangdo": "상도동", "sadang": "사당동", "heukseok": "흑석동", "sindaebang": "신대방동",
    "cheonho": "천호동", "gil": "길동", "amsa": "암사동", "myeongil": "명일동", "seongnae": "성내동",
    "mokdong": "목동", "sinjeong": "신정동", "hwagok": "화곡동", "magok": "마곡동", "guro_dong": "구로동",
    "sindorim": "신도림", "gasan": "가산동", "doksan": "독산동", "itaewon": "이태원", "hannam": "한남동",
    "hyehwa": "혜화동", "myeongdong": "명동", "hoehyeon": "회현동", "sindang": "신당동",

    # [인천/경기 세부 동]
    "bupyeong": "부평동", "sanggok": "산곡동", "cheongcheon": "청천동", "galsan": "갈산동", "sipjeong": "십정동", "bugae": "부개동", "samsan": "삼산동",
    "guwol": "구월동", "ganseok": "간석동", "mansu": "만수동", "nonhyeon_incheon": "논현동", "seochang": "서창동", "dorim": "도림동",
    "songdo": "송도동", "yeonsu": "연수동", "dongchun": "동춘동", "cheonghak": "청학동", "okryeon": "옥련동", "seonhak": "선학동",
    "juan": "주안동", "yonghyeon": "용현동", "hakik": "학익동", "dohwa": "도화동", "sungui": "숭의동", "gwangyo": "관교동",
    "cheongna": "청라동", "geomdan": "검단", "luwon": "루원시티", "gajeong": "가정동", "seoknam": "석남동", "yeonhui": "연희동", "dangha": "당하동", "majeon": "마전동",
    "gyeyang": "계양", "jakjeon": "작전동", "hyoseong": "효성동", "gyesan": "계산동", "seoun": "서운동",
    "yeongjong": "영종도", "unseo": "운서동", "jungsan": "중산동", "sinpo": "신포동", "dongincheon": "동인천",
    "songhyeon": "송현동", "songrim": "송림동", "manseok": "만석동", "hwasu": "화수동",
    "ingye": "인계동", "haenggung": "행궁동", "hwaseo": "화서동", "ji-dong": "지동", "maesan": "매산동",
    "gwanggyo": "광교", "yeongtong": "영통동", "mangpo": "망포동", "maetan": "매탄동", "woncheon": "원천동",
    "jeongja": "정자동", "jo-won": "조원동", "yuljeon": "율전동", "cheoncheon": "천천동", "yeonmu": "연무동",
    "gwonseon": "권선동", "gosaek": "고색동", "homaesil": "호매실동", "seriu": "세류동", "geumgok": "금곡동",
    "seohyeon": "서현동", "yatap": "야탑동", "pangyo": "판교", "baekhyeon": "백현동", "sunae": "수내동", "ime": "이매동", "gumi": "구미동", "unjoong": "운중동",
    "wirye": "위례", "sinheung": "신흥동", "taepyeong": "태평동", "sanseong": "산성동", "bokjeong": "복정동", "sujin": "수진동",
    "moran": "모란", "seongnam_dong": "성남동", "sangdaewon": "상대원동", "hagdaewon": "하대원동", "geumgwang": "금광동", "bank": "은행동",
    "baekseok": "백석동", "madu": "마두동", "janghang": "장항동", "jeongbalsan": "정발산동", "siksa": "식사동", "pungsan": "풍산동",
    "juyeop": "주엽동", "daehwa": "대화동", "tanhyun": "탄현동", "ilsan": "일산동", "songsan": "송산동", "deogi": "덕이동",
    "hwajeong": "화정동", "haengsin": "행신동", "samsong": "삼송", "wonheung": "원흥", "hyangdong": "향동", "deogeun": "덕은", "wondang": "원당",
    "pungdeokcheon": "풍덕천동", "jookjeon": "죽전동", "dongcheon": "동천동", "sanghyeon": "상현동", "shinbong": "신봉동", "sungbok": "성복동",
    "dongbaek": "동백동", "singal": "신갈동", "gugal": "구갈동", "bora": "보라동", "seonong": "서농동", "guseong": "구성", "mabuk": "마북동",
    "kimryangjang": "김량장동", "yeokbuk": "역북동", "samga": "삼가동", "pogok": "포곡", "mohan": "모현", "yangji": "양지",
    "pyeongchon": "평촌동", "beomgye": "범계", "indeogwon": "인덕원", "gwanyang": "관양동", "hogye": "호계동", "bisan": "비산동",
    "anyang_dong": "안양동", "seoksu": "석수동", "bakdal": "박달동",
    "gojan": "고잔동", "jungang": "중앙동", "chogi": "초지동", "wongok": "원곡동", "seonbu": "선부동", "daebu": "대부도",
    "bono": "본오동", "sadong": "사동", "wolpi": "월피동", "seongpo": "성포동", "il-dong": "일동", "i-dong": "이동",
    "jungdong": "중동", "sangdong": "상동", "sinjungdong": "신중동", "sosa": "소사동", "wonmi": "원미동", "ojeong": "오정동", "yeokgok": "역곡동", "gogang": "고강동",
    "dongtan": "동탄1", "dongtan2": "동탄2", "byeongjeom": "병점", "hyangnam": "향남", "bongdam": "봉담", "namyang": "남양", "saesol": "새솔동", "jinjoo": "진안동",
    "godeok": "고덕", "bijeon": "비전동", "songtan": "송탄", "anjeong": "안정리", "anseok": "안중", "poseung": "포승", "cheongbuk": "청북", "sejeong": "세교동",
    "baegot": "배곧동", "jeongwang": "정왕동", "eunhaeng": "은행동", "mokgam": "목감동", "daeya": "대야동", "sinhyeon": "신현동", "neunggok": "능곡동", "janghyeon": "장현동",
    "gurae": "구래동", "unyang": "운양동", "janggi": "장기동", "pungmu": "풍무동", "sau": "사우동", "masan": "마산동", "gochon": "고촌", "tongjin": "통진",
    "unjeong": "운정", "geumchon": "금촌동", "munsan": "문산", "gyoha": "교하", "yadang": "야당동", "dongpae": "동패동",
    "dasang": "다산동", "byeolnae": "별내동", "pyeongnae": "평내동", "hopyeong": "호평동", "jinjeop": "진접", "wabu": "와부", "onam": "오남", "hwado": "화도",
    "uijeongbu_dong": "의정부동", "howon": "호원동", "singok": "신곡동", "minrak": "민락동", "gosan": "고산동", "ganeung": "가능동", "geumo": "금오동",
    "misa": "미사", "wirye_hanam": "위례", "gamil": "감일", "deokpung": "덕풍동", "sinjang": "신장동", "pungcheon": "풍산동",
    "cheolsan": "철산동", "gwangmyeong_dong": "광명동", "soha": "소하동", "iljik": "일직동", "haan": "하안동",
    "sanbon": "산본동", "geumjeong": "금정동", "dang-dong": "당동", "daeyami": "대야미", "bugok": "부곡동",
    "sutaek": "수택동", "inmae": "인창동", "galmae": "갈매동", "gyomun": "교문동", "achasan": "아천동",
    "won-dong": "원동", "seggyo": "세교", "gweol": "궐동", "osandong": "오산동", "eunjeong": "은계동",
    "gyeongan": "경안동", "taejeon": "태전동", "opocheup": "오포", "sinhyun": "신현동", "neungpyeong": "능평동", "tanbeol": "탄벌동",
    "changjeon": "창전동", "jeungpo": "증포동", "bubal": "부발", "majung": "마장", "anheung": "안흥동",
    "okjeong": "옥정동", "goeup": "고읍동", "deokgye": "덕계동", "baekseok_yangju": "백석",
    "poil": "포일동", "naeson": "내손동", "gojeon": "고천동", "sam-dong": "삼동",
    "gongdo": "공도", "daedeok": "대덕", "anseong_dong": "안성동", "boggae": "보개"
}

def get_loc_name(rel_path):
    parts = rel_path.replace("\\", "/").split("/")
    if len(parts) == 2 and parts[1] == "index.html":
        folder = parts[0]
        return NAME_MAP.get(folder, folder)
    else:
        folder = parts[0]
        file_name = parts[-1].replace(".html", "")
        folder_kr = NAME_MAP.get(folder, folder)
        file_kr = NAME_MAP.get(file_name, file_name)
        return f"{folder_kr} {file_kr}" if folder_kr != file_kr else folder_kr

# ==============================================================================
# 2. '출장 마사지' 필수 포함 30종 차별화 타이틀
# ==============================================================================
TITLE_TEMPLATES = [
    "{loc} 출장 마사지 24시 VIP 홈케어 & 프리미엄 스파 - 테라피365",
    "프라이빗 1:1 {loc} 출장 마사지 신속 방문 케어 :: 테라피365",
    "{loc} 출장 마사지 추천 · 뭉친 근육을 푸는 호텔식 홈타이 (테라피365)",
    "지친 하루를 위한 {loc} 출장 마사지 30분 도착 보장 | 테라피365",
    "{loc} 출장 마사지 24시간 안심 후불제 프라이빗 솔루션 | 테라피365",
    "스트레스 완화 & 림프 순환 전문 {loc} 출장 마사지 [테라피365]",
    "{loc} 출장 마사지 직장인 야근 피로 녹이는 감성 스웨디시 - 테라피365",
    "내 집에서 즐기는 {loc} 출장 마사지 VIP 바디 테라피 (테라피365)",
    "{loc} 출장 마사지 전문 테라피스트 1:1 방문 코스 비교 | 테라피365",
    "품격 있는 휴식의 기준, {loc} 출장 마사지 & 24시 홈스파 (테라피365)",
    "{loc} 출장 마사지 믿을 수 있는 정찰제 아로마 힐링 케어 | 테라피365",
    "선입금 없는 100% 현장 결제 {loc} 출장 마사지 신속 배차 - 테라피365",
    "{loc} 출장 마사지 타이 & 스웨디시 스페셜 콤보 코스 | 테라피365",
    "도심 속 완벽한 쉼표 {loc} 출장 마사지 24시간 방문 테라피 :: 테라피365",
    "{loc} 출장 마사지 숙련된 베테랑 관리사의 섬세한 케어 [테라피365]",
    "{loc} 출장 마사지 새벽·야간 언제든 예약 가능한 홈케어 (테라피365)",
    "지친 일상에 활력을 채우는 {loc} 출장 마사지 딥티슈 힐링 | 테라피365",
    "{loc} 출장 마사지 호텔급 최고급 에센셜 오일 테라피 - 테라피365",
    "어디서나 30분 내 도착 {loc} 출장 마사지 & 프리미엄 홈타이 | 테라피365",
    "{loc} 출장 마사지 고객 만족도 1위 검증 제휴 매장 TOP 5 :: 테라피365",
    "{loc} 출장 마사지 프라이빗 룸케어 실시간 안심 예약 (테라피365)",
    "부드러운 손길의 감성 릴렉싱 {loc} 출장 마사지 24시 | 테라피365",
    "{loc} 출장 마사지 전신 밸런싱 & 피로회복 집중 솔루션 - 테라피365",
    "깨끗한 1회용 위생용품 완비 {loc} 출장 마사지 안심 방문 [테라피365]",
    "{loc} 출장 마사지 24시간 언제나 열려있는 힐링 플랫폼 (테라피365)",
    "하루의 피로를 상쾌하게 비우는 {loc} 출장 마사지 1:1 케어 | 테라피365",
    "{loc} 출장 마사지 합리적인 가격의 고품격 아로마 타이 코스 - 테라피365",
    "남녀노소 누구나 편안한 {loc} 출장 마사지 24시 맞춤 홈케어 (테라피365)",
    "{loc} 출장 마사지 실시간 빠른 배정 & VIP 바디 힐링 안내 :: 테라피365",
    "365일 지친 당신을 위한 {loc} 출장 마사지 전문 플랫폼 | 테라피365"
]

# ==============================================================================
# 3. '출장 마사지' 필수 포함 30종 설명(Description)
# ==============================================================================
DESC_TEMPLATES = [
    "{loc} 출장 마사지 24시간 안심 후불제 테라피365! 아로마, 건식 타이, 스웨디시 1:1 맞춤 힐링.",
    "지친 하루를 채우는 {loc} 출장 마사지. 숙련된 전문 테라피스트가 30분 내 계신 곳으로 찾아갑니다.",
    "{loc} 출장 마사지 전지역 24시 신속 방문 케어. 천연 오일 스웨디시와 림프 순환 케어를 만나보세요.",
    "선입금 없는 100% 현장 결제 {loc} 출장 마사지 테라피365! 뭉친 근육을 시원하게 풀어드립니다.",
    "{loc} 출장 마사지 직장인 야근 피로회복 24시간 방문 테라피. 철저한 위생 관리와 정찰제 운영.",
    "호텔식 프리미엄 바디 테라피를 집에서! {loc} 출장 마사지 전문 플랫폼 테라피365입니다.",
    "{loc} 출장 마사지 1:1 맞춤형 딥티슈 & 림프 힐링 솔루션. 전화 한 통으로 신속하게 배차됩니다.",
    "피로에 지친 당신을 위한 {loc} 출장 마사지 24시 홈케어. 타이, 아로마 스페셜 코스를 경험해보세요.",
    "{loc} 출장 마사지 전 구역 30분 내 빠른 도착 보장! 전문 자격 관리사의 품격 있는 힐링 안내.",
    "청결한 1회용 비품 완비 {loc} 출장 마사지 안심 방문. 내 공간에서 누리는 가장 안락한 스파 타임.",
    "{loc} 출장 마사지 24시간 실시간 예약 테라피365. 감성 로드 스웨디시부터 전신 스트레칭까지 완벽 케어.",
    "야간·새벽 언제든 이용 가능한 {loc} 출장 마사지 24시. 검증된 TOP 5 제휴 매장의 정직한 힐링 안내.",
    "{loc} 출장 마사지 인근 20~30분 신속 방문! 부드러운 아로마 릴렉싱 케어로 스트레스를 날려보세요.",
    "믿고 찾는 {loc} 출장 마사지 1위 테라피365. 섬세한 압 조절과 맞춤 컨디셔닝으로 고객 만족 보장.",
    "{loc} 출장 마사지 전지역 당일 신속 배차! 시그니처 건식 타이와 VIP 림프 케어로 몸을 리프레시하세요.",
    "내 집에서 즐기는 극상의 힐링 {loc} 출장 마사지. 합리적인 정찰제 요금으로 안심하고 예약하세요.",
    "{loc} 출장 마사지 1:1 맞춤형 바디 테라피. 전문 관리사의 세심한 손길로 뭉친 어깨를 풀어드립니다.",
    "365일 쉬지 않는 {loc} 출장 마사지 24시간 프리미엄 동반자 테라피365! 프라이빗 방문 케어 안내.",
    "{loc} 출장 마사지 최고급 천연 에센셜 오일 사용! 피부 보습과 근육 이완을 선사하는 프리미엄 스파.",
    "선입금 사기 걱정 없는 100% 후불 결제 {loc} 출장 마사지. 언제 어디서나 안심하고 이용하세요.",
    "{loc} 출장 마사지 직장인 단골 재이용률 상위 매장 안내. 친절한 1:1 상담과 빠른 배정을 지원합니다.",
    "프라이빗한 나만의 공간에서 즐기는 {loc} 출장 마사지 24시. 최상의 힐링 코스를 제안합니다.",
    "{loc} 출장 마사지 타이 + 아로마 콤보 스페셜 프로그램. 숙련된 테라피스트의 손길을 느껴보세요.",
    "번거로운 이동 없이 자택에서 만나는 {loc} 출장 마사지. 지친 일상에 활력을 불어넣어 드립니다.",
    "{loc} 출장 마사지 전 구역 신속 배차 네트워크 테라피365! 정직한 가격과 친절한 서비스로 모십니다.",
    "체형과 컨디션에 맞춘 {loc} 출장 마사지 1:1 솔루션. 전문 테라피스트가 직접 방문하여 케어합니다.",
    "{loc} 출장 마사지 24시간 운영 방문 테라피. 스트레스 해소와 숙면을 돕는 감성 릴렉싱 코스 완비.",
    "깨끗하고 안전한 {loc} 출장 마사지 예약 플랫폼. 테라피365에서 검증된 제휴처를 확인하세요.",
    "{loc} 출장 마사지 맞춤형 전신 바디 밸런싱. 부드러운 스웨디시 오일 케어로 긴장을 풀어드립니다.",
    "도심 속 최고의 휴식처 {loc} 출장 마사지 24시 테라피365! 지금 바로 실시간 예약을 문의하세요."
]

# ==============================================================================
# 4. '출장 마사지' 필수 포함 30종 키워드(Keywords)
# ==============================================================================
KEYWORD_TEMPLATES = [
    "{loc} 출장 마사지, 테라피365, {loc} 홈케어, {loc} 아로마 테라피, 24시 방문 스파",
    "{loc} 출장 마사지, {loc} 바디 테라피, {loc} 24시 홈타이, 프라이빗 1인 케어",
    "{loc} 출장 마사지, {loc} 힐링 테라피, 림프 순환 케어, 24시간 방문 홈케어",
    "{loc} 출장 마사지, {loc} 호텔식 스웨디시, {loc} 24시 테라피, 직장인 피로회복",
    "{loc} 출장 마사지, {loc} 방문 테라피, {loc} 건식 타이, 후불제 안심 케어",
    "{loc} 출장 마사지, 테라피365 {loc}, {loc} 아로마 오일 케어, 24시간 출장 스파",
    "{loc} 출장 마사지, {loc} 1:1 맞춤 테라피, {loc} 출장 마사지 추천, 30분 도착",
    "{loc} 출장 마사지, {loc} 24시 홈타이 예약, {loc} 감성 스웨디시, 바디 밸런싱",
    "{loc} 출장 마사지, {loc} 전문 테라피스트, {loc} 24시간 방문 케어, 정찰제 테라피",
    "{loc} 출장 마사지, {loc} 출장 홈스파, {loc} 아로마 릴렉싱, 1회용 위생 비품",
    "{loc} 출장 마사지, {loc} 24시 출장 마사지, {loc} 홈케어 플랫폼, 야간 새벽 테라피",
    "{loc} 출장 마사지, 테라피365, {loc} 타이 마사지, {loc} 스웨디시 전문점",
    "{loc} 출장 마사지, {loc} VIP 룸케어, {loc} 방문 바디 테라피, 24시 홈타이",
    "{loc} 출장 마사지, {loc} 출장 마사지 후기, {loc} 24시 아로마 테라피, 신속 배차",
    "{loc} 출장 마사지, {loc} 감성 힐링 케어, {loc} 24시간 홈타이, 1:1 테라피스트",
    "{loc} 출장 마사지, {loc} 바디 릴렉싱, {loc} 출장 마사지 가격, 선입금 없는 후불제",
    "{loc} 출장 마사지, {loc} 24시 방문 테라피, {loc} 스웨디시 오일, 전신 힐링 코스",
    "{loc} 출장 마사지, 테라피365 {loc}, {loc} 24시간 출장 홈타이, 호텔식 1인 테라피",
    "{loc} 출장 마사지, {loc} 림프 드레니쉬, {loc} 출장 마사지 빠른곳, 24시 직장인 케어",
    "{loc} 출장 마사지, {loc} 건식 타이 케어, {loc} 아로마 힐링 스파, 24시간 방문 예약",
    "{loc} 출장 마사지, {loc} 24시 출장 마사지 가이드, {loc} 홈케어 전문, 맞춤 압 조절",
    "{loc} 출장 마사지, {loc} 감성 로드 스웨디시, {loc} 24시간 힐링 테라피, 신속 방문",
    "{loc} 출장 마사지, 테라피365, {loc} 출장 마사지 TOP 5, {loc} 24시 홈타이 추천",
    "{loc} 출장 마사지, {loc} 프라이빗 홈스파, {loc} 24시간 방문 테라피, 최고급 오일",
    "{loc} 출장 마사지, {loc} 전신 컨디셔닝, {loc} 출장 마사지 안심 예약, 100% 후불",
    "{loc} 출장 마사지, {loc} 24시 힐링 아로마, {loc} 홈케어 테라피스트, 당일 빠른 도착",
    "{loc} 출장 마사지, {loc} 스웨디시 마사지, {loc} 24시간 출장 홈타이, 스트레스 해소",
    "{loc} 출장 마사지, {loc} 1:1 방문 스파, {loc} 출장 마사지 코스 안내, 피로회복",
    "{loc} 출장 마사지, 테라피365 {loc}, {loc} 24시 바디 힐링, 건식 습식 콤보",
    "{loc} 출장 마사지, {loc} 프리미엄 방문 테라피, {loc} 출장 마사지 24시, VIP 맞춤 케어"
]

# ==============================================================================
# 5. 전 파일 순회 및 개별 무작위 메타태그 적용
# ==============================================================================
count = 0

for root, dirs, files in os.walk("."):
    for file in files:
        if not file.endswith(".html"):
            continue
        
        file_path = os.path.join(root, file)
        rel_path = os.path.relpath(file_path, ".").replace("\\", "/")
        
        if rel_path == "index.html":
            continue
        
        loc_name = get_loc_name(rel_path)
        
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        new_title = random.choice(TITLE_TEMPLATES).format(loc=loc_name)
        new_desc = random.choice(DESC_TEMPLATES).format(loc=loc_name)
        new_keywords = random.choice(KEYWORD_TEMPLATES).format(loc=loc_name)
        new_og_title = f"{loc_name} 출장 마사지 & 24시 프리미엄 힐링 테라피 | 테라피365"
        
        # 1. <title> 치환
        content = re.sub(r'<title>.*?</title>', f'<title>{new_title}</title>', content, flags=re.DOTALL)
        
        # 2. <meta name="description"> 치환
        content = re.sub(r'<meta\s+name=["\']description["\']\s+content=["\'].*?["\']\s*/?>', 
                         f'<meta name="description" content="{new_desc}">', content, flags=re.DOTALL)
        
        # 3. <meta name="keywords"> 치환 또는 추가
        if '<meta name="keywords"' in content or "<meta name='keywords'" in content:
            content = re.sub(r'<meta\s+name=["\']keywords["\']\s+content=["\'].*?["\']\s*/?>', 
                             f'<meta name="keywords" content="{new_keywords}">', content, flags=re.DOTALL)
        else:
            content = re.sub(r'(<meta\s+name=["\']description["\'].*?>)', 
                             rf'\1\n    <meta name="keywords" content="{new_keywords}">', content, flags=re.DOTALL)
        
        # 4. <meta property="og:title"> 치환
        if 'property="og:title"' in content:
            content = re.sub(r'<meta\s+property=["\']og:title["\']\s+content=["\'].*?["\']\s*/?>', 
                             f'<meta property="og:title" content="{new_og_title}">', content, flags=re.DOTALL)
            
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
            
        count += 1

print(f"🎉 총 {count}개 페이지에 '출장 마사지' 핵심 키워드가 포함된 차별화 30종 패턴이 완벽하게 적용되었습니다.")
'@ | Out-File -FilePath "update_seo_keywords_theraphy365.py" -Encoding utf8

# 실행 및 깃허브 배포
python update_seo_keywords_theraphy365.py
python generate_seo.py
git add .
git commit -m "테라피365 전 구/동 페이지 '출장 마사지' 핵심 키워드 최우선 배치 및 배포"
git push