import os
from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = int(os.environ.get("PORT", 8080))

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"""
        <!DOCTYPE html>
        <html>
        <head><title>Masirino</title></head>
        <body style="background:#0f0c29;color:white;text-align:center;padding:50px;font-family:Tahoma;direction:rtl">
            <h1 style="font-size:3rem">🎓 مسیرینو</h1>
            <p style="font-size:1.5rem">مشاور هوشمند تحصیلی</p>
            <p style="color:#10b981">✅ سرور با موفقیت اجرا شد!</p>
            <p style="color:#c4c4f0">پورت: """ + str(PORT).encode() + b"""</p>
        </body>
        </html>
        """)

print("🚀 سرور در حال اجرا...")
server = HTTPServer(("0.0.0.0", PORT), Handler)
print(f"✅ سرور روی پورت {PORT} اجرا شد")
server.serve_forever()
