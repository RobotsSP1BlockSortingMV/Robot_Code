import MachineVision as mv
import Movement as rbaction
import time
horizontal_d = 10000000
vertical_d = 10000000

#Move arm into inital position
rbaction.movement_command('sit_down',0)
#time.sleep(10)
#rbaction.movement_command('standing_position',0)
#time.sleep(15)
#rbaction.movement_command('walking_position',0)
#time.sleep(15)
#rbaction.movement_command('move_head_up_or_down',160)
#time.sleep(8)
#rbaction.movement_command('move_right_upper_shoulder',1)
#time.sleep(8)
#rbaction.movement_command('move_right_elbow',120)
#time.sleep(8)
#rbaction.movement_command(('move_right_lower_shoulder'),120)
#rbaction.movement_command('move_neck_left_or_right',145)
#rbaction.movement_command('move_left_upper_shoulder',140)
while True:
    capture_device = mv.set_capture(1)
    color1_lower,color1_upper,color2_lower,color2_upper = mv.set_color_ranges()
    horizontal_d,vertical_d = mv.view_image_get_distance(color1_lower,color1_upper,color2_lower,color2_upper,capture_device)
    print(horizontal_d,vertical_d)
    #if h,v 1000000 then move head until distance changes
    #elif h,v > 50 move arm depending on range right or left 
    #keep going till this loop ends 

#Activate magnet code 
#Move arm up 
#Find box to place in?