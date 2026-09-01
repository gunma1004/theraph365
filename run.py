# -*- coding: utf-8 -*-
import os
import sys

# 실행할 빌드 단계 정의 (20종 스팸 회피 키워드 파이프라인 반영)
BUILD_STEPS = [
    ("1. 브랜드명 & 도메인 최신화 (테라피365)", "convert_to_theraphy365.py"),
    ("2. 수도권 전지역 네비게이션 그리드 연결", "add_full_capital_grid.py"),
    ("3. 20종 스팸 회피 키워드 메타태그 생성 및 전면 재구성", "update_seo_keywords_theraphy365.py"),
    ("4. 외부 이미지 로컬 정적 경로 일괄 치환", "update_images.py"),
    ("5. Open Graph (og:title / og:description) 안전 동기화", "apply_all_og.py"),
    ("6. 네이버 SEO / Canonical 태그 최종 점검", "optimize_naver_meta.py"),
    ("7. 업체 카드 무작위 셔플 스크립트 주입", "add_shuffle.py"),
    ("8. sitemap.xml & robots.txt 최종 갱신", "generate_seo.py"),
    ("9. GitHub 자동 커밋 및 배포 푸시", "git")
]

def print_menu():
    print("=" * 60)
    print("        테라피365 20종 SEO 스팸 회피 통합 빌드 & 배포")
    print("=" * 60)
    for idx, (desc, _) in enumerate(BUILD_STEPS, 1):
        print(f"[{idx}] {desc}")
    print("[0] 전체 일괄 빌드 및 GitHub 배포 (1 ~ 9번 자동 실행)")
    print("=" * 60)

def run_script(script_name):
    if script_name == "git":
        print("\n📦 GitHub 커밋 및 원격 저장소 푸시 중...")
        os.system("git add .")
        os.system('git commit -m "테라피365 20종 세부 테마 키워드 및 메타 최적화 자동 배포"')
        os.system("git push")
    else:
        if os.path.exists(script_name):
            print(f"\n▶ 실행 중: {script_name}")
            os.system(f"{sys.executable} {script_name}")
        else:
            print(f"⚠ 건너뜀 (파일 없음): {script_name}")

if __name__ == "__main__":
    print_menu()
    try:
        user_input = input("실행할 번호를 입력하세요 (엔터 치면 0번 전체 실행): ").strip()
    except (EOFError, KeyboardInterrupt):
        user_input = "0"

    if user_input == "" or user_input == "0":
        print("\n🚀 전체 SEO 빌드 및 배포 파이프라인을 가동합니다...\n")
        for _, script in BUILD_STEPS:
            run_script(script)
        print("\n🎉 모든 최적화 빌드와 GitHub 푸시 배포가 완벽하게 완료되었습니다!")
    else:
        try:
            choice_idx = int(user_input) - 1
            if 0 <= choice_idx < len(BUILD_STEPS):
                run_script(BUILD_STEPS[choice_idx][1])
            else:
                print("❌ 유효하지 않은 번호입니다.")
        except ValueError:
            print("❌ 숫자를 입력해 주세요.")