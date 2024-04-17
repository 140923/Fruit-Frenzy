import pgzrun
import random

WIDTH = 800
HEIGHT = 600

apple = Actor('apple')
score = 0
level = 1
update_timer = 60  # Initial timer value, equivalent to 1 second at 60 FPS

def draw():
    screen.clear()
    apple.draw()
    screen.draw.text("Score: " + str(score), color="white", topleft=(10, 10))
    screen.draw.text("Level: " + str(level), color="white", topleft=(10, 30))

def apple_place():
    apple.x = random.randint(apple.width // 2, WIDTH - apple.width // 2)
    apple.y = random.randint(apple.height // 2, HEIGHT - apple.height // 2)


def update():
    global update_timer
    update_timer -= 1
    print(update_timer)
    if update_timer == 0:
        apple_place()
        update_timer = max(60 - level * 5, 10)  # Decrease timer with increasing level, minimum 10 frames

def on_mouse_down(pos):
    global score, level
    if apple.collidepoint(pos):
        score += 1
        print("Good Shot! Score:", score)
        if score % 5 == 0:
            level += 1
            print("Level Up! Level:", level)
    else:
        print("Game Over! Final Score:", score, "at level:",level)
        quit()

apple_place()
pgzrun.go()

