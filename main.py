import pygame
import os

pygame.init()

# Set the width and height of the screen
screen_width, screen_height = 600, 100
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the caption of the screen
pygame.display.set_caption("Music Player")

# Set the font and font size
font = pygame.font.Font(None, 36)

# Set the directory path for music files
music_dir = "D:/Music"

# Get the list of music files in the directory
music_files = os.listdir(music_dir)

# Create a list of playable music files
music_list = []
for file in music_files:
    if file.endswith(".mp3") or file.endswith(".wav"):
        music_list.append(os.path.join(music_dir, file))

# Initialize the pygame mixer module
pygame.mixer.init()


# Create a function to play music
def play_music(music_file):
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()


# Set the initial song to play
current_song_index = 0
current_song = music_list[current_song_index]
play_music(current_song)

# Create buttons
button_width, button_height = 100, 50
play_button_rect = pygame.Rect(50, 50, button_width, button_height)
stop_button_rect = pygame.Rect(200, 50, button_width, button_height)
next_button_rect = pygame.Rect(350, 50, button_width, button_height)

# Create a loop to handle events
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            # Stop the current song if the spacebar is pressed
            if event.key == pygame.K_SPACE:
                pygame.mixer.music.stop()
            # Play the next song if the right arrow key is pressed
            elif event.key == pygame.K_RIGHT:
                current_song_index = (current_song_index + 1) % len(music_list)
                current_song = music_list[current_song_index]
                play_music(current_song)
            # Play the previous song if the left arrow key is pressed
            elif event.key == pygame.K_LEFT:
                current_song_index = (current_song_index - 1) % len(music_list)
                current_song = music_list[current_song_index]
                play_music(current_song)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Stop the current song if the stop button is clicked
            if stop_button_rect.collidepoint(event.pos):
                pygame.mixer.music.stop()
            # Play the current song if the play button is clicked
            elif play_button_rect.collidepoint(event.pos):
                play_music(current_song)
            # Play the next song if the next button is clicked
            elif next_button_rect.collidepoint(event.pos):
                current_song_index = (current_song_index + 1) % len(music_list)
                current_song = music_list[current_song_index]
                play_music(current_song)

    # Clear the screen
    screen.fill((255, 255, 255))

    # Render the buttons
    pygame.draw.rect(screen, (0, 255, 0), play_button_rect)
    pygame.draw.rect(screen, (255, 0, 0), stop_button_rect)
    pygame.draw.rect(screen, (0, 0, 255), next_button_rect)

    # Render the button labels
    play_label = font.render("Play", True, (0, 0, 0))
    stop_label = font.render("Stop", True, (0, 0, 0))
    next_label = font.render("Next", True, (255, 255, 255))
    screen.blit(play_label, (play_button_rect.centerx - play_label.get_width() // 2, play_button_rect.centery - play_label.get_height() // 2))
    screen.blit(stop_label, (stop_button_rect.centerx - stop_label.get_width() // 2, stop_button_rect.centery - stop_label.get_height() // 2))
    screen.blit(next_label, (next_button_rect.centerx - next_label.get_width() // 2, next_button_rect.centery - next_label.get_height() // 2))

    # Render the name of the current song
    song_label = font.render(os.path.basename(current_song), True, (0, 0, 0))
    screen.blit(song_label, (screen_width // 2 - song_label.get_width() // 2, 10))

    # Update the display
    pygame.display.update()

    # Wait for a short period of time to avoid using too much CPU
    pygame.time.wait(10)

