import pygame
import cv2

capture = cv2.VideoCapture(0)
success, camera_image = capture.read()

window = pygame.display.set_mode(camera_image.shape[1::-1])
clock = pygame.time.Clock()

run = success
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    success, camera_image = capture.read()
    if success:
        camera_surf = pygame.image.frombuffer(
            camera_image.tobytes(), camera_image.shape[1::-1], "BGR")
    else:
        run = False
    window.blit(camera_surf, (0, 0))
    pygame.display.flip()

pygame.quit()
exit()