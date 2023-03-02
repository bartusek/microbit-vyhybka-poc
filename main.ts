input.onButtonPressed(Button.A, function on_button_pressed_a() {
    Prehod_vyhybku()
})
input.onSound(DetectedSound.Loud, function on_sound_loud() {
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    strip.clear()
    strip.show()
})
function Prehod_vyhybku() {
    
    input.setSoundThreshold(SoundThreshold.Loud, 255)
    if (L4 == 0) {
        L4 = 1
        wuKong.setServoAngle(wuKong.ServoTypeList._270, wuKong.ServoList.S0, 90)
        strip.setPixelColor(1, neopixel.colors(NeoPixelColors.Red))
        strip.show()
        music.playSoundEffect(music.createSoundEffect(WaveShape.Sine, 5000, 0, 255, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), SoundExpressionPlayMode.UntilDone)
    } else {
        L4 = 0
        wuKong.setServoAngle(wuKong.ServoTypeList._270, wuKong.ServoList.S0, 180)
        strip.setPixelColor(1, neopixel.colors(NeoPixelColors.Green))
        strip.show()
        music.playSoundEffect(music.createSoundEffect(WaveShape.Sine, 1, 5000, 0, 255, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), SoundExpressionPlayMode.UntilDone)
    }
    
    basic.pause(500)
    input.setSoundThreshold(SoundThreshold.Loud, 181)
}

let strip : neopixel.Strip = null
let L4 = 0
L4 = 1
wuKong.setServoAngle(wuKong.ServoTypeList._270, wuKong.ServoList.S0, 90)
strip = neopixel.create(DigitalPin.P16, 4, NeoPixelMode.RGB)
input.setSoundThreshold(SoundThreshold.Loud, 187)
basic.forever(function on_forever() {
    
})
