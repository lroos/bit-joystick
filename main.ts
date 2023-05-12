joystickbit.onButtonEvent(joystickbit.JoystickBitPin.P14, joystickbit.ButtonType.down, function () {
    radio.sendValue("button_e", 1)
    music.playSoundEffect(music.createSoundEffect(WaveShape.Triangle, 300, 200, 255, 0, 75, SoundExpressionEffect.None, InterpolationCurve.Curve), SoundExpressionPlayMode.UntilDone)
})
joystickbit.onButtonEvent(joystickbit.JoystickBitPin.P15, joystickbit.ButtonType.down, function () {
    radio.sendValue("button_f", 1)
    music.playSoundEffect(music.createSoundEffect(WaveShape.Sine, 200, 600, 255, 0, 150, SoundExpressionEffect.None, InterpolationCurve.Linear), SoundExpressionPlayMode.UntilDone)
})
joystickbit.onButtonEvent(joystickbit.JoystickBitPin.P13, joystickbit.ButtonType.down, function () {
    radio.sendValue("button_d", 1)
    music.playSoundEffect(music.createSoundEffect(WaveShape.Sine, 762, 787, 198, 0, 124, SoundExpressionEffect.None, InterpolationCurve.Curve), SoundExpressionPlayMode.UntilDone)
})
joystickbit.onButtonEvent(joystickbit.JoystickBitPin.P12, joystickbit.ButtonType.down, function () {
    radio.sendValue("button_c", 1)
    music.playSoundEffect(music.createSoundEffect(WaveShape.Triangle, 351, 433, 179, 0, 213, SoundExpressionEffect.None, InterpolationCurve.Curve), SoundExpressionPlayMode.UntilDone)
})
let ry = 0
let rx = 0
joystickbit.initJoystickBit()
let x = joystickbit.getRockerValue(joystickbit.rockerType.X)
let y = joystickbit.getRockerValue(joystickbit.rockerType.Y)
music.setVolume(132)
music.playSoundEffect(music.builtinSoundEffect(soundExpression.spring), SoundExpressionPlayMode.InBackground)
let led2 = game.createSprite(2, 2)
serial.redirectToUSB()
basic.forever(function () {
    rx = Math.map(joystickbit.getRockerValue(joystickbit.rockerType.X), 0, 1100, 0, 4)
    if (x != rx) {
        x = rx
        radio.sendValue("x", 2 - x)
        led2.set(LedSpriteProperty.X, 4 - x)
    }
    ry = Math.map(joystickbit.getRockerValue(joystickbit.rockerType.Y), 0, 1100, 0, 4)
    if (y != ry) {
        y = ry
        radio.sendValue("y", 2 - y)
        led2.set(LedSpriteProperty.Y, 4 - y)
    }
})
