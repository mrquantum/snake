import pygame
import numpy as np
from random import randint

pygame.init()
screensize=500
win = pygame.display.set_mode((screensize,screensize))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
score=0
font = pygame.font.SysFont('comicsans', 30, True)

vel=20
velx=20
vely=20

class snakeblock(object):
	def __init__(self,x,y,radius):
		self.x=x
		self.y=y
		self.radius=radius
		self.width=2*radius
		self.heigth=2*radius
		self.hitbox=[self.x,self.y,self.radius,self.radius]
		self.velx=0
		self.vely=0
		#~ self.collided=False
	
	def collide(self,other):
		if self.hitbox[1] < other.hitbox[1] + other.hitbox[3] and self.hitbox[1] + self.hitbox[3] > other.hitbox[1]:
			if self.hitbox[0] + self.hitbox[2] > other.hitbox[0] and self.hitbox[0] < other.hitbox[0] + other.hitbox[2]:
				return True
	
	def teleport(self):
		#teleports the block to a random pos
		self.x=randint(2,screensize//vel-2)*vel
		self.hitbox[0]=food.x
		self.y=randint(2,screensize//vel-2)*vel
		self.hitbox[1]=food.y
	
	
	
	def drawblock(self,win,color,shape='circle',hitbox=False):
	
		if shape=='polygon':
			noangle=6
			points=[]
			for i in range(0,noangle):
				points.append((self.x+self.radius*np.cos(2*np.pi*i/noangle),self.y+self.radius*np.sin(2*np.pi*i/noangle)))
			pygame.draw.polygon(win, (255,0,0),tuple(points))
		#~ print points
		elif shape=='rect':
			pygame.draw.rect(win,color,(self.x-self.radius,self.y-self.radius,2*self.radius,2*self.radius),0)
		elif shape=='circle':
			pygame.draw.circle(win,color,(self.x,self.y),self.radius,0)
		elif shape=='triangle':
			offset=0
			if self.vely>0:
				offset=-np.pi/2
			elif self.vely<0:
				offset=np.pi/2
			elif self.velx<0:
				offset=0
			elif self.velx>0:
				offset=np.pi
			else:
				offset=0
			noangle=3
			points=[]
			for i in range(0,noangle):
				points.append((self.x+self.radius*np.cos(2*np.pi*i/noangle+offset),self.y+self.radius*np.sin(2*np.pi*i/noangle+offset)))
			pygame.draw.polygon(win, (255,0,0),tuple(points))
		
		if hitbox:
			pygame.draw.rect(win,(0,255,0),(self.x-self.radius,self.y-self.radius,2*self.radius,2*self.radius),1)
		


class snake(snakeblock):
	def __init__(self,snakeblock):
		self.Snake=[]
		self.Snake.append(snakeblock)
		self.headvelx=0
		self.headvely=0
		self.initx=100
		self.inity=100
		
	def getdirection(self):
		keys=pygame.key.get_pressed()
		if keys[pygame.K_LEFT] and self.Snake[0].velx!=20:
			self.Snake[0].velx=-20
			self.Snake[0].vely=0
		elif keys[pygame.K_RIGHT] and self.Snake[0].velx!=-20:
			self.Snake[0].velx=20
			self.Snake[0].vely=0
		elif keys[pygame.K_UP] and self.Snake[0].vely!=20:
			self.Snake[0].velx=0
			self.Snake[0].vely=-20
		elif keys[pygame.K_DOWN] and self.Snake[0].vely!=-20:
			self.Snake[0].velx=0
			self.Snake[0].vely=20
	
	def crawl(self):
		#update every pos except the head
		if len(self.Snake)>1:
			for i in range(len(self.Snake)-1,0,-1):
				self.Snake[i].x=self.Snake[i-1].x
				self.Snake[i].y=self.Snake[i-1].y
				self.Snake[i].velx=self.Snake[i-1].velx
				self.Snake[i].vely=self.Snake[i-1].vely
				self.Snake[i].hitbox=self.Snake[i-1].hitbox
		
		#update the head
		self.Snake[0].x+=self.Snake[0].velx
		self.Snake[0].y+=self.Snake[0].vely
		self.Snake[0].hitbox[0]+=self.Snake[0].velx
		self.Snake[0].hitbox[1]+=self.Snake[0].vely


	def eat(self):
		#elongates the snake
		x0=self.Snake[len(self.Snake)-1].x
		y0=self.Snake[len(self.Snake)-1].y
		velx0=self.Snake[len(self.Snake)-1].velx
		vely0=self.Snake[len(self.Snake)-1].vely
		dx=0
		dy=0
		if velx0==0:
			if vely0>0:
				dy=-10
			elif vely<0:
				dy=10
		elif vely==0:
			if velx0>0:
				dx=-10
			elif vely<0:
				dx=10
		self.Snake.append(snakeblock(x0+dx,y0+dy,8))
		self.Snake[len(self.Snake)-1].hitbox[2]=8
		self.Snake[len(self.Snake)-1].hitbox[3]=8
	def reset(self):
		self.Snake=[]
		self.Snake.append(snakeblock(self.initx,self.inity,10))
	
	def draw(self,win):
		color=(255,0,0)
		self.Snake[0].drawblock(win,color,shape='polygon')
		
		if len(self.Snake)>2:
			for i in range(1,len(self.Snake)-1):
				block=self.Snake[i]
				block.drawblock(win,color)
		if len(self.Snake)>1:
			block=self.Snake[len(self.Snake)-1]
			block.drawblock(win,color,shape='triangle')
			
class obstacle(snakeblock):
	
	def __init__(self,snakeblock):
		self.color=(0,0,255)
		self.wall=[]
		self.wall.append(snakeblock)
		
	def draw(self,win,rect=True):
		for block in self.wall:
			block.drawblock(win,self.color,shape='rect')
			
		
		

def redrawwindow(win):
	win.fill((0,0,0))
	

	reptile.draw(win)
	Wall.draw(win)
	food.drawblock(win,(255,255,0))
	text =font.render('Score: ' + str(score), 1, (255,0,255))
	win.blit(text, (370, 30))

	pygame.display.update()



food=snakeblock(100,300,10)

#make wall
Wall=obstacle(snakeblock(0,0,20))
for xy in range(0,520,20):
	Wall.wall.append(snakeblock(xy,0,20))
	Wall.wall.append(snakeblock(0,xy,20))
	Wall.wall.append(snakeblock(xy,screensize,20))
	Wall.wall.append(snakeblock(screensize,xy,20))


run=True

head=snakeblock(100,100,10)
reptile=snake(head)
while run:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False
	clock.tick(10)
	
	

	reptile.getdirection()
	reptile.crawl()

	#check for food-collision
	if reptile.Snake[0].collide(food):
		score+=1
		reptile.eat()
		
		snakecoll=True #true to emulate a do-while loop in python
		wallcoll=True
		while snakecoll==True or wallcoll==True:
			snakecoll=False #set control variables
			wallcoll=False 
			food.teleport() #actually places the food at different pos
			for block in reptile.Snake:
				if food.collide(block):
					snakecoll=True
					break
			for block in Wall.wall:
				if food.collide(block):
					wallcoll=True
					break
				
		


	for block in Wall.wall:
		if reptile.Snake[0].collide(block):
			reptile.reset()
			score=0	
		
	#check for self-collision
	#~ if len(reptile.Snake)>3:
		#~ for j in range(2,len(reptile.Snake)-1):
			#~ if reptile.Snake[0].collide(reptile.Snake[j]):
				#~ print "yes"
				#~ reptile.reset()
				#~ score=0


	redrawwindow(win)

	



		


pygame.quit()

		
	
	
