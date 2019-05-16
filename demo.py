from moonmask.moonmask_ui import MoonMaskUI
ui = MoonMaskUI()

print("\nJanuary 2nd test: \n")
ui.set_moon_phase("2019"+'-'+"01"+'-'+"02")
ui.save_collage(filename='Jan-02')

text = input("\nJanuary 1st test: \n")

ui.set_moon_phase("2019"+'-'+"01"+'-'+"01")
ui.save_collage(filename='Jan-01')