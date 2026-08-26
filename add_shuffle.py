# -*- coding: utf-8 -*-
import os
import re

SHUFFLE_SCRIPT = """
    <!-- Vendor Card Random Shuffle Script -->
    <script>
    document.addEventListener("DOMContentLoaded", function () {
        const cards = Array.from(document.querySelectorAll(".vendor-card"));
        if (cards.length <= 1) return;

        // 다른 섹션(지도, 후기 등)의 순서가 뒤로 밀리지 않도록 첫 번째 카드 앞에 기준점 생성
        const firstCard = cards[0];
        const container = firstCard.parentNode;
        const anchor = document.createElement("div");
        anchor.style.display = "none";
        container.insertBefore(anchor, firstCard);

        // 피셔-예이츠 셔플 알고리즘
        for (let i = cards.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [cards[i], cards[j]] = [cards[j], cards[i]];
        }

        // 기준점 위치 뒤로 순서대로 재배치 및 랭킹 뱃지 넘버링 갱신
        cards.forEach((card, idx) => {
            const badge = card.querySelector(".vendor-rank, .vendor-badge");
            if (badge) {
                badge.textContent = `추천 ${String(idx + 1).padStart(2, '0')}`;
            }
            container.insertBefore(card, anchor);
        });

        // 기준점 제거
        anchor.remove();
    });
    </script>
"""

count = 0
for root, dirs, files in os.walk("."):
    # 숨김 폴더(.git 등) 제외
    if any(part.startswith(".") for part in root.split(os.sep)):
        continue

    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # vendor-card가 존재하고 셔플 스크립트가 아직 없는 경우에만 주입
            if "vendor-card" in content and "Vendor Card Random Shuffle Script" not in content:
                content = re.sub(r'(</body>)', rf'{SHUFFLE_SCRIPT.strip()}\n\1', content, flags=re.IGNORECASE)
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                count += 1

print(f"✔ 총 {count}개 HTML 파일에 안전한 '업체 카드 실시간 랜덤 셔플' 스크립트가 적용되었습니다!")