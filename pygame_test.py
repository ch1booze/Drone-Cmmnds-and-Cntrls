
import pygame_test

pygame_test.joystick.init()

joysticks = [pygame_test.joystick.Joystick(x) for x in range(pygame_test.joystick.get_count())]
print(joysticks)