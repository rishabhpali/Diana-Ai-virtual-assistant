import os
import pygame
def speak(text):
    voice = 'en-GB-SoniaNeural'
    chunks = text.split()
    chunk_size = 100
    chunks = [chunks[i:i + chunk_size]for i in range(0,len(chunks),chunk_size)]
    
    for chunk in chunks:
        text = ' '.join(chunk)
        data = f'python -m edge_tts --voice "{voice}" --text "{text}" --write-media "data.mp3"'
        os.system(data)
        
        
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("data.mp3")
        
        try:
            pygame.mixer.music.play()
            
            while pygame.mixer.music.get_busy():
             pygame.time.Clock().tick(10)
        
        except Exception as e:
            print(e)
        finally:
         pygame.mixer.music.stop()
         pygame.mixer.quit()
        
    return True
        