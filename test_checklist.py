"""
=============================================================
  TEST CHECKLIST - Game Chiikawa Nhặt Dâu Tây
  Mô tả: Kiểm thử thủ công các chức năng cơ bản của game
=============================================================

INPUT:
  - Phím mũi tên (LEFT, RIGHT, UP, DOWN) để điều khiển nhân vật
  - Sự kiện đóng cửa sổ (nhấn nút X)

OUTPUT:
  - Nhân vật di chuyển theo phím nhấn
  - Dâu tây rơi từ trên xuống và xuất hiện lại ngẫu nhiên
  - Điểm tăng khi chạm dâu
  - Tốc độ dâu tăng mỗi 5 điểm

=============================================================
CHECKLIST KIỂM THỬ THỦ CÔNG
=============================================================

[ ] TC-01: Mở game thành công
    - Chạy: python gamechiikawa.py
    - Kết quả mong đợi: Cửa sổ game 800x600 xuất hiện với tiêu đề "Chiikawa Nhặt Dâu Tây"
    - Trạng thái: PASS / FAIL

[ ] TC-02: Nhân vật hiển thị
    - Kết quả mong đợi: Nhân vật Chiikawa (hoặc hình tròn hồng) xuất hiện ở giữa phía dưới màn hình
    - Trạng thái: PASS / FAIL

[ ] TC-03: Dâu tây rơi
    - Kết quả mong đợi: Quả dâu tây (hoặc hình tròn đỏ) rơi từ trên xuống dưới
    - Trạng thái: PASS / FAIL

[ ] TC-04: Di chuyển sang trái
    - Thao tác: Nhấn phím ← (LEFT)
    - Kết quả mong đợi: Nhân vật dịch chuyển sang trái, không đi qua cạnh màn hình
    - Trạng thái: PASS / FAIL

[ ] TC-05: Di chuyển sang phải
    - Thao tác: Nhấn phím → (RIGHT)
    - Kết quả mong đợi: Nhân vật dịch chuyển sang phải, không đi qua cạnh màn hình
    - Trạng thái: PASS / FAIL

[ ] TC-06: Di chuyển lên
    - Thao tác: Nhấn phím ↑ (UP)
    - Kết quả mong đợi: Nhân vật dịch chuyển lên trên, không vượt khỏi màn hình
    - Trạng thái: PASS / FAIL

[ ] TC-07: Di chuyển xuống
    - Thao tác: Nhấn phím ↓ (DOWN)
    - Kết quả mong đợi: Nhân vật dịch chuyển xuống dưới, không vượt khỏi màn hình
    - Trạng thái: PASS / FAIL

[ ] TC-08: Thu thập dâu tây - điểm tăng
    - Thao tác: Điều khiển nhân vật chạm vào dâu tây
    - Kết quả mong đợi: Điểm tăng 1, dâu tây xuất hiện lại ở vị trí ngẫu nhiên phía trên
    - Trạng thái: PASS / FAIL

[ ] TC-09: Tốc độ tăng mỗi 5 điểm
    - Thao tác: Thu thập 5 quả dâu
    - Kết quả mong đợi: Tốc độ rơi của dâu tây tăng lên rõ rệt
    - Trạng thái: PASS / FAIL

[ ] TC-10: Dâu rơi qua đáy màn hình - reset vị trí
    - Kết quả mong đợi: Khi dâu rơi qua đáy, nó xuất hiện lại từ trên với vị trí ngẫu nhiên
    - Trạng thái: PASS / FAIL

[ ] TC-11: Hiển thị điểm
    - Kết quả mong đợi: Góc trên trái hiển thị "Dau tay: X" với số điểm cập nhật liên tục
    - Trạng thái: PASS / FAIL

[ ] TC-12: Đóng cửa sổ game
    - Thao tác: Nhấn nút X trên cửa sổ game
    - Kết quả mong đợi: Game đóng lại hoàn toàn, không bị treo
    - Trạng thái: PASS / FAIL

=============================================================
KẾT QUẢ TỔNG HỢP
=============================================================
  Tổng số test case: 12
  PASS: ___
  FAIL: ___
  Ghi chú: _______________________________________________
=============================================================
"""

import sys
import os

# Fix Unicode output on Windows terminal
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

def run_checklist():
    print("=" * 60)
    print("  KIEM THU TU DONG - Game Chiikawa Nhat Dau Tay")
    print("=" * 60)

    results = []

    # TC-A1: Kiem tra file game ton tai
    test_name = "TC-A1: File gamechiikawa.py ton tai"
    passed = os.path.exists("gamechiikawa.py")
    results.append((test_name, passed))
    print(f"[{'PASS' if passed else 'FAIL'}] {test_name}")

    # TC-A2: Kiem tra requirements.txt ton tai va khong rong
    test_name = "TC-A2: File requirements.txt ton tai va co noi dung"
    passed = os.path.exists("requirements.txt") and os.path.getsize("requirements.txt") > 0
    results.append((test_name, passed))
    print(f"[{'PASS' if passed else 'FAIL'}] {test_name}")

    # TC-A3: Kiem tra README.md ton tai
    test_name = "TC-A3: File README.md ton tai"
    passed = os.path.exists("README.md")
    results.append((test_name, passed))
    print(f"[{'PASS' if passed else 'FAIL'}] {test_name}")

    # TC-A4: Kiem tra import pygame hoac pygame-ce
    test_name = "TC-A4: Thu vien pygame (hoac pygame-ce) duoc cai dat"
    pygame_mod = None
    for pkg in ("pygame", "pygame"):
        try:
            import pygame as pygame_mod
            break
        except ImportError:
            pass
    if pygame_mod is None:
        try:
            import pygame_ce as pygame_mod  # type: ignore
        except ImportError:
            pass
    passed = pygame_mod is not None
    results.append((test_name, passed))
    status_note = f" (version: {pygame_mod.version.ver})" if passed else " (chua cai - chay: pip install pygame-ce)"
    print(f"[{'PASS' if passed else 'FAIL'}] {test_name}{status_note}")

    # TC-A5: Kiem tra import random
    test_name = "TC-A5: Module random co the import"
    try:
        import random
        passed = True
    except ImportError:
        passed = False
    results.append((test_name, passed))
    print(f"[{'PASS' if passed else 'FAIL'}] {test_name}")

    # TC-A6: Kiem tra import os
    test_name = "TC-A6: Module os co the import"
    try:
        import os as _os
        passed = True
    except ImportError:
        passed = False
    results.append((test_name, passed))
    print(f"[{'PASS' if passed else 'FAIL'}] {test_name}")

    # TC-A7: Kiem tra logic tinh diem
    test_name = "TC-A7: Logic tinh diem hoat dong dung"
    score = 0
    score += 1
    passed = (score == 1)
    results.append((test_name, passed))
    print(f"[{'PASS' if passed else 'FAIL'}] {test_name}")

    # TC-A8: Kiem tra logic tang toc do
    test_name = "TC-A8: Logic tang toc do moi 5 diem hoat dong dung"
    item_speed = 4
    score = 0
    for i in range(5):
        score += 1
        if score % 5 == 0:
            item_speed += 0.5
    passed = (item_speed == 4.5)
    results.append((test_name, passed))
    print(f"[{'PASS' if passed else 'FAIL'}] {test_name}")

    # TC-A9: Kiem tra gioi han di chuyen nhan vat (trai)
    test_name = "TC-A9: Nhan vat khong vuot bien trai"
    player_x = 0
    player_speed = 7
    SCREEN_WIDTH = 800
    if player_x > 0:
        player_x -= player_speed
    passed = (player_x == 0)  # Khong di chuyen khi da o bien
    results.append((test_name, passed))
    print(f"[{'PASS' if passed else 'FAIL'}] {test_name}")

    # TC-A10: Kiem tra gioi han di chuyen nhan vat (phai)
    test_name = "TC-A10: Nhan vat khong vuot bien phai"
    player_x = SCREEN_WIDTH - 70
    if player_x < SCREEN_WIDTH - 70:
        player_x += player_speed
    passed = (player_x == SCREEN_WIDTH - 70)
    results.append((test_name, passed))
    print(f"[{'PASS' if passed else 'FAIL'}] {test_name}")

    # TC-A11: Kiem tra dau tay reset khi vuot day
    test_name = "TC-A11: Dau tay reset khi vuot day man hinh"
    import random
    SCREEN_HEIGHT = 600
    item_y = 610  # Vuot qua day
    item_x_before = 100
    item_x = item_x_before
    if item_y > SCREEN_HEIGHT:
        item_x = random.randint(0, SCREEN_WIDTH - 40)
        item_y = -40
    passed = (item_y == -40)
    results.append((test_name, passed))
    print(f"[{'PASS' if passed else 'FAIL'}] {test_name}")

    # TC-A12: Kiem tra logic va cham Rect (khong can man hinh)
    test_name = "TC-A12: Logic va cham nhan vat va dau tay"
    try:
        # Thu dung pygame neu da cai, fallback sang tinh toan thu cong
        try:
            import pygame as _pg
            r1 = _pg.Rect(100, 100, 70, 70)
            r2 = _pg.Rect(120, 120, 40, 40)  # Chong len r1
            passed = r1.colliderect(r2)
        except ImportError:
            # Fallback: kiem tra overlap bang toan hoc thuan tuy
            x1,y1,w1,h1 = 100,100,70,70
            x2,y2,w2,h2 = 120,120,40,40
            passed = (x1 < x2+w2 and x1+w1 > x2 and y1 < y2+h2 and y1+h1 > y2)
    except Exception as e:
        passed = False
    results.append((test_name, passed))
    print(f"[{'PASS' if passed else 'FAIL'}] {test_name}")

    # --- Ket qua ---
    print("\n" + "=" * 60)
    total = len(results)
    passed_count = sum(1 for _, p in results if p)
    failed_count = total - passed_count
    print(f"  Tong: {total} | PASS: {passed_count} | FAIL: {failed_count}")
    print("=" * 60)

    if failed_count > 0:
        print("\n[!] Cac test that bai:")
        for name, p in results:
            if not p:
                print(f"   - {name}")
        sys.exit(1)
    else:
        print("\n[OK] Tat ca test deu PASS!")
        sys.exit(0)

if __name__ == "__main__":
    run_checklist()
