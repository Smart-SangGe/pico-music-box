# pico-music-box

# 光敏八音盒

这是一个使用 Raspberry Pi Pico 控制的光敏八音盒项目。它能够根据环境亮度自动播放预定义的音乐曲目。

## 硬件要求

-   Raspberry Pi Pico
-   无源蜂鸣器
-   光敏电阻（光敏电阻引脚连接到 GPIO 26）
-   其他所需电路和连接线

## 依赖库

无需安装额外的依赖库，项目使用的是 MicroPython 内置的库。

## 安装和使用

1. 将项目代码复制到您的 Raspberry Pi Pico 开发环境中。

2. 将无源蜂鸣器连接到 GPIO 16 引脚。

3. 将光敏电阻连接到 GPIO 26 引脚。

4. 使用适当的方式将代码烧录到 Raspberry Pi Pico 上。

5. 启动 Raspberry Pi Pico，它会自动检测环境亮度并播放预定义的音乐曲目。

## 音乐曲目

项目代码中的 `song` 变量定义了预定义的音乐曲目。每个元素是一个元组，包含音符、播放时间和停顿时间。您可以根据需要自定义音乐曲目，添加或修改 `song` 列表中的元素。

## 自定义配置

-   若要调整环境亮度阈值，可以修改 `check_light_and_play()` 函数中的 `light_value > 4000` 部分。根据实际情况进行调整。

-   若要调整音符的频率和播放参数，可以修改 `notes` 字典中的音符频率和 `play_note()` 函数中的参数。

## 注意事项

-   确保正确连接硬件，并根据实际需求进行引脚映射和配置。

-   可能需要根据具体情况和硬件配置进行调整和优化。

-   请确保遵守适用的法律法规和使用条款。

## 贡献

欢迎贡献和改进该项目。如果您发现任何问题或有改进建议，请提交 issue 或 pull request。

## 许可证

该项目基于 [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html) 进行授权。

## 作者

编写和维护该项目的作者是 [SangGe](https://github.com/Smart-SangGe)。
