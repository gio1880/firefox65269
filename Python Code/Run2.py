from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port,Direction

hub = PrimeHub()
left_motor = Motor(Port.B,Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E,Direction.CLOCKWISE)
RAM = Motor(Port.F)
LAM = Motor(Port.D)

wheel_diameter = 56
axle_track = 122
robot = DriveBase(left_motor,right_motor,wheel_diameter,axle_track)

robot.use_gyro(True)

robot.settings(straight_speed = 720,straight_acceleration= 300, turn_rate=600, turn_acceleration=400)
hub.imu.reset_heading(0)

if hub.imu.ready():
    robot.straight(175)
    robot.turn(-43)
    robot.straight(300)
    RAM.run_time(-600,1300)
    LAM.run_time(800,700)
    LAM.run_time(-200,500)
    LAM.run_time(-800,800)
    robot.straight(-300)
    robot.straight(120)
    RAM.run_time(600,1300)
    robot.straight(100)
    robot.straight(-47)
    robot.turn(-90)
    robot.straight(90)
    robot.straight(-170)
    robot.turn(90)
    robot.straight(-500)
    