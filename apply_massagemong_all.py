# -*- coding: utf-8 -*-
import os
import re
import random

# ==============================================================================
# 1. 영문 폴더/파일명 -> 한글 지역명 매핑
# ==============================================================================
NAME_MAP = {
    "seoul": "서울", "gangnam": "강남구", "seocho": "서초구", "songpa": "송파구", "gangdong": "강동구",
    "mapo": "마포구", "yongsan": "용산구", "seodaemun": "서대문구", "eunpyeong": "은평구",
    "jongno": "종로구", "junggu": "중구", "jungnang": "중랑구", "seongbuk": "성북구",
    "gangbuk": "강북구", "dobong": "도봉구", "nowon": "노원구", "seongdong": "성동구",
    "gwangjin": "광진구", "dongdaemun": "동대문구", "yeongdeungpo": "영등포구",
    "guro": "구로구", "geumcheon": "금천구", "yangcheon": "양천구", "gangse": "강서구",
    "gangseo": "강서구", "dongjak": "동작구", "gwanak": "관악구",
    "incheon_bupyeong": "인천 부평구", "incheon_namdong": "인천 남동구", "incheon_yeonsu": "인천 연수구",
    "incheon_michuhol": "인천 미추홀구", "incheon_seogu": "인천 서구", "incheon_gyeyang": "인천 계양구",
    "incheon_junggu": "인천 중구", "incheon_donggu": "인천 동구",
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
    "uiwang": "의왕시", "anseong": "안성시"
}

def get_loc_name(rel_path):
    parts = rel_path.replace("\\", "/").split("/")
    if len(parts) == 2 and parts[1] == "index.html":
        folder = parts[0]
        return NAME_MAP.get(folder, folder.capitalize())
    else:
        folder = parts[0]
        file_name = parts[-1].replace(".html", "")
        folder_kr = NAME_MAP.get(folder, folder.capitalize())
        file_kr = NAME_MAP.get(file_name, file_name.capitalize())
        return f"{folder_kr} {file_kr}" if folder_kr != file_kr else folder_kr

# ==============================================================================
# 2. 서브페이지 전용 5대 제휴 업체 템플릿 (출장마사지 & 홈타이 키워드 최적화)
# ==============================================================================
VENDOR_TEMPLATES = [
    # 기쁨조 테라피
    """
        <div class="vendor-card">
            <div class="vendor-thumb-wrap">
                <img src="/images/vendor1.jpg" alt="{loc} 출장마사지 기쁨조 테라피" class="vendor-img">
                <div class="vendor-tag-float">👑 최우수 만족도 매장</div>
            </div>
            <div class="vendor-body">
                <div class="vendor-header-flex">
                    <div class="vendor-title-group">
                        <span class="vendor-rank">{rank}</span>
                        <span class="vendor-title">기쁨조 테라피</span>
                    </div>
                    <div class="vendor-tagline">★ {loc} 전 지역 30분 내 신속 방문 출장마사지</div>
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
                <div class="vendor-btn-wrap">
                    <a href="tel:0507-1280-3223" class="btn-call">📞 기쁨조 테라피 예약 : 0507-1280-3223</a>
                </div>
            </div>
        </div>
    """,
    # 한국미인 홈케어
    """
        <div class="vendor-card">
            <div class="vendor-thumb-wrap">
                <img src="/images/vendor2.jpg" alt="{loc} 출장마사지 한국미인 홈케어" class="vendor-img">
                <div class="vendor-tag-float">✨ 야간/새벽 집중 힐링</div>
            </div>
            <div class="vendor-body">
                <div class="vendor-header-flex">
                    <div class="vendor-title-group">
                        <span class="vendor-rank">{rank}</span>
                        <span class="vendor-title">한국미인 홈케어</span>
                    </div>
                    <div class="vendor-tagline">★ {loc} 홈타이 & 직장인 피로회복 전문 출장케어</div>
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
                <div class="vendor-btn-wrap">
                    <a href="tel:0507-1280-3303" class="btn-call">📞 한국미인 홈케어 예약 : 0507-1280-3303</a>
                </div>
            </div>
        </div>
    """,
    # 미인클럽 스파 & 테라피
    """
        <div class="vendor-card">
            <div class="vendor-thumb-wrap">
                <img src="/images/vendor3.jpg" alt="{loc} 출장마사지 미인클럽 스파" class="vendor-img">
                <div class="vendor-tag-float">💎 호텔식 VIP 프로그램</div>
            </div>
            <div class="vendor-body">
                <div class="vendor-header-flex">
                    <div class="vendor-title-group">
                        <span class="vendor-rank">{rank}</span>
                        <span class="vendor-title">미인클럽 스파 & 테라피</span>
                    </div>
                    <div class="vendor-tagline">★ 1회용 청결 소독용품 완비 & {loc} 감성 힐링 스파</div>
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
                <div class="vendor-btn-wrap">
                    <a href="tel:0507-1280-3193" class="btn-call">📞 미인클럽 테라피 예약 : 0507-1280-3193</a>
                </div>
            </div>
        </div>
    """,
    # 퀸즈홈테라피
    """
        <div class="vendor-card">
            <div class="vendor-thumb-wrap">
                <img src="/images/vendor4.jpg" alt="{loc} 출장마사지 퀸즈홈테라피" class="vendor-img">
                <div class="vendor-tag-float">🌿 감성 바디 스트레칭</div>
            </div>
            <div class="vendor-body">
                <div class="vendor-header-flex">
                    <div class="vendor-title-group">
                        <span class="vendor-rank">{rank}</span>
                        <span class="vendor-title">퀸즈홈테라피</span>
                    </div>
                    <div class="vendor-tagline">★ {loc} 전지역 1:1 방문 홈타이 & 섬세한 압 조절</div>
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
                <div class="vendor-btn-wrap">
                    <a href="tel:0507-1280-3334" class="btn-call">📞 퀸즈홈테라피 예약 : 0507-1280-3334</a>
                </div>
            </div>
        </div>
    """,
    # 한국골든테라피
    """
        <div class="vendor-card">
            <div class="vendor-thumb-wrap">
                <img src="/images/vendor5.jpg" alt="{loc} 출장마사지 한국골든테라피" class="vendor-img">
                <div class="vendor-tag-float">🏷️ 가성비 정찰제 1위</div>
            </div>
            <div class="vendor-body">
                <div class="vendor-header-flex">
                    <div class="vendor-title-group">
                        <span class="vendor-rank">{rank}</span>
                        <span class="vendor-title">한국골든테라피</span>
                    </div>
                    <div class="vendor-tagline">★ {loc} 정찰제 출장안마 & 친절한 1:1 바디 케어</div>
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
                <div class="vendor-btn-wrap">
                    <a href="tel:0507-1280-3361" class="btn-call">📞 한국골든테라피 예약 : 0507-1280-3361</a>
                </div>
            </div>
        </div>
    """
]

def build_random_vendors_html(loc_name):
    shuffled_templates = VENDOR_TEMPLATES.copy()
    random.shuffle(shuffled_templates)
    
    html_pieces = []
    for idx, tmpl in enumerate(shuffled_templates, start=1):
        rank_label = f"추천 {idx:02d}"
        html_pieces.append(tmpl.format(loc=loc_name, rank=rank_label))
        
    return "\n".join(html_pieces)

# ==============================================================================
# 3. 서브페이지 일괄 처리 실행
# ==============================================================================
updated_files = 0

for root, dirs, files in os.walk("."):
    if any(part.startswith(".") for part in root.split(os.sep)):
        continue

    for file in files:
        if not file.endswith(".html"):
            continue
        
        file_path = os.path.join(root, file)
        rel_path = os.path.relpath(file_path, ".").replace("\\", "/")
        
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # 브랜드명 통일 (스파루나/마사지몽 잔재 제거 -> 테라피365)
        content = content.replace("스파루나", "테라피365").replace("마사지몽", "테라피365")
        content = content.replace("SpaLuna", "Theraphy365").replace("MassageMong", "Theraphy365")
        content = content.replace("spaluna", "theraphy365").replace("massagemong", "theraphy365")

        # 서브페이지인 경우: 업체 카드 교체 및 지역 출장마사지 키워드 적용
        if rel_path != "index.html" and '<div class="vendor-card"' in content or '<div class="vendor-card">' in content:
            loc_name = get_loc_name(rel_path)
            
            # 섹션 타이틀 변경
            content = re.sub(
                r'<h2[^>]*>.*?TOP 5.*?</h2>', 
                f'<h2>{loc_name} 출장마사지 & 홈타이 추천 제휴처 TOP 5</h2>', 
                content, count=1, flags=re.IGNORECASE
            )
            
            # 모든 기존 vendor-card 추출 후 새 셔플 카드로 교체
            vendors_replacement = build_random_vendors_html(loc_name)
            content = re.sub(
                r'(<div class="vendor-card">[\s\S]*?</div>\s*</div>)(?=\s*<!--|\s*<div class="section-header"|\s*<div class="map-section-card")', 
                vendors_replacement.strip(), 
                content, count=1
            )
            
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            updated_files += 1
            print(f"✔ [{rel_path}] {loc_name} 출장마사지 키워드 및 제휴처 셔플 완료")

print(f"\n🎉 총 {updated_files}개 서브페이지에 '지역명+출장마사지' 키워드와 5개 업체가 완벽히 적용되었습니다!")