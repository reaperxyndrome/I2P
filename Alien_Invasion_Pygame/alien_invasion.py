from pygame import *
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
	init()
	ai_settings = Settings()
	screen = display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	display.set_caption("Alien Invasion")
	icon = image.load("images/ship.bmp")
	display.set_icon(icon)
	ship = Ship(ai_settings, screen)
	bullets = Group()
	while True:
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(bullets)
		gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
