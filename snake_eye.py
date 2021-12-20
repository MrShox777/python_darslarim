#bismilahi rohmani rohim 
#<data:04.12.2021.>
import pygame

pygame.init()
width = 640
height = 480

display = pygame.display.set_mode((640, 480))
#pygame.display.undate()
pygame.display.set_caption("Snakee game by Howdy")

game_end = False 

colors={ 
	"Snake_head":(0,255,0),
	"Snake_tail":(0,200,0),
	"apple": (255,0,0)
}
snake_pos = {
	"x":640/2-5,
	"y":480/2-5,
	"x_change":0,
	"y_change":0
}

snake_size=(10,10)

snake_speed = 10

while not game_end:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_end = True

		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:

				snake_pos["x_change"] = -10

			elif event.key == pygame.K_RIGHT:

				snake_pos["x_change"] =snake_speed 
				snake_pos["y_changa"] = 0

			elif event.key == pygame.K_UP:

				snake_pos["x_change"] = 0
				snake_pos["y_changa"] = -snake_speed

            #elif event.key == pygame.K_DOWN:

                #snake_pos["x_change"] = 0
                #snake_pos["y_changa"] = snake_speed
    #display.fill((0,0,0))

    #snake_pos["x"] += snake_pos["x_change"];	 
    #snake_pos["y"] += snake_pos["y_change"];	 
    
   # pygame.draw.rect(display, colors["snake_head"],[
    #	snake_pos["x"],
    #	snake_pos["y"],
    #	snake_size[0],
    #	snake_size[1]])

    #pygame.display.undate()


pygame.quit()
quit()