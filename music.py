from machine import Pin, PWM, ADC
import utime

# 定义音符和频率
notes = {
    'c': 261,# 1
    'd': 294,# 2
    'e': 329,# 3
    'f': 349,# 4 
    'g': 392,# 5
    'a': 440,# 6
    'b': 494,# 7
    'C': 523,# ·1
    'D': 587,# ·2
    'E': 659,# ·3
    'F': 698,# ·4
    'G': 784,# ·5
    'A': 880,# ·6
    'B': 988 # ·7
}

# 歌曲序列，每个元素是一个元组，包含音符、播放时间和停顿时间
song = [
    # 祝你生日快乐
    ('g', 0.5, 0.05),
    ('g', 0.5, 0.1),
    ('a', 0.5, 0.1),
    ('g', 0.5, 0.1),
    ('C', 0.5, 0.1),
    ('b', 1, 0.1),
    
    # 祝你生日快乐
    ('g', 0.5, 0.05),
    ('g', 0.5, 0.1),
    ('a', 0.5, 0.1),
    ('g', 0.5, 0.1),
    ('D', 0.5, 0.1),
    ('C', 1, 0.1),
    
    # 祝你生日快乐
    ('g', 0.5, 0.05),
    ('g', 0.5, 0.1),
    ('G', 0.5, 0.1),
    ('E', 0.5, 0.1),
    ('C', 0.5, 0.1),
    ('b', 0.5, 0.1),
    ('a', 0.5, 0.1),
    ('a', 1, 0.1),
    
    # 祝你生日快乐
    ('F', 0.5, 0.05),
    ('F', 0.5, 0.1),
    ('E', 0.5, 0.1),
    ('C', 0.5, 0.1),
    ('D', 0.5, 0.1),
    ('C', 1.5, 0.1)
]

# 无源蜂鸣器引脚
buzzer = PWM(Pin(16))

# 通过PWM播放音符
def play_note(note, play_time, pause_time):
    buzzer.freq(notes[note])
    buzzer.duty_u16(1000)
    utime.sleep(play_time)
    buzzer.duty_u16(0)
    utime.sleep(pause_time)

# 主程序
if __name__ == '__main__':
    for note, play_time, pause_time in song:
        play_note(note, play_time, pause_time)
    

