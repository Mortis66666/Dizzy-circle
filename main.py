import pygame
import time

WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dizzy circle")


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def draw(circles):
	win.fill(BLACK)

	for radius in circles:
		pygame.draw.circle(win, WHITE, (WIDTH/2, HEIGHT/2), radius, 10)

	pygame.display.update()


def main():
	run = True
	clock = pygame.time.Clock()
	FPS = 60
	circles = []
	last_update = 0

	while run:
		clock.tick(FPS)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		draw(circles)

		remv = []
		for i, radius in enumerate(circles):
			if radius > WIDTH/2+300:
				remv.append(radius)
				continue
			circles[i] = radius + 2

		for r in remv:
			circles.remove(r)

		now = time.time()

		if now - last_update > 0.5:
			circles.append(1)
			last_update = now


	pygame.quit()

if __name__ == "__main__":
	main()