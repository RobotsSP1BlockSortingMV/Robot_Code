import BaseMovement as bs
import MachineVision as mv

num_threads = 2
capture_device = mv.set_capture(0)
print(mv.view_image_get_distance(mv.set_color_ranges(),capture_device))