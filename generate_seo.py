# -*- coding: utf-8 -*-
import os
from datetime import datetime

BASE_URL = "https://theraphy365.pages.dev"
today = datetime.today().strftime('%Y-%m-%d')

# 1. robots.txt 생성
robots_content = f"""User-agent: *
Allow: /

User-agent: Yeti
Allow: /

User-agent: Googlebot
Allow: /

Sitemap: {BASE_URL}/sitemap.xml
"""
with open("robots.txt", "w", encoding="utf-8") as f:
    f.write(robots_content)

# 2. sitemap.xml & urllist.txt 생성
html_files = []
seen_urls = set()

for root, dirs, files in os.walk("."):
    # .git, .vscode 등 실제 숨김 폴더만 제외 (현재폴더 . 은 정상 포함)
    parts = root.replace("\\", "/").split("/")
    if any(p.startswith(".") and p not in [".", ".."] for p in parts):
        continue

    for file in files:
        if file.lower().endswith(".html"):
            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(file_path, ".").replace("\\", "/")
            
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
                
            if url not in seen_urls:
                seen_urls.add(url)
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

print(f"✔ robots.txt 갱신 완료")
print(f"✔ 총 {len(html_files)}개 정상 URL이 sitemap.xml 및 urllist.txt에 완벽히 등록되었습니다!")
