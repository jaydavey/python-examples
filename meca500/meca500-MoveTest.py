#this program moves the meca500
Program = """SetTRF(0,0,50,180,0,90)
                SetBlending(50)
                SetCartAcc(100)
                SetCartAngVel(150)
                SetCartLinVel(400)
                SetJointAcc(150)
                SetJointVel(100)
                MoveJoints(0,0,0,0,0,0)
                SetWRF(-173.205,-100,0,0,0,-240)
                MovePose(0,0,50,0,0,0)
                StartProgram(1)
                SetWRF(-100,-173.205,0,0,0,-210)
                MovePose(0,0,50,0,0,0)
                StartProgram(1)"""

Program = Program.replace(' ','')
movements = Program.split("\n")

import MecademicRobot

def AutoRepair(robot):
    if(robot.isInError()):
        robot.ResetError()
    elif(robot.GetStatus()['Paused']==1):
        robot.ResumeMotion()

robot = MecademicRobot.RobotController('192.168.1.174')
robot.connect()
robot.ActivateRobot()
robot.home()
robot.SetWRF(200,0,0,0,0,-90)
robot.SetTRF(0,0,50,180,0,90)
robot.SetBlending(100)
robot.SetCartAcc(100)     #600 %     max
robot.SetCartAngVel(300)  #300 deg/s max
robot.SetCartLinVel(500)  #1000 mm/s max
robot.SetJointAcc(150)    #150 %     max
robot.SetJointVel(100)    #100 %     max
# robot.StartProgram(1)
# robot.SetEOB(1)
# robot.SetEOM(1)

for action in movements:
  robot.exchange_msg(action)
  if(robot.is_in_error()):
    AutoRepair(robot)

robot.disconnect()