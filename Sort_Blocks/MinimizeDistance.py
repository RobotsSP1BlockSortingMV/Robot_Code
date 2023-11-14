import MachineVision as mv
import Movement as rbaction
import time
horizontal_d = 10000000
vertical_d = 10000000

right_elbow_current = 120
right_lower_shoulder_current = 120

#Move arm into inital position
rbaction.movement_command('sit_down',0)
def initial_position():
    rbaction.movement_command('standing_position',0)
    time.sleep(15)
    rbaction.movement_command('walking_position',0)
    time.sleep(15)
    rbaction.movement_command('move_head_up_or_down',160)
    time.sleep(8)
    rbaction.movement_command('move_right_upper_shoulder',1)
    time.sleep(8)
    rbaction.movement_command('move_right_elbow',120)
    time.sleep(8)
    rbaction.movement_command(('move_right_lower_shoulder'),120)
    time.sleep(3)
    rbaction.movement_command('move_neck_left_or_right',145)

#initial_position()
#rbaction.movement_command('move_neck_left_or_right',140)
#rbaction.movement_command('move_right_lower_shoulder', 120)
#time.sleep(3)
#rbaction.movement_command('move_right_elbow',right_elbow_current)
while True:
    capture_device = mv.set_capture(1)
    color1_lower,color1_upper,color2_lower,color2_upper = mv.set_color_ranges()
    horizontal_d,vertical_d = mv.view_image_get_distance(color1_lower,color1_upper,color2_lower,color2_upper,capture_device)
    print(horizontal_d,vertical_d)
    #if vertical_d > 20:
    #    right_elbow_current -= 10
    #    rbaction.movement_command('move_right_elbow',(right_elbow_current))
    #    time.sleep(3)
    #elif vertical_d < 0:
    #    right_elbow_current += 10
    #    rbaction.movement_command('move_right_elbow',(right_elbow_current))
    if horizontal_d > 0:
        right_lower_shoulder_current -= 10
        rbaction.movement_command('move_right_lower_shoulder',right_lower_shoulder_current)
    elif horizontal_d < 0:
        right_lower_shoulder_current += 10
        rbaction.movement_command('move_right_lower_shoulder', right_lower_shoulder_current)
        time.sleep(3)



