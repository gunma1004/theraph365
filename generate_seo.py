# -*- coding: utf-8 -*-
import os
import glob
from datetime import datetime

# 3호점 정식 도메인 주소
BASE_URL = "https://theraphy365.pages.dev"
today = datetime.today().strftime('%Y-%m-%d')

# 1. robots.txt 새로 생성 (Sitemap 주소 동기화)
robots_content = f"""User-agent: *
Allow: /

Sitemap: {BASE_URL}/sitemap.xml
"""
with open("robots.txt", "w", encoding="utf-8") as f:
    f.write(robots_content)

# 2. 모든 HTML 파일 탐색하여 sitemap.xml 및 urllist.txt 생성
html_files = []
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(file_path, ".").replace("\\", "/")
            
            # 깃허브/시스템 숨김 폴더 제외
            if rel_path.startswith("."):
                continue
                
            if rel_path == "index.html":
                url = f"{BASE_URL}/"
                priority = "1.0"
            elif rel_path.endswith("index.html"):
                folder = rel_path.rsplit("/index.html", 1)[0]
                url = f"{BASE_URL}/{folder}/"
                priority = "0.9"
            else:
                url = f"{BASE_URL}/{rel_path}"
                priority = "0.8"
                
            html_files.append((url, priority))

# sitemap.xml 작성
sitemap_lines = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
]

urllist_lines = []

for url, priority in html_files:
    sitemap_lines.append("  <url>")
    sitemap_lines.append(f"    <loc>{url}</loc>")
    sitemap_lines.append(f"    <lastmod>{today}</lastmod>")
    sitemap_lines.append("    <changefreq>daily</changefreq>")
    sitemap_lines.append(f"    <priority>{priority}</priority>")
    sitemap_lines.append("  </url>")
    urllist_lines.append(url)

sitemap_lines.append("</urlset>")

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write("\n".join(sitemap_lines))

with open("urllist.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(urllist_lines))

print(f"✔ robots.txt의 사이트맵 주소가 '{BASE_URL}/sitemap.xml' 로 변경되었습니다.")
print(f"✔ 총 {len(html_files)}개 페이지가 포함된 sitemap.xml 및 urllist.txt가 완벽히 재생성되었습니다.")
