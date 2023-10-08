import Movement as mo
import MachineVision as mv

distance = 10000000
while distance > 100:
    capture_device = mv.set_capture(0)
    distance = mv.view_image_get_distance(mv.set_color_ranges(),capture_device)