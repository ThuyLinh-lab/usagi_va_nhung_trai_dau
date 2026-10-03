"""
gamechiikawa.py
===============
Game 2D: Chiikawa Nhat Dau Tay
Ngon ngu: Python 3.10+
Thu vien: pygame >= 2.0.0

Mo ta:
    Nguoi choi dieu khien nhan vat Chiikawa (phim mui ten) de nhat
    dau tay roi tu tren xuong. Moi lan cham duoc 1 diem. Cu 5 diem,
    toc do roi tang them 0.5 de tang do kho.

Input:
    - Phim Left/Right/Up/Down: Di chuyen nhan vat
    - Su kien dong cua so (X): Thoat game

Output:
    - Cua so 800x600 px hien thi nhan vat, dau tay, va diem so
"""

import pygame
import random
import os

# ============================================================
# 1. KHOI TAO PYGAME
# ============================================================
pygame.init()

# --- Cau hinh man hinh ---
SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chiikawa Nhat Dau Tay")

# --- FPS ---
clock = pygame.time.Clock()
FPS   = 60

# ============================================================
# 2. MAU SAC
# ============================================================
WHITE = (255, 255, 255)
BLACK = (0,   0,   0)
GREEN = (200, 245, 200)  # Nen co xanh diu
PINK  = (255, 182, 193)  # Dai dien nhan vat (neu thieu anh)
RED   = (235, 64,  52)   # Dai dien dau tay  (neu thieu anh)

# ============================================================
# 3. TAI HINH ANH
#    Ho tro .png (tach nen trong suot) va .jpg
# ============================================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_image(candidates, size):
    """
    Thu tai anh tu danh sach duong dan uu tien.
    Tu dong tim kiem theo BASE_DIR cua file game.
    Tra ve Surface da scale (convert_alpha), hoac None neu khong tim thay.

    Input : candidates (list[str]) - danh sach duong dan
            size       (tuple)     - (width, height) can scale
    Output: pygame.Surface | None
    """
    for name in candidates:
        possible_paths = [
            os.path.join(BASE_DIR, name),
            name,
            os.path.join(os.getcwd(), name)
        ]
        for path in possible_paths:
            if os.path.exists(path):
                try:
                    img = pygame.image.load(path)
                    # Ho tro nen trong suot neu co
                    try:
                        img = img.convert_alpha()
                    except Exception:
                        pass
                    scaled = pygame.transform.smoothscale(img, size)
                    print(f"[OK] Da tai thanh cong hinh anh: {name} (kich thuoc: {size})")
                    return scaled
                except Exception as err:
                    print(f"[LOI] Khong the tai anh {path}: {err}")
    print(f"[CANH BAO] Khong tim thay anh nao trong: {candidates}")
    return None

# ============================================================
# 4. THONG SO GAME
# ============================================================
# Nhan vat (Usagi)
PLAYER_W       = 75
PLAYER_H       = 95
PLAYER_SPEED   = 7
player_x       = SCREEN_WIDTH  // 2 - PLAYER_W // 2
player_y       = SCREEN_HEIGHT - PLAYER_H - 30

player_img = load_image(
    ["usagi.png", "usagi.jpg", "chiikawa.png", "chiikawa.jpg"],
    (PLAYER_W, PLAYER_H)
)
item_img = load_image(
    ["strawberry.png", "strawberry.jpg"],
    (40, 40)
)

# Dau tay
ITEM_W         = 40
ITEM_H         = 40
ITEM_SPEED_INIT = 4.0
item_speed     = ITEM_SPEED_INIT
item_x         = random.randint(0, SCREEN_WIDTH - ITEM_W)
item_y         = -ITEM_H

# Diem so
score = 0
font  = pygame.font.SysFont("Arial", 28, bold=True)

# ============================================================
# 5. HAM HO TRO
# ============================================================
def draw_score(surface, score):
    """Ve diem so len goc tren trai man hinh.
    Input : surface (pygame.Surface), score (int)
    Output: None (ve truc tiep len surface)
    """
    text = font.render(f"Dau tay: {score}", True, BLACK)
    surface.blit(text, (20, 20))


def draw_player(surface, x, y):
    """Ve nhan vat: dung anh neu co, fallback sang hinh tron hong.
    Input : surface, x (int), y (int)
    Output: None
    """
    if player_img:
        surface.blit(player_img, (x, y))
    else:
        pygame.draw.circle(surface, PINK,
                           (x + PLAYER_W // 2, y + PLAYER_H // 2),
                           PLAYER_W // 2)


def draw_item(surface, x, y):
    """Ve dau tay: dung anh neu co, fallback sang hinh tron do.
    Input : surface, x (int), y (int)
    Output: None
    """
    if item_img:
        surface.blit(item_img, (x, y))
    else:
        pygame.draw.circle(surface, RED,
                           (x + ITEM_W // 2, y + ITEM_H // 2),
                           ITEM_W // 2)


def reset_item():
    """Reset dau tay ve vi tri ngau nhien phia tren man hinh.
    Input : None
    Output: (new_x, new_y) tuple[int, int]
    """
    new_x = random.randint(0, SCREEN_WIDTH - ITEM_W)
    new_y = -ITEM_H
    return new_x, new_y

# ============================================================
# 6. VONG LAP CHINH
# ============================================================
running = True
while running:
    clock.tick(FPS)

    # --- Xu ly su kien ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Dieu khien nhan vat (Input) ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]  and player_x > 0:
        player_x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - PLAYER_W:
        player_x += PLAYER_SPEED
    if keys[pygame.K_UP]    and player_y > 0:
        player_y -= PLAYER_SPEED
    if keys[pygame.K_DOWN]  and player_y < SCREEN_HEIGHT - PLAYER_H:
        player_y += PLAYER_SPEED

    # --- Cap nhat vi tri dau tay ---
    item_y += item_speed
    if item_y > SCREEN_HEIGHT:
        item_x, item_y = reset_item()

    # --- Kiem tra va cham ---
    player_rect = pygame.Rect(player_x, player_y, PLAYER_W, PLAYER_H)
    item_rect   = pygame.Rect(item_x,   item_y,   ITEM_W,   ITEM_H)

    if player_rect.colliderect(item_rect):
        score += 1
        item_x, item_y = reset_item()
        if score % 5 == 0:
            item_speed += 0.5  # Tang do kho moi 5 diem

    # --- Ve man hinh (Output) ---
    screen.fill(GREEN)
    draw_player(screen, player_x, player_y)
    draw_item(screen, item_x, int(item_y))
    draw_score(screen, score)
    pygame.display.update()

# ============================================================
# 7. THOAT
# ============================================================
pygame.quit()
