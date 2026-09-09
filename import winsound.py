import winsound

# 주파수(Frequency)와 재생 시간(Duration, 밀리초)을 설정하여 소리를 냅니다.
def play_sound():
    winsound.Beep(1000, 500)  # 1000Hz의 소리를 0.5초(500ms) 동안 재생

print("앗! 함정을 밟았습니다!")
play_sound()