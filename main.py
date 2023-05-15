from machine import Pin, PWM, ADC
import utime

# 定义音符和频率
notes = {
    'c': 261,
    'd': 294,
    'e': 329,
    'f': 349,
    'g': 392,
    'a': 440,
    'b': 494,
    'C': 523,
    'D': 587,
    'E': 659,
    'F': 698,
    'G': 784,
    'A': 880,
    'B': 988
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

# 光敏电阻引脚
ldr = ADC(Pin(26))

# 通过PWM播放音符
def play_note(note, play_time, pause_time):
    buzzer.freq(notes[note])
    buzzer.duty_u16(2000) # 响度
    utime.sleep(play_time)
    buzzer.duty_u16(0)
    utime.sleep(pause_time)

# 检查环境亮度并播放音乐
def check_light_and_play():
    while True:
        light_value = ldr.read_u16()
        print(light_value)
        utime.sleep(2)
        if light_value > 4000:  # 环境亮度阈值可以根据实际情况调整
            for note, play_time, pause_time in song:
                play_note(note, play_time, pause_time)

# 主程序
if __name__ == '__main__':
    check_light_and_play()
