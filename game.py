import pygame
import math
import time
import sys

pygame.init()

width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Йога-тест: 60 секунд концентрации. Игра - кто меньше раз отвлечётся")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GRAY = (150, 150, 150)
BUTTON_COLOR = (70, 130, 180)
BUTTON_HOVER_COLOR = (50, 100, 150)

# Шрифты
font_small = pygame.font.SysFont('Arial', 24)
font_instruction = pygame.font.SysFont('Arial', 28)

center = (width // 2, height // 2)
clock_radius = 200

# Кнопка "Старт"
button_rect = pygame.Rect(20, 20, 100, 40)
button_active = False
game_started = False


def draw_clock(seconds, minutes, hours):
    screen.fill(WHITE)

    # Рисуем кнопку
    button_color = BUTTON_HOVER_COLOR if button_rect.collidepoint(pygame.mouse.get_pos()) else BUTTON_COLOR
    pygame.draw.rect(screen, button_color, button_rect, border_radius=5)
    button_text = font_small.render("Старт", True, WHITE)
    screen.blit(button_text, (button_rect.x + 30, button_rect.y + 10))

    # Циферблат
    pygame.draw.circle(screen, BLACK, center, clock_radius, 2)

    # Метки часов
    for i in range(12):
        angle = math.radians(i * 30 - 90)
        x = center[0] + (clock_radius - 20) * math.cos(angle)
        y = center[1] + (clock_radius - 20) * math.sin(angle)
        pygame.draw.circle(screen, BLACK, (int(x), int(y)), 5)

    if game_started:
        # Часовая стрелка (10 часов)
        hours_angle = math.radians(hours * 30 + minutes * 0.5 - 90)
        hours_end = (
            center[0] + (clock_radius - 70) * math.cos(hours_angle),
            center[1] + (clock_radius - 70) * math.sin(hours_angle)
        )
        pygame.draw.line(screen, GREEN, center, hours_end, 6)

        # Минутная стрелка (0 минут)
        minutes_angle = math.radians(minutes * 6 - 90)
        minutes_end = (
            center[0] + (clock_radius - 40) * math.cos(minutes_angle),
            center[1] + (clock_radius - 40) * math.sin(minutes_angle)
        )
        pygame.draw.line(screen, BLUE, center, minutes_end, 4)

        # Секундная стрелка
        seconds_angle = math.radians(seconds * 6 - 90)
        seconds_end = (
            center[0] + (clock_radius - 20) * math.cos(seconds_angle),
            center[1] + (clock_radius - 20) * math.sin(seconds_angle)
        )
        pygame.draw.line(screen, RED, center, seconds_end, 2)

    # Центральная точка
    pygame.draw.circle(screen, BLACK, center, 8)

    # Текст инструкции под часами
    instruction_text = font_instruction.render("Наблюдайте за секундной стрелкой", True, BLACK)
    text_rect = instruction_text.get_rect(center=(width // 2, height - 50))
    screen.blit(instruction_text, text_rect)

    pygame.display.flip()


def main():
    global game_started, button_active

    start_time = time.time()
    running = True
    clock = pygame.time.Clock()

    while running:
        current_time = time.time()
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button_rect.collidepoint(mouse_pos) and not game_started:
                    game_started = True
                    start_time = time.time()

        if game_started:
            elapsed = current_time - start_time
            if elapsed >= 60:
                game_started = False
            else:
                seconds = int(elapsed) % 60
                draw_clock(seconds, 0, 10)
        else:
            draw_clock(0, 0, 10)

        clock.tick(30)


if __name__ == "__main__":
    main()
    pygame.quit()