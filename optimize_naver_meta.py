# -*- coding: utf-8 -*-
import os
import re

# 프로젝트 내의 모든 index.html (루트 및 강남 등 모든 지역 폴더) 탐색
html_files = []
for root, dirs, files in os.walk("."):
    # 숨김 폴더(.git 등) 제외
    if any(part.startswith(".") for part in root.split(os.sep)):
        continue
    if "index.html" in files:
        html_files.append(os.path.join(root, "index.html"))

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. 기존 <title> 내용 추출
    title_match = re.search(r'<title>(.*?)</title>', content, flags=re.DOTALL)
    current_title = title_match.group(1).strip() if title_match else "테라피365"

    # 2. 기존 <meta name="description"> 내용 추출
    desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']\s*/?>', content, flags=re.DOTALL)
    current_desc = desc_match.group(1).strip() if desc_match else "테라피365 제휴점 안내"

    # 3. og:title 교체 또는 추가
    if re.search(r'<meta\s+property=["\']og:title["\']', content):
        content = re.sub(r'<meta\s+property=["\']og:title["\']\s+content=["\'].*?["\']\s*/?>',
                         f'<meta property="og:title" content="{current_title}">', content, flags=re.DOTALL)
    else:
        content = content.replace("</head>", f'    <meta property="og:title" content="{current_title}">\n</head>')

    # 4. og:description 교체 또는 추가
    if re.search(r'<meta\s+property=["\']og:description["\']', content):
        content = re.sub(r'<meta\s+property=["\']og:description["\']\s+content=["\'].*?["\']\s*/?>',
                         f'<meta property="og:description" content="{current_desc}">', content, flags=re.DOTALL)
    else:
        content = content.replace("</head>", f'    <meta property="og:description" content="{current_desc}">\n</head>')

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✔ 적용 완료: {file_path}")

print("\n🎉 gangnam을 포함한 모든 지역 페이지의 Open Graph 태그가 적용되었습니다!")