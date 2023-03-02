def on_button_pressed_a():
    Prehod_vyhybku()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_sound_loud():
    pass
input.on_sound(DetectedSound.LOUD, on_sound_loud)

def on_button_pressed_b():
    strip.clear()
    strip.show()
input.on_button_pressed(Button.B, on_button_pressed_b)

def Prehod_vyhybku():
    global L4
    input.set_sound_threshold(SoundThreshold.LOUD, 255)
    if L4 == 0:
        L4 = 1
        wuKong.set_servo_angle(wuKong.ServoTypeList._270, wuKong.ServoList.S0, 90)
        strip.set_pixel_color(1, neopixel.colors(NeoPixelColors.RED))
        strip.show()
        music.play_sound_effect(music.create_sound_effect(WaveShape.SINE,
                5000,
                0,
                255,
                0,
                500,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LINEAR),
            SoundExpressionPlayMode.UNTIL_DONE)
    else:
        L4 = 0
        wuKong.set_servo_angle(wuKong.ServoTypeList._270, wuKong.ServoList.S0, 180)
        strip.set_pixel_color(1, neopixel.colors(NeoPixelColors.GREEN))
        strip.show()
        music.play_sound_effect(music.create_sound_effect(WaveShape.SINE,
                1,
                5000,
                0,
                255,
                500,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LINEAR),
            SoundExpressionPlayMode.UNTIL_DONE)
    basic.pause(500)
    input.set_sound_threshold(SoundThreshold.LOUD, 181)
strip: neopixel.Strip = None
L4 = 0
L4 = 1
wuKong.set_servo_angle(wuKong.ServoTypeList._270, wuKong.ServoList.S0, 90)
strip = neopixel.create(DigitalPin.P16, 4, NeoPixelMode.RGB)
input.set_sound_threshold(SoundThreshold.LOUD, 187)

def on_forever():
    pass
basic.forever(on_forever)
