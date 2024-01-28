from arena import *

# setup library
scene = Scene(host="arenaxr.org", namespace = "yongqiz2", scene="yolo")

# make a box
box = Box(object_id="myBox", position=(0,0.45,-3), scale=(.45,.90,.45))

# add the box to ARENA
scene.add_object(box)


@scene.run_forever(interval_ms=200)
def periodic():
    with open('value.txt', 'r') as file:
        try:
            values = file.read().split(']')
            x = float(values[0].split('[')[-1])
            y = float(values[2].split('[')[-1])
            z = float(values[1].split('[')[-1])
        except Exception as e:
            print(e)

    #x = box.data.position.x + 0.1

    box.update_attributes(position=Position(-x,y,-z))

    scene.update_object(box)


# start tasks
scene.run_tasks()

