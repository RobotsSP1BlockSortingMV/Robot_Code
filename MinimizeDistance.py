import MachineVision as mv
import Movement as bo
horizontal_d = 10000000
vertical_d = 10000000

while horizontal_d > 50 and vertical_d > 50:
    capture_device = mv.set_capture(0)
    color1_lower,color1_upper,color2_lower,color2_upper = mv.set_color_ranges()
    horizontal_d,vertical_d = mv.view_image_get_distance(color1_lower,color1_upper,color2_lower,color2_upper,capture_device)
    print(horizontal_d,vertical_d)