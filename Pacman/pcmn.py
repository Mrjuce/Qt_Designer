import pygame
import random

pygame.init()

# Розміри екрану
WIDTH, HEIGHT = 800, 600
FPS = 30

# Кольори
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Шрифти
font = pygame.font.Font(None, 36)

# Параметри персонажа
pacman_size = 30
pacman_speed = 5
pacman_direction = 0  # 0 - вправо, 1 - вниз, 2 - вліво, 3 - вгору

# Створення екрану
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man")

# Створення об'єкта Pac-Man
pacman = pygame.Rect(WIDTH // 2 - pacman_size // 2, HEIGHT // 2 - pacman_size // 2, pacman_size, pacman_size)

# Створення ворогів
enemy_size = 30
enemies = [pygame.Rect(random.randint(0, WIDTH - enemy_size), random.randint(0, HEIGHT - enemy_size), enemy_size, enemy_size) for _ in range(3)]

# Створення стін лабіринту
walls = [
    pygame.Rect(50, 50, 150, 30),
    pygame.Rect(250, 50, 30, 150),
    pygame.Rect(400, 50, 150, 30),
    pygame.Rect(50, 250, 30, 150),
    pygame.Rect(200, 250, 150, 30),
    pygame.Rect(400, 250, 30, 150),
    pygame.Rect(550, 250, 150, 30),
    pygame.Rect(50, 450, 150, 30),
    pygame.Rect(250, 450, 30, 150),
    pygame.Rect(400, 450, 150, 30),
]

# Створення точок (перевірка на зіткнення зі стінами та ворогами)
points = []
while len(points) < 10:
    point = pygame.Rect(random.randint(0, WIDTH - 10), random.randint(0, HEIGHT - 10), 10, 10)
    if not any(point.colliderect(wall) for wall in walls) and not any(point.colliderect(enemy) for enemy in enemies):
        points.append(point)

# Головний цикл гри
clock = pygame.time.Clock()

def draw_text(text, x, y):
    """Функція для виведення тексту на екран"""
    rendered_text = font.render(text, True, WHITE)
    screen.blit(rendered_text, (x, y))

def move_pacman(pacman, keys):
    """Функція для переміщення Pac-Man"""
    global pacman_direction
    if keys[pygame.K_LEFT] and pacman_direction != 0:
        pacman_direction = 2
    elif keys[pygame.K_RIGHT] and pacman_direction != 2:
        pacman_direction = 0
    elif keys[pygame.K_UP] and pacman_direction != 1:
        pacman_direction = 3
    elif keys[pygame.K_DOWN] and pacman_direction != 3:
        pacman_direction = 1

    # Рухаємо Pac-Man в залежності від напрямку
    if pacman_direction == 0:  # Вправо
        pacman.x += pacman_speed
    elif pacman_direction == 1:  # Вниз
        pacman.y += pacman_speed
    elif pacman_direction == 2:  # Вліво
        pacman.x -= pacman_speed
    elif pacman_direction == 3:  # Вгору
        pacman.y -= pacman_speed

    # Перевірка на зіткнення зі стінами та повернення назад
    for wall in walls:
        if pacman.colliderect(wall):
            if pacman_direction == 0:
                pacman.x -= pacman_speed
            elif pacman_direction == 1:
                pacman.y -= pacman_speed
            elif pacman_direction == 2:
                pacman.x += pacman_speed
            elif pacman_direction == 3:
                pacman.y += pacman_speed

def check_collisions(pacman, points, enemies):
    """Функція для перевірки зіткнень з точками та ворогами"""
    global score
    # Перевірка зіткнень з точками
    for point in points[:]:
        if pacman.colliderect(point):
            points.remove(point)
            score += 1
    # Перевірка зіткнень з ворогами
    for enemy in enemies:
        if pacman.colliderect(enemy):
            return False  # Якщо зіткнення з ворогом, програш
    return True

score = 0
running = True
game_over = False  # Змінна для відстеження Game Over

while running:
    screen.fill(BLACK)

    # Перевірка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:  # Гра продовжується, якщо не Game Over
        # Отримуємо натискання клавіш
        keys = pygame.key.get_pressed()

        # Переміщуємо Pac-Man
        move_pacman(pacman, keys)

        # Перевірка зіткнень
        if not check_collisions(pacman, points, enemies):
            game_over = True  # Game Over

        # Якщо всі точки зібрані
        if not points:
            draw_text("Рівень пройдено!", WIDTH // 2 - 100, HEIGHT // 2)
            pygame.display.update()
            pygame.time.delay(2000)  # Затримка 2 секунди перед виходом
            running = False  # Вихід з гри

    # Виведення результату
    draw_text(f"Score: {score}", 10, 10)

    # Малюємо Pac-Man
    pygame.draw.circle(screen, YELLOW, pacman.center, pacman_size // 2)

    # Малюємо ворогів
    for enemy in enemies:
        pygame.draw.rect(screen, BLUE, enemy)

    # Малюємо стіни
    for wall in walls:
        pygame.draw.rect(screen, RED, wall)

    # Малюємо точки
    for point in points:
        pygame.draw.rect(screen, WHITE, point)

    if game_over:  # Виводимо Game Over, якщо game_over == True
        draw_text("Game Over", WIDTH // 2 - 80, HEIGHT // 2)
        draw_text(f"Score: {score}", WIDTH // 2 - 60, HEIGHT // 2 + 40)

    pygame.display.update()

    # Обмеження FPS
    clock.tick(FPS)

pygame.quit()