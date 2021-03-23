from pygame import mixer
print('{:.^40}'.format('EX021'))
mixer.init()
mixer.music.load("D:\mp3\osbaroesdapisadinharemixlofi.mp3")  # Music file can only be MP3
mixer.music.play()
# Then start a infinite loop
while True:
    print("")
