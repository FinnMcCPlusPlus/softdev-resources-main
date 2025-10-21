from kivy.animation import Animation
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.animation import Animation
from pidev.kivy.ImageButton import ImageButton
from pidev.Joystick import Joystick
import pygame

try:
    joy = Joystick(0, False)
except pygame.error as e:
    print("No joystick connected, please connect and try again.")


class JoystickScreen(Screen):

    pressed = False

    def on_enter(self):
        Clock.schedule_interval(self.joy_update,0.05)
        print("Call to on_enter from JoystickScreen")

    def on_leave(self):
        Clock.unschedule(self.joy_update)
        print("Call to on_leave from JoystickScreen")

    def joy_update(self, dt=None):
        newx = self.ids.image_button.x + Joystick.get_axis(joy,"x") * 10
        newy = self.ids.image_button.y + Joystick.get_axis(joy,"y") * -10
        print(newx)
        print(newy)
        self.ids.image_button.x = newx
        self.ids.image_button.y = newy
        self.ids.x_pos.text = "x: " + str(newx)
        self.ids.y_pos.text = "y: " + str(newy)
        self.update_buttons_clicked()
        print("Call to joy_update from JoystickScreen")

    def update_buttons_clicked(self):
        butstr = ""
        for i in range(10):
            if joy.get_button_state(i):
                butstr += str(i)
        if butstr == "":
           self.ids.pressed_label.text = "No Buttons Pressed"
           print("No Buttons Pressed")
        else:
            self.ids.pressed_label.text = butstr
            print(butstr)

        print("Call to check_buttons_clicked from JoystickScreen")

    def switch_screen_main(self):
        print("Call to switch_screen_main from JoystickScreen")
        if not self.pressed:
            animate = Animation(color = (1,0,0,1), duration = 1)
            animate += Animation(size = (1000,1000), duration = 5)
            animate.start(self.ids.image_button)
            print("animation finished")
            self.pressed = True
        else:
            self.pressed = False
            print("returning to main")
            self.manager.current = 'main'

