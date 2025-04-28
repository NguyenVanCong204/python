import pyshorteners
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

# URL gốc
url = "https://shopee.vn/product/27681309/28956884499?uls_trackid=52get973001g&utm_campaign=id_TeMBPlgf8M&utm_content=----&utm_medium=affiliates&utm_source=an_17309450142&utm_term=cvp62pnhan4w"

# Loại bỏ các tham số UTM
parsed_url = urlparse(url)
query_params = parse_qs(parsed_url.query)

# Loại bỏ các tham số UTM
utm_params = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content']
for param in utm_params:
    if param in query_params:
        del query_params[param]

# Tạo lại URL mà không có tham số UTM
new_query = urlencode(query_params, doseq=True)
new_url = urlunparse(parsed_url._replace(query=new_query))

# Rút gọn URL
s = pyshorteners.Shortener()
short_url = s.tinyurl.short(new_url)

print("🔗 Link rút gọn:", short_url)
