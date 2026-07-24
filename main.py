import os
def tim_file(ten_file, thu_muc_bat_dau):
    kiemtra = False
    print("[+] Đang tìm kiếm vui lòng chờ !")
    
    for root, dirs, files in os.walk(thu_muc_bat_dau):
        try:
            for file in files:
                if ten_file.lower() in file.lower():
                    kiemtra = True
                    print(f"Đường dẫn: {os.path.join(root, file)}")
        except PermissionError:
            # Bỏ qua thư mục không có quyền đọc và tiếp tục chạy
            continue
        except Exception as e:
            print(f"Lỗi :{e}")
            continue

    if kiemtra:
        print("[+] Đã quét xong!")
    else:
        print("[-] Không tìm thấy!")


def tim_flag(ten_file, duong_dan_dau_vao, danh_sach_key):
    kiemtra = False
    print("[+] Đang quét tìm flag vui lòng chờ !")

    # Danh sách chứa các đường dẫn file cần kiểm tra
    danh_sach_file = []

    # TRƯỜNG HỢP 1: Đầu vào là một FILE cụ thể
    if os.path.isfile(duong_dan_dau_vao):
        danh_sach_file.append(duong_dan_dau_vao)

    # TRƯỜNG HỢP 2: Đầu vào là một THƯ MỤC (dùng os.walk như cũ)
    elif os.path.isdir(duong_dan_dau_vao):
        for root, dirs, files in os.walk(duong_dan_dau_vao):
            try:
                for file in files:
                    if ten_file.lower() in file.lower():
                        danh_sach_file.append(os.path.join(root, file))
            except PermissionError:
                continue
            except Exception:
                continue
    else:
        print("[-] Đường dẫn không hợp lệ hoặc không tồn tại!")
        return

    # Tiến hành đọc và kiểm tra các file đã thu thập được
    for duong_dan in danh_sach_file:
        try:
            with open(duong_dan, "r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    for key in danh_sach_key:
                        sach_key = key.strip()
                        if sach_key:
                            # Thêm .lower() vào cả key và line để bỏ qua phân biệt hoa/thường hoàn toàn
                            if sach_key.lower() in line.lower():
                                kiemtra = True
                                print(f"[MATCH - Key: '{sach_key}']")
                                print(line.strip())
                                print(f"Đường dẫn: {duong_dan}\n")
        except Exception:
            continue

    if not kiemtra:
        print("[-] Không tìm thấy key nào!")
    else:
        print("[+] Đã quét xong!")


if __name__ == "__main__":
    # viết hàm main
    while True:
        print("\n=======================================")
        print("    [+] CHÀO MỪNG ĐẾN VỚI SCRIPT MINI [+]")
        print("=======================================")
        print("1. Tìm kiếm file theo tên")
        print("2. Tìm kiếm key_word trong file")
        print("3. Thoát chương trình")
        
        lua_chon = input("Nhập lựa chọn của mày (1-3): ").strip()

        if lua_chon == "1":
            print("\n--- CHỨC NĂNG: TÌM KIẾM FILE ---")
            ten_file = input("Nhập tên file cần tìm: ").strip()
            pham_vi = input("Nhập đường dẫn thư mục bắt đầu quét: ").strip()
            if os.path.exists(pham_vi):
                tim_file(ten_file, pham_vi)
            else:
                print("[-] Đường dẫn không tồn tại!")

        elif lua_chon == "2":
            print("\n--- CHỨC NĂNG: TÌM FLAG TRONG FILE---")
            ten_file = input("Nhập tên file chứa flag : ").strip()
            pham_vi = input("Nhập đường dẫn tới file có chứa flag, hoặc Thư mục cần quét: ").strip()
            if os.path.exists(pham_vi):
                nhap_key = input("Nhập danh sách key, cách nhau bằng dấu phẩy (VD: HTB, FLAG, admin): ").strip()
                danh_sach_key = nhap_key.split(",")
                tim_flag(ten_file, pham_vi,danh_sach_key)
            else:
                print("[-] Đường dẫn không tồn tại!")
                    
        elif lua_chon == "3":
            print("\n[+] Đang thoát chương trình. Tạm biệt mày!")
            break
        else:
            print("\n[-] Lựa chọn không hợp lệ! Vui lòng chọn từ 1 đến 3.")
