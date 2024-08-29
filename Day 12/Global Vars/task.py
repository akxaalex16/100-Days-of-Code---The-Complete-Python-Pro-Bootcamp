# Modifying Global Scope

enemies = 1


def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")


def increase_enemies_2(enemy):
    print(f"enemies inside function: {enemies}")
    return enemy + 1


increase_enemies()
print(f"enemies outside function: {enemies}")

enemies = increase_enemies_2(enemies)
print(f"enemies outside function: {enemies}")