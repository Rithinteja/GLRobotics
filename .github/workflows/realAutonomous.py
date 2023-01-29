#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
left_motor_a = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
left_motor_b = Motor(Ports.PORT10, GearSetting.RATIO_18_1, False)
left_drive_smart = MotorGroup(left_motor_a, left_motor_b)
right_motor_a = Motor(Ports.PORT11, GearSetting.RATIO_18_1, True)
right_motor_b = Motor(Ports.PORT20, GearSetting.RATIO_18_1, True)
right_drive_smart = MotorGroup(right_motor_a, right_motor_b)
drivetrain = DriveTrain(left_drive_smart, right_drive_smart, 319.19, 295, 40, MM, 1)
intakeMotor = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
spinMotor = Motor(Ports.PORT4, GearSetting.RATIO_18_1, False)
rollerMotor = Motor(Ports.PORT5, GearSetting.RATIO_18_1, False)


# wait for rotation sensor to fully initialize
wait(30, MSEC)
#endregion VEXcode Generated Robot Configuration

# ------------------------------------------
# 
# 	Project:      VEXcode Project
#	Author:       VEX
#	Created:
#	Description:  VEXcode V5 Python Project
# 
# ------------------------------------------

# Library imports
from vex import *

# Begin project code
def motorConfig():
    drivetrain.set_stopping(HOLD)
    intakeMotor.set_stopping(HOLD)
    spinMotor.set_stopping(HOLD)
    rollerMotor.set_stopping(HOLD)
    intakeMotor.set_velocity(70, PERCENT)
    intakeMotor.set_max_torque(70, PERCENT)

def blueRoller():
    motorConfig()

    rollerMotor.spin(FORWARD)
    wait(2, SECONDS)
    rollerMotor.stop()

    drivetrain.turn_for(RIGHT, 135, DEGREES)
    drivetrain.drive_for(FORWARD, 60, INCHES)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 2, INCHES)

    intakeMotor.spin_for(FORWARD)

def redRoller():
    motorConfig()

    rollerMotor.spin(FORWARD)
    wait(2, SECONDS)
    rollerMotor.stop()

    drivetrain.turn_for(LEFT, 135, DEGREES)
    drivetrain.drive_for(FORWARD, 60, INCHES)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 2, INCHES)

    intakeMotor.spin_for(FORWARD)
                
def blueNoRoller():
    motorConfig()

    drivetrain.drive_for(FORWARD, 24, INCHES)
    drivetrain.turn_for(RIGHT, 90, DEGREES)

    rollerMotor.spin(FORWARD)
    wait(2, SECONDS)

    drivetrain.turn_for(RIGHT, 135, DEGREES)
    drivetrain.drive_for(FORWARD, 60, INCHES)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 24, INCHES)

def redNoRoller():
    motorConfig()

    drivetrain.drive_for(FORWARD, 24, INCHES)
    drivetrain.turn_for(RIGHT, 90, DEGREES)

    rollerMotor.spin(FORWARD)
    wait(2, SECONDS)

    drivetrain.turn_for(RIGHT, 135, DEGREES)
    drivetrain.drive_for(FORWARD, 60, INCHES)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 24, INCHES)
