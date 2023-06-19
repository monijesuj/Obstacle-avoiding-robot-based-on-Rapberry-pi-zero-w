# Obstacle-avoiding-robot-based-on-Rapberry-pi-zero-w

The obstacle avoidance robot is an intelligent device that can automatically recognize obstacles in front of it and avoid them by turning in a different direction. This design allows the robot to navigate in an unknown environment, avoiding collisions, which is a basic requirement for any autonomous mobile robot.
The main principle of operation of the robot is to use an ultrasonic sensor, which is mounted on a servo motor, to measure the distance to the obstacle and continue moving until the robot reaches a particular distance from the object, after which it stops. Then it turns the servo(and by implication the ultrasonic sensor) to the right to measure the distance to any obstacle, turns the servo to the left to measure the distance to the obstacle. Then compare the distances, whichever is greater, the robot turns in that direction. If both the distance is less than the given threshold, then the robot reverses, stops and again measures the distances to obstacles on both sides.

![image](https://github.com/MONIJESU1/Obstacle-avoiding-robot-based-on-Rapberry-pi-zero-w/assets/91800002/a4fc1506-4988-4264-962e-f18b0524ec67)

