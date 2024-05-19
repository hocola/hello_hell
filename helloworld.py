import pygame

pygame.init() # 초기화

screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))


# 화면 타이틀 설정
pygame.display.set_caption("its me haha")

#FPS 설정
clock = pygame.time.Clock()

# bring up background images
background = pygame.image.load("C:/Users/asus/OneDrive/바탕 화면/PythonWork place/게임배경.png")

character = pygame.image.load("C:/Users/asus/OneDrive/바탕 화면/PythonWork place/게임캐릭터.png")
character_size = character.get_rect().size # 캐릭터 이미지 사이즈 구하기
character_width = character_size[0] # 캐릭터 가로 크기
character_height = character_size[1] # 캐릭터 세로 크기
# 캐릭터의 기준 좌표를 캐릭터의 왼쪽 상단으로 둔다.
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height  


# 캐릭터 이동 좌표
to_x = 0
to_y = 0

# 캐릭터 이동속도 변수
charcter_speed = 1


running = True
while running:
    dt = clock.tick(5) # 초당 프레임 수 fps 설정
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN: # 키보드와 키가 눌러졌을 경우
            if event.key == pygame.K_LEFT: #왼쪽 방향키가 눌렸을 때
                to_x -= charcter_speed
            elif event.key == pygame.K_RIGHT: #오른쪽 방향키가 눌렸을 때
                to_x += charcter_speed
            elif event.key == pygame.K_DOWN: #아래쪽 방향키가 눌렸을 때
                to_y += charcter_speed
            elif event.key == pygame.K_UP: #위쪽 방향키가 눌렸을 때
                to_y -= charcter_speed


        if event.type == pygame.KEYUP: #방향키를 뗐을 때 캐릭터 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0


    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    #왼쪽, 오른쪽 경계 정하기
    if character_x_pos < 0:
        character_x_pos = 0

    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    #위, 아래쪽 경계 정하기
    if character_y_pos < 0:
        character_y_pos = 0

    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height




    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update()        

# 추가된 부분
pygame.quit()