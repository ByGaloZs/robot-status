from app.fms import Robot

robot = Robot()
print(f"Estado inicial {robot.state}")
print("Estado inicial", robot.state)

robot.power_on()
print(f"Encendiendo robot y mostrando su estado: {robot.state}")
print("Encendiendo robot y mostrando su estado:", robot.state)

robot.error()
print(f"Robot en error y mostrando su estado: {robot.state}")
print("Robot en error y mostrando su estado:", robot.state)

robot.reset()
print(f"Reseteo del robot y mostrando su estado: {robot.state}")
print("Reseteo del robot y mostrando su estado: ", robot.state)

