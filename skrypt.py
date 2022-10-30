def my_function():
    qbit.set_qbit_run_speed(10, qbit.OrientionType.GO_AHEAD)
qbit.onQbit_remote_ir_pressed(qbit.IRKEY.UP, my_function)

def my_function2():
    qbit.set_qbit_run_speed(85, qbit.OrientionType.TURN_LEFT)
qbit.onQbit_remote_ir_pressed(qbit.IRKEY.LEFT, my_function2)

def my_function3():
    qbit.set_qbit_run_speed(85, qbit.OrientionType.TURN_RIGHT)
qbit.onQbit_remote_ir_pressed(qbit.IRKEY.RIGHT, my_function3)

def my_function4():
    qbit.set_qbit_run_speed(10, qbit.OrientionType.GO_BACK)
qbit.onQbit_remote_ir_pressed(qbit.IRKEY.DOWN, my_function4)

qbit.qbit_init()

def on_every_interval():
    if qbit.ultrasonic() > 15:
        qbit.set_qbit_run_speed(10, qbit.OrientionType.GO_AHEAD)
    else:
        qbit.set_qbit_run_speed(85, qbit.OrientionType.TURN_RIGHT)
loops.every_interval(1000, on_every_interval)
