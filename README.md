# 🍓 Game Chiikawa Nhặt Dâu Tây (Pygame)

> **Mục tiêu dự án:** Xây dựng game 2D đơn giản bằng Python và thư viện Pygame, giúp người chơi điều khiển nhân vật Chiikawa di chuyển và nhặt dâu tây rơi từ trên xuống để tích lũy điểm cao nhất có thể.

---

## 📁 Cấu Trúc Dự Án

```text
pygamechiikawa/
│
├── gamechiikawa.py      # File mã nguồn chính (logic game, giao diện, vòng lặp)
├── test_checklist.py    # Kiểm thử tự động + checklist thủ công
├── requirements.txt     # Danh sách thư viện phụ thuộc
├── .gitignore           # Bỏ qua các file không cần theo dõi
├── README.md            # Tài liệu hướng dẫn dự án (file này)
├── chiikawa.jpg         # (Tuỳ chọn) Hình ảnh nhân vật Chiikawa
└── strawberry.jpg       # (Tuỳ chọn) Hình ảnh quả dâu tây
```

---

## 🚀 Hướng Dẫn Cài Đặt & Chạy Game

### 1. Yêu cầu hệ thống
- **Python 3.10+** (khuyến nghị) đã được cài đặt.
- Hệ điều hành: Windows / macOS / Linux.
- Công cụ: VS Code hoặc bất kỳ trình soạn thảo nào.

### 2. Cài đặt thư viện phụ thuộc

```bash
pip install -r requirements.txt
```

Hoặc cài thủ công:

```bash
pip install pygame
```

> Nếu gặp lỗi `pip`, dùng: `python -m pip install -r requirements.txt`

### 3. Chạy Game

```bash
python gamechiikawa.py
```

Hoặc mở file `gamechiikawa.py` trong VS Code và nhấn nút **▶ Run**.

### 4. Chạy Kiểm Thử

```bash
python test_checklist.py
```

---

## 📥 Input & 📤 Output

### Input (Đầu vào)
| Input | Loại | Mô tả |
|-------|------|-------|
| Phím `←` (LEFT) | Bàn phím | Di chuyển nhân vật sang trái |
| Phím `→` (RIGHT) | Bàn phím | Di chuyển nhân vật sang phải |
| Phím `↑` (UP) | Bàn phím | Di chuyển nhân vật lên trên |
| Phím `↓` (DOWN) | Bàn phím | Di chuyển nhân vật xuống dưới |
| Nhấn nút X cửa sổ | Chuột | Đóng game |

### Output (Đầu ra)
| Output | Mô tả |
|--------|-------|
| Cửa sổ game 800×600 px | Màn hình nền xanh, hiển thị nhân vật và dâu tây |
| Điểm số (góc trên trái) | `Dau tay: X` — cập nhật theo thời gian thực |
| Dâu tây rơi | Xuất hiện ngẫu nhiên, rơi từ trên xuống |
| Tốc độ tăng | Cứ mỗi 5 điểm, tốc độ dâu tăng thêm 0.5 |

### Ví dụ luồng chơi
```
[Khởi động]  → Cửa sổ game mở, Chiikawa ở giữa phía dưới
[Phím →]     → Chiikawa dịch phải 7px mỗi frame
[Chạm dâu]  → Điểm: 0 → 1, dâu reset vị trí mới
[5 điểm]    → Tốc độ dâu: 4.0 → 4.5
[10 điểm]   → Tốc độ dâu: 4.5 → 5.0
[Nhấn X]    → Game đóng hoàn toàn
```

---

## 🎮 Cách Chơi

| Phím | Hành động |
|------|-----------|
| `←` | Di chuyển trái |
| `→` | Di chuyển phải |
| `↑` | Di chuyển lên |
| `↓` | Di chuyển xuống |

**Quy tắc:**
1. Điều khiển Chiikawa chạm vào dâu tây đang rơi để **+1 điểm**.
2. Cứ mỗi **5 điểm**, tốc độ rơi của dâu tăng thêm — thử thách hơn!
3. Nếu chưa có file ảnh, game tự dùng hình vẽ mặc định (tròn hồng/đỏ).

---

## 🗺️ Phạm Vi & Lộ Trình Phát Triển

### MVP (Tuần 1 - Đã hoàn thành ✅)
- [x] Nhân vật di chuyển 4 hướng bằng phím mũi tên
- [x] Dâu tây rơi từ trên xuống ngẫu nhiên
- [x] Phát hiện va chạm và tính điểm
- [x] Tốc độ tăng dần theo điểm số
- [x] Hiển thị điểm real-time

### Kế hoạch mở rộng (Tuần 2+)
- [ ] Thêm màn hình "Game Over" khi bỏ lỡ dâu
- [ ] Thêm âm thanh khi nhặt dâu
- [ ] Bảng xếp hạng điểm cao (High Score)
- [ ] Nhiều loại vật phẩm (bonus / bẫy)
- [ ] Menu bắt đầu / thoát

---

## 🧪 Kiểm Thử

File [`test_checklist.py`](test_checklist.py) bao gồm:
- **12 test case tự động** kiểm tra logic game (tính điểm, giới hạn di chuyển, va chạm,...)
- **Checklist thủ công** với 12 mục để tester xác nhận khi chạy game thực tế

```bash
python test_checklist.py
# Output mong đợi: 🎉 Tất cả test đều PASS!
```

---

## 📦 Phụ Thuộc

| Thư viện | Phiên bản | Mục đích |
|----------|-----------|---------|
| `pygame` | ≥ 2.0.0 | Vòng lặp game, render, sự kiện bàn phím |

---

## 📜 Nguồn Dữ Liệu & Đạo Đức

- Nhân vật **Chiikawa** là IP của tác giả Nagano (nagano_chiikawa). Dự án này chỉ phục vụ **mục đích học tập**, không thương mại.
- Không sử dụng dữ liệu người dùng, không có kết nối mạng, không lưu thông tin nhạy cảm.
- Hình ảnh minh họa (nếu có) được sử dụng cho mục đích phi thương mại / học thuật.

---

## 👤 Tác Giả

Dự án học tập môn Lập trình Python — Game 2D với Pygame.
https://github.com/pygame/pygame