import MachineVision as mv
import Movement as bo
horizontal_d = 10000000
vertical_d = 10000000

#Move arm into inital position
while horizontal_d > 50 and vertical_d > 50:
    capture_device = mv.set_capture(0)
    color1_lower,color1_upper,color2_lower,color2_upper = mv.set_color_ranges()
    horizontal_d,vertical_d = mv.view_image_get_distance1(color1_lower,color1_upper,color2_lower,color2_upper,capture_device)
    print(horizontal_d,vertical_d)
    #if h,v 1000000 then move head until distance changes
    #elif h,v > 50 move arm depending on range right or left 
    #keep going till this loop ends 

#Activate magnet code 
#Move arm up 
#Find box to place in?