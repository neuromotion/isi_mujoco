import mujoco
from mujoco import viewer
import math


ten_file = open("output/TLengthWrite.txt", "w")

model = mujoco.MjModel.from_xml_path('isi_mujoco/models/gait10dof18musc_pinned.xml')
data = mujoco.MjData(model)

# def control_callback(model, data):
#     # Calculate the control input

# mujoco.set_mjcb_control(control_callback)

# mjfGeneric.mjcb_control = mycontroller

muscle = "9"
frequency = 1

def mycontroller(m, d):
  hTension = abs(math.cos(frequency*d.time))
  if d.time > 10:
    d.ctrl[int(muscle)] = hTension
mujoco.set_mjcb_control(mycontroller)




# # Set up the control callback
# mjcb = mjcb_control.MjcbControl(model, control_callback)
# sim.add_callback(mjcb)


# Computes global Cartesian poses for all objects
mujoco.mj_kinematics(model, data)

# Testing what data can be pulled
# print(data.geom_xpos)
# print(data.ten_length)
# print(data.ten_length[0])
# print(data.ten_length[17])

muscle_list = ["hamstrings_r = [0]", "bifemsh_r = [1]", "glut_max_r = [2]", "iliopsoas_r = [3]", "rect_fem_r = [4]", "vasti_r = [5]", "gastroc_r = [6]", "soleus_r = [7]", "tib_ant_r = [8]", "hamstrings_l = [9]", "bifemsh_l = [10]", "glut_max_l = [11]", "iliopsoas_l = [12]", "rect_fem_l = [13]", "vasti_l = [14]", "gastroc_l = [15]", "soleus_l = [16]", "tib_ant_l = [17]"]

# def control_callback(t, qpos, qvel):
#   # Calculate the control input
#   u = -5.0 * qpos[1] - 0.1 * qvel[1]
#   return u
        
# mjcb_control = mjfGeneric.mjcb_control(model, control_callback)

# while data.time < 5:
#   # Step the simulation.
#   mujoco.mj_step(model, data)
#     # Set up the control callback
#   sim.add_callback(mjcb)

# do in the callback, sees a 5 for muscle force, goes thru calcs
# data.ctrl[0] = 5

viewer.launch(model)

while True:
  muscle = input("Enter integer muscle index, or type 'list': ")
  if muscle == "list":
    print(muscle_list)
  else:
    time = input("How many seconds of data do you want to record? ")
    while data.time < int(time):
      # Step the simulation.
      mujoco.mj_step(model, data)
      # print(data.ten_length)
      # Writes lengths of hamstring_r, the first muscle actuator
      ten_file.write(str(data.ten_length[int(muscle)]) + "\n")
    quit()
 
# Writes data into text file as integers separated by spaces
  #for i in range(1, 18):
  #   ten_file.write(str(data.ten_length[i-1]) + " ")
  # ten_file.write("\n")

# Writes data into text file as collection of lists
  #ten_file.write(str(data.ten_length))

