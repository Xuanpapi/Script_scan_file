# 🚀 File & Flag Hunter Tool

Một công cụ viết bằng Python giúp mày quét tìm kiếm file theo tên hoặc tự động rà soát nội dung bên trong các file để tìm `flag` (hoặc các từ khóa bí mật khác) trên toàn bộ máy tính hoặc một thư mục cụ thể. Thích hợp cho dân chơi CTF hoặc tự động hóa tìm kiếm file nhanh.

---

## ✨ Tính năng chính

1. **Tìm kiếm file theo tên:** Hỗ trợ quét không phân biệt hoa/thường, tìm nhanh trong thư mục chỉ định hoặc quét sạch tất cả các ổ đĩa trên máy (`C:\`, `D:\`,...).
2. **Quét nội dung tìm Flag/Key:** 
   - Hỗ trợ tìm kiếm **nhiều key cùng lúc** (cách nhau bằng dấu phẩy).
   - Không phân biệt chữ hoa hay chữ thường (Case-insensitive).
   - Tự động bỏ qua các thư mục bị khóa quyền truy cập (`PermissionError`) để không bị văng lỗi giữa chừng.
3. **Menu tương tác linh hoạt:** Giao diện dòng lệnh (CLI) thân thiện với 3 lựa chọn dễ thao tác.

## Mẹo nhỏ khi nhập đường dẫn tìm kiếm
    -Đường dẫn càng chi tiết càng tốt
    -Nếu muốn quét cả Ổ thì cú pháp :ví dụ C:\ hoặc E:\ vv
    
---

## 🛠️ Hướng dẫn cài đặt & Sử dụng

### 1. Clone repo về máy
```bash
git clone https://github.com/Xuanpapi/Script_scan_file.git