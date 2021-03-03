from gtts import gTTS
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    print('Google text-to-speech')
    text = input("Input: ")
    clear()
    tts = gTTS(text=text, lang="en")
    count = 1
    while True:
        try:
            tts.save("gtts.mp3")
            break
        except:
            clear()
            if count == 1:
                print('Recieved a connection error.')
                count += 1
            else:
                print('Recieved a connection error ' + str(count) + ' times.')
                count += 1
    print(f'''Saved "{text}" as text-to-speach to gtts.mp3''')

if __name__ == '__main__':
    clear()
    main()