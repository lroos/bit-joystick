def my_function():
    radio.send_value("button_e", 1)
    music.play_sound_effect(music.create_sound_effect(WaveShape.TRIANGLE,
            300,
            200,
            255,
            0,
            75,
            SoundExpressionEffect.NONE,
            InterpolationCurve.CURVE),
        SoundExpressionPlayMode.IN_BACKGROUND)
joystickbit.on_button_event(joystickbit.JoystickBitPin.P14,
    joystickbit.ButtonType.DOWN,
    my_function)

def my_function2():
    radio.send_value("button_f", 1)
    music.play_sound_effect(music.create_sound_effect(WaveShape.SINE,
            200,
            600,
            255,
            0,
            150,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        SoundExpressionPlayMode.IN_BACKGROUND)
joystickbit.on_button_event(joystickbit.JoystickBitPin.P15,
    joystickbit.ButtonType.DOWN,
    my_function2)

def my_function3():
    radio.send_value("button_d", 1)
    music.play_sound_effect(music.create_sound_effect(WaveShape.SINE,
            762,
            787,
            198,
            0,
            124,
            SoundExpressionEffect.NONE,
            InterpolationCurve.CURVE),
        SoundExpressionPlayMode.IN_BACKGROUND)
joystickbit.on_button_event(joystickbit.JoystickBitPin.P13,
    joystickbit.ButtonType.DOWN,
    my_function3)

def my_function4():
    radio.send_value("button_c", 1)
    music.play_sound_effect(music.create_sound_effect(WaveShape.TRIANGLE,
            351,
            433,
            179,
            0,
            213,
            SoundExpressionEffect.NONE,
            InterpolationCurve.CURVE),
        SoundExpressionPlayMode.IN_BACKGROUND)
joystickbit.on_button_event(joystickbit.JoystickBitPin.P12,
    joystickbit.ButtonType.DOWN,
    my_function4)

joystickbit.init_joystick_bit()
x = joystickbit.get_rocker_value(joystickbit.rockerType.X)
y = joystickbit.get_rocker_value(joystickbit.rockerType.Y)
music.play_sound_effect(music.builtin_sound_effect(soundExpression.spring),
    SoundExpressionPlayMode.UNTIL_DONE)
led2 = led.point(2, 2)
serial.redirect_to_usb()

def on_forever():
    global x, y
    if x != joystickbit.get_rocker_value(joystickbit.rockerType.X):
        x = joystickbit.get_rocker_value(joystickbit.rockerType.X)
        radio.send_value("x", x)
    if y != joystickbit.get_rocker_value(joystickbit.rockerType.Y):
        y = joystickbit.get_rocker_value(joystickbit.rockerType.Y)
        radio.send_value("y", y)
    serial.write_value("x", joystickbit.get_rocker_value(joystickbit.rockerType.X))
basic.forever(on_forever)
