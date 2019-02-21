import pygame

pygame.init()
win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
score=0
font = pygame.font.SysFont('comicsans', 30, True)


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
		self.eat=False
				
	
	
	def draw(self,win,color):
		pygame.draw.circle(win,color,(self.x,self.y),self.radius,0)
		pygame.draw.rect(win,(0,255,0),(self.x-self.radius,self.y-self.radius,2*self.radius,2*self.radius),1)


class eatblock(object):
	def __init__(self,x,y,radius):
		self.x=x
		self.y=y
		self.radius=radius
		self.width=2*radius
		self.heigth=2*radius
		self.hitbox=[self.x,self.y,self.radius,self.radius]
		self.velx=0
		self.vely=0
		
	def draw(self,win):
		pygame.draw.circle(win,(255,0,0),(self.x,self.y),self.radius,1)
		pygame.draw.rect(win,(0,255,0),(self.x-self.radius,self.y-self.radius,2*self.radius,2*self.radius),1)






run=True


def redrawwindow(win):
	win.fill((0,0,0))
	
	j=0
	color=(255,0,0)
	for block in snake:
		if j==len(snake)-1:
			color=(0,0,255)
		j+=1
		block.draw(win,color)
		#~ print j
		#~ print j,',',block.x,',',block.y
	food.draw(win)
	text =font.render('Score: ' + str(score), 1, (0,0,255))
	win.blit(text, (390, 10))
	pygame.display.update()


def crawl():
	
	head=snake[0]
	for i in range(1,len(snake)):
		snake[i].x=snake[i-1].x
		snake[i].y=snake[i-1].y
		snake[i].velx=snake[i-1].velx
		snake[i].vely=snake[i-1].vely
		snake[i].hitbox[0]=snake[i-1].hitbox[0]
		snake[i].hitbox[1]=snake[i-1].hitbox[1]

		
	if keys[pygame.K_LEFT] and snake[0].x>velx:
		snake[0].velx =-velx
		snake[0].vely=0
		snake[0].x+=snake[0].velx
		snake[0].hitbox[0]+=snake[0].velx
	elif keys[pygame.K_RIGHT] and snake[0].x < 500 - snake[0].width - velx:       
		snake[0].velx =velx
		snake[0].vely=0
		snake[0].x+=snake[0].velx
		snake[0].hitbox[0]+=snake[0].velx
	elif keys[pygame.K_DOWN] and snake[0].y>vely:     
		snake[0].velx =0
		snake[0].vely=vely
		snake[0].y+=snake[0].vely
		snake[0].hitbox[1]+=snake[0].vely
	#~ elif keys[pygame.K_UP] and snake[0].y > 500 - snake[0].heigth - vely:       
	elif keys[pygame.K_UP]:
		snake[0].velx =0
		snake[0].vely=-vely
		snake[0].y+=snake[0].vely
		snake[0].hitbox[1]+=snake[0].vely
	else:
		snake[0].x+=snake[0].velx
		snake[0].y+=snake[0].vely
		snake[0].hitbox[0]+=snake[0].velx
		snake[0].hitbox[1]+=snake[0].vely


block1=snakeblock(100,100,10)
food=eatblock(400,400,10)
#~ snake=[block(100,100,10)]

velx=20
vely=20

snake=[snakeblock(100,100,10),snakeblock(80,100,10)]


while run:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False
	clock.tick(10)
	keys=pygame.key.get_pressed()
	crawl()

	head=snake[0]
	#~ print len(snake)
	if head.hitbox[1] < food.hitbox[1] + food.hitbox[3] and head.hitbox[1] + head.hitbox[3] > food.hitbox[1]:
		if head.hitbox[0] + head.hitbox[2] > food.hitbox[0] and head.hitbox[0] < food.hitbox[0] + food.hitbox[2]:
			score += 1
			tail=snake[len(snake)-1]
			dx=0
			dy=0
	
			if tail.velx>0:
				dx=-20
			if tail.velx<0:
				dx=+20
			if tail.vely>0:
				dy=-20
			if tail.vely<0: 
				dy=20
			print tail.x,',',tail.y
			#~ newtail=snakeblock(tail.x+dx,tail.y+dy,10)
			newtail=snakeblock(20,20,10)
			print newtail.x,',',newtail.y
			snake.append(newtail)
			print len(snake)
	
	redrawwindow(win)








	

		


pygame.quit()

		
	
	

