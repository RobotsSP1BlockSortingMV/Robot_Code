import MachineVision as mv
import Movement as bs
distance = 100000000

while distance > 100:
    capture_device = mv.set_capture(0)
    color1_lower,color1_upper,color2_lower,color2_upper = mv.set_color_ranges()
    distance = mv.view_image_get_distance(color1_lower,color1_upper,color2_lower,color2_upper,capture_device)