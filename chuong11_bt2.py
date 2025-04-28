from googlesearch import search
import requests
from bs4 import BeautifulSoup

singer = input("Nhập tên ca sĩ: ")
query = f"{singer} songs and albums site:en.wikipedia.org"

print("🔎 Đang tìm kiếm trên Google...")
results = list(search(query, num_results=5))

# Lọc các link hợp lệ (bắt đầu bằng http)
valid_links = [url for url in results if url.startswith("http")]

# In ra các link tìm được
for idx, url in enumerate(valid_links):
    print(f"[{idx+1}] {url}")

if not valid_links:
    print("❌ Không tìm thấy kết quả phù hợp.")
else:
    url = valid_links[0]
    print(f"\n📄 Đang lấy dữ liệu từ: {url}")

    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    print("\n📌 Tiêu đề trang:", soup.title.string)

    print("\n🎵 Danh sách bài hát và album (gợi ý):\n")
    for li in soup.select("li"):
        text = li.get_text()
        if "album" in text.lower() or "song" in text.lower():
            print("•", text)
