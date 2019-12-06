import pygame
import sys
import subprocess
from pygame.locals import *
import os
import RPi.GPIO as GPIO
import time

# os.putenv('SDL_VIDEODRIVER', 'fbcon')   # Display on piTFT
# os.putenv('SDL_FBDEV', '/dev/fb1')
# os.putenv('SDL_MOUSEDRV', 'TSLIB')     # Track mouse clicks on piTFT
# os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

leftq = [("stop1", "0"), ("stop2", "0"), ("stop3", "0")]
rightq = [("stop1", "0"), ("stop2", "0"), ("stop3", "0")]
start = time.time()

#Servo Configure
GPIO.setmode(GPIO.BCM)
#left
GPIO.setup(16, GPIO.OUT)
#right
GPIO.setup(13, GPIO.OUT)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pLeft = GPIO.PWM(16, 1000/21.5)
pLeft.start(100*1.5/21.5)
pRight = GPIO.PWM(13, 1000/21.5)
pRight.start(100*1.5/21.5)


#left stop
def GPIO17_callback(channel):
	# print("Left Stop")
	pLeft.stop()
	leftq.pop(0)
	leftq.append(("stop", str(int(time.time()-start))))
	print(leftq)
	screen.fill(BLACK)
	display("stop")
	# for i in range(3):
	# 	l_surface = my_font.render(leftq[i][0], True, WHITE)
	# 	rect = text_surface.get_rect(center = lpos[2-i])
	# 	lt_surface = my_font.render(leftq[i][1], True, WHITE)
	# 	rect_t = text_surface.get_rect(center = ltpos[2-i])
	# 	screen.blit(l_surface, rect)
	# 	screen.blit(lt_surface, rect_t)
	# pygame.display.flip()
#left clockwise
def GPIO22_callback(channel):
	# print("Left clock")

	pLeft.start(100*1.7/21.7)
	pLeft.ChangeFrequency(1000/21.7)
	leftq.pop(0)
	leftq.append(("clock", str(int(time.time()-start))))
	print(leftq)
	screen.fill(BLACK)
	display("stop")
	# screen.fill(BLACK)
	# for i in range(3):
	# 	l_surface = my_font.render(leftq[i][0], True, WHITE)
	# 	rect = text_surface.get_rect(center = lpos[2-i])
	# 	lt_surface = my_font.render(leftq[i][1], True, WHITE)
	# 	rect_t = text_surface.get_rect(center = ltpos[2-i])
	# 	screen.blit(l_surface, rect)
	# 	screen.blit(lt_surface, rect_t)
	# pygame.display.flip()

#left counter-clockwise
def GPIO23_callback(channel):
	# print("Left counter-clock")
	pLeft.start(100*1.3/21.3)
	pLeft.ChangeFrequency(1000/21.3)
	leftq.pop(0)
	leftq.append(("counter", str(int(time.time()-start))))
	print(leftq)
	screen.fill(BLACK)
	display("stop")
	# screen.fill(BLACK)
	# for i in range(3):
	# 	l_surface = my_font.render(leftq[i][0], True, WHITE)
	# 	rect = text_surface.get_rect(center = lpos[2-i])
	# 	lt_surface = my_font.render(leftq[i][1], True, WHITE)
	# 	rect_t = text_surface.get_rect(center = ltpos[2-i])
	# 	screen.blit(l_surface, rect)
	# 	screen.blit(lt_surface, rect_t)
	# pygame.display.flip()

#right stop
def GPIO27_callback(channel):
	# pRight.start(100*1.5/21.5)
	# pRight.ChangeFrequency(1000/21.5)
	pRight.stop()
	rightq.pop(0)
	rightq.append(("stop", str(int(time.time()-start))))
	print(rightq)
	screen.fill(BLACK)
	display("stop")
#right clockwise
def GPIO19_callback(channel):
	pRight.start(100*1.7/21.7)
	pRight.ChangeFrequency(1000/21.7)
	rightq.pop(0)
	rightq.append(("clock", str(int(time.time()-start))))
	print(rightq)
	screen.fill(BLACK)
	display("stop")

#right counter-clockwise
def GPIO26_callback(channel):
	pRight.start(100*1.3/21.3)
	pRight.ChangeFrequency(1000/21.3)
	rightq.pop(0)
	rightq.append(("counter", str(int(time.time()-start))))
	print(rightq)
	screen.fill(BLACK)
	display("stop")

GPIO.add_event_detect(17, GPIO.FALLING, callback=GPIO17_callback, bouncetime = 300)
GPIO.add_event_detect(22, GPIO.FALLING, callback=GPIO22_callback, bouncetime = 300)
GPIO.add_event_detect(23, GPIO.FALLING, callback=GPIO23_callback, bouncetime = 300)
GPIO.add_event_detect(27, GPIO.FALLING, callback=GPIO27_callback, bouncetime = 300)
GPIO.add_event_detect(19, GPIO.FALLING, callback=GPIO19_callback, bouncetime = 300)
GPIO.add_event_detect(26, GPIO.FALLING, callback=GPIO26_callback, bouncetime = 300)










pygame.init()
pygame.mouse.set_visible(True)
WHITE = 255, 255, 255
BLACK = 0,0,0
screen = pygame.display.set_mode((320, 240))

my_font= pygame.font.Font(None, 20)
my_buttons= { 'stop':(140,120), 'quit':(240, 220), 'left history':(80,40), 'right history':(240, 40)}
new_buttons= { 'resume':(140,120), 'quit':(240, 220), 'left history':(80,40), 'right history':(240, 40)}
# q_buttons = { 'stop':(180,120), 'quit':(240, 180), 'left history':(80,40)}

screen.fill(BLACK)
rectList = []
surfaceList = []
newRect = []
newSurf = []

lpos = {0:(40,80), 1:(40,120), 2:(40,160)}
rpos = {0:(200,80), 1:(200,120), 2:(200,160)}
ltpos = {0:(100,80), 1:(100,120), 2:(100,160)}
rtpos = {0:(260,80), 1:(260,120), 2:(260,160)}

def display(state):
	if state == "stop":
		pygame.draw.circle(screen, pygame.Color(255,0,0), (140,120),25,0)
		for my_text, text_pos in my_buttons.items():
			text_surface = my_font.render(my_text, True, WHITE)
			rect = text_surface.get_rect(center = text_pos)
			surfaceList.append(text_surface)
			rectList.append(rect)
			screen.blit(text_surface, rect)

	elif state == "resume":
		pygame.draw.circle(screen, pygame.Color(0,255,0), (140,120),25,0)
		for my_text, text_pos in new_buttons.items():    
			text_surface = my_font.render(my_text, True, WHITE)
			rect = text_surface.get_rect(center = text_pos)
			newSurf.append(text_surface)
			newRect.append(rect)
			screen.blit(text_surface, rect)


	for i in range(3):
		l_surface = my_font.render(leftq[i][0], True, WHITE)
		rect = text_surface.get_rect(center = lpos[2-i])
		lt_surface = my_font.render(leftq[i][1], True, WHITE)
		rect_t = text_surface.get_rect(center = ltpos[2-i])
		screen.blit(l_surface, rect)
		screen.blit(lt_surface, rect_t)

	for i in range(3):
		r_surface = my_font.render(rightq[i][0], True, WHITE)
		rect = text_surface.get_rect(center = rpos[2-i])
		rt_surface = my_font.render(rightq[i][1], True, WHITE)
		rect_t = text_surface.get_rect(center = rtpos[2-i])
		screen.blit(r_surface, rect)
		screen.blit(rt_surface, rect_t)



	pygame.display.flip()

def quit():
	global code_run
	code_run = False

display("stop")
code_run = True
while code_run:
	#set sleep time to avoid start-up latency
	time.sleep(0.005)
	x = -1
	y = -1
	for event in pygame.event.get():
		if event.type is MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
		elif event.type is MOUSEBUTTONUP:
			pos = pygame.mouse.get_pos()
			x, y = pos

	if (y > 120 and x > 160) :
			print("Quit pressed")
			start_flag = False
			quit()
	elif 120 < x < 160 and 100 < y < 140:
		pLeft.stop()
		pRight.stop()
		screen.fill(BLACK)
		display("resume")








