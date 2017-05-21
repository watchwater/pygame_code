#-*- coding:utf-8 -*-
import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()
screen=pygame.display.set_mode((640,480),0,32)

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
	
	rand_col=(randint(0,255),randint(0,255),randint(0,255))
	#实现随机产生一个色调
	
	#screen.lock()  注意这个会有一个隐含的锁住功能
	for _ in xrange(100):
		rand_pos = (randint(0,639),randint(0,479))
		screen.set_at(rand_pos,rand_col)
	#screen.unlock() 注意这儿有一个隐含的解锁功能
	
	pygame.display.update()