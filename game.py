import pygame 
import random
import time

pygame.init()

width, height = 800, 600
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Rock Paper Scissors")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

font = pygame.font.SysFont(None, 40)
large_font = pygame.font.SysFont(None, 60)

rock_img = pygame.image.load("rock.png")
paper_img = pygame.image.load("paper.png")
scissors_img = pygame.image.load("scissor.png")

img_size = (300, 300)
rock_img = pygame.transform.scale(rock_img, img_size)
paper_img = pygame.transform.scale(paper_img, img_size)
scissors_img = pygame.transform.scale(scissors_img, img_size)

def draw_text(text, font, color,  x, y):
    img = font.render(text, True, color)
    text_rect = img.get_rect(center=(x, y))
    window.blit(img, text_rect)

def draw_buttons(text, x, y,w,h,inactive_color, active_color):
    mouse = pygame.mouse.get_pos()
    
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(window, active_color, (x, y, w, h))
        
    else:
        pygame.draw.rect(window, inactive_color, (x, y, w, h))
    
    text_surf = font.render(text, True, BLACK)
    text_rect = text_surf.get_rect()
    text_rect.center = ((x + (w /2)),(y +( h/2)))
    window.blit(text_surf, text_rect)

    return x+w > mouse[0] > x and y + h > mouse[1] > y

def game_loop():
    player_choice = None
    computer_choice = None
    result = None
    player_score = 0
    computer_score = 0
    round_in_progress = False

    animation_image=[rock_img, paper_img, scissors_img]
    animation_index = 0
    last_animation_time = time.time()

    click_handled= False

    running = True
    while running:
        current_time = time.time()
        mouse_clicked = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_clicked = True    
        window.fill(WHITE)

        if not round_in_progress:
            if current_time - last_animation_time >=1:
                animation_index = (animation_index + 1) % 3
                last_animation_time = current_time

            animation_rect = animation_image[animation_index].get_rect(center=(width // 2, height // 2))
            window.blit(animation_image[animation_index], animation_rect)

            rock_hover = draw_buttons("Rock", 100, 450, 100, 50, BLUE, (255,100, 100))
            paper_hover = draw_buttons("Paper", 300, 450, 100, 50, BLUE, (255,100, 100))
            scissors_hover = draw_buttons("Scissors", 500, 450, 120, 50, BLUE,(255,100, 100))
            
            if  mouse_clicked and not click_handled:
                if rock_hover:
                    player_choice = "rock"
                    round_in_progress = True
                elif paper_hover:
                    player_choice = "paper"
                    round_in_progress = True
                elif scissors_hover:
                    player_choice = "scissors"
                    round_in_progress = True
                click_handled = True

                if round_in_progress:
                    computer_choice = random.choice(["rock", "paper", "scissors"])
                    click_handled = True

                    if player_choice == computer_choice:
                        result = "It's a tie!"
                    elif (player_choice == "rock" and computer_choice == "scissors") or \
                         (player_choice == "paper" and computer_choice == "rock") or \
                         (player_choice == "scissors" and computer_choice == "paper"):
                        result = "You win!"
                        player_score += 10
                    else:
                        result = "Computer wins!"
                        computer_score += 10
            
            if round_in_progress and computer_choice :
                
                player_img = rock_img if player_choice == "rock" else paper_img if player_choice == "paper" else scissors_img
                player_rect = player_img.get_rect(center=(200, height // 2))
                window.blit(player_img, player_rect)

                computer_img = rock_img if computer_choice == "rock" else paper_img if computer_choice == "paper" else scissors_img 
                computer_rect = computer_img.get_rect(center=(width -200, height // 2))
                window.blit(computer_img, computer_rect)

                draw_text(result, large_font, BLACK, width // 2, 100)

                next_round_hover = draw_buttons("Next Round", 300, 500, 200, 70, (200, 200, 200), (150, 150, 150))

                if next_round_hover and click_handled and mouse_clicked:
                    player_choice = None
                    computer_choice = None
                    result = None
                    round_in_progress = False
                    click_handled = False
                    
        draw_text(f"Player Score: {player_score}", font, BLACK, 150, 50)
        draw_text(f"Computer Score: {computer_score}", font, BLACK, 650, 50)

        pygame.display.update()

    if not mouse_clicked:
        click_handled = False

    pygame.quit()
game_loop()
