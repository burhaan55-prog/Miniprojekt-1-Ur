
import pygame
import math
import datetime

pygame.init()

screen = pygame.display.set_mode((640, 480))

start_point = (320, 240)
length = 180

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((255, 255, 255))
    # Cirkel rundt om uret
    pygame.draw.circle(screen,(0,0,0), start_point, 190, 2)

    # Lektion 2 + 3: De 12 streger til uret
    for i in range(12):
        angle = i * 30

        start_x = start_point[0] + 160 * math.cos(math.radians(angle))
        start_y = start_point[1] + 160 * math.sin(math.radians(angle))

        end_x = start_point[0] + length * math.cos(math.radians(angle))
        end_y = start_point[1] + length * math.sin(math.radians(angle))

        start = (start_x, start_y)
        end_point = (end_x, end_y)

        pygame.draw.line(screen, (0,0,0), start, end_point, 5)

    # sekundviser
    now = datetime.datetime.now()
    seconds = now.second
    angle = seconds * 6 - 90

    end_x = start_point[0] + 150 * math.cos(math.radians(angle))
    end_y = start_point[1] + 150 * math.sin(math.radians(angle))

    end_point = (end_x, end_y)

    pygame.draw.line(screen, (255,0,0), start_point, end_point, 5)

    
    # minutviser
    minutes = now.minute + seconds / 60
    angle = minutes * 6 - 90

    end_x = start_point[0] + 110 * math.cos(math.radians(angle))
    end_y = start_point[1] + 110 * math.sin(math.radians(angle))

    end_point = (end_x, end_y)

    pygame.draw.line(screen, (0,0,0), start_point, end_point, 6)


    # Timeviser
    hours = now.hour + minutes / 60
    angle = hours * 30 - 90

    end_x = start_point[0] + 80 * math.cos(math.radians(angle))
    end_y = start_point[1] + 80 * math.sin(math.radians(angle))

    end_point = (end_x, end_y)

    pygame.draw.line(screen, (0,0,0), start_point, end_point, 8)
# cirkel i midten
    pygame.draw.circle(screen, (0,0,0), start_point, 7)

    pygame.display.flip()

