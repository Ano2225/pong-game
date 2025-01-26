import pygame, sys, random

def ball_animation():
     global ball_speed_x, ball_speed_y
     ball.x += ball_speed_x
     ball.y += ball_speed_y
     
     #handle collisions
     if ball.top <= 0 or ball.bottom >= screen_height:
         ball_speed_y *= -1
     if ball.left <= 0 or ball.right >= screen_width:
        ball_restart()
         
     if ball.colliderect(player) or ball.colliderect(opponent):
         ball_speed_x *= -1

def player_animation():
     player.y += player_speed
     if player.top <= 0:
         player.top = 0
     if player.bottom >= screen_height:
         player.bottom = screen_height

def opponent_ai():
    if opponent.top < ball.y:
         opponent.top += opponent_speed
    if opponent.bottom > ball.y:
         opponent.bottom -= opponent_speed
    if opponent.top <= 0:
         opponent.top = 0
    if opponent.bottom >= screen_height:
         opponent.bottom = screen_height 

def ball_restart():
    global ball_speed_x, ball_speed_y, player_score, opponent_score
    
    #Determine who scored 
    if ball.left <= 0:
        player_score += 1
    elif ball.right >= screen_width:
        opponent_score += 1
    
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))
 
             
#General setup
pygame.init()
clock = pygame.time.Clock()

#setting up the main window
screen_width = 1280
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# Game Rectangle
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15,30,30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70,10,140)
opponent = pygame.Rect(10, screen_height/2 - 70,10,140)

#colors
bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

#speed variables
ball_speed_y = 7
ball_speed_x = 7
player_speed = 0
opponent_speed = 7

#score variable
player_score = 0
opponent_score = 0

font = pygame.font.Font(None, 36)

while True:
     #Handling input
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             pygame.quit()
             sys.exit()
         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_DOWN:
                 player_speed += 7
             if event.key == pygame.K_UP:
                 player_speed -= 7
         if event.type == pygame.KEYUP:
             if event.key == pygame.K_DOWN:
                 player_speed -= 7
             if event.key == pygame.K_UP:
                 player_speed += 7
    
     ball_animation()
     player_animation()
     opponent_ai()
    
         
     #Visuals
     screen.fill(bg_color)
     pygame.draw.rect(screen, light_grey, player)
     pygame.draw.rect(screen, light_grey, opponent)
     pygame.draw.ellipse(screen, light_grey, ball)
     pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2,screen_height))
     
     score_text = font.render('Score', True, light_grey)
     score_text_rect = score_text.get_rect(center=(screen_width/2, 20))
     
     score_surface = font.render(f'{opponent_score}  {player_score}',True, light_grey)
     score_rect = score_surface.get_rect(center=(screen_width/2, 50))
     screen.blit(score_surface, score_rect)
     screen.blit(score_text, score_text_rect)
    
     #updating the window
     pygame.display.flip()
     clock.tick(60)