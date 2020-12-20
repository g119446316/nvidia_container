from jtop import jtop, JtopException


def read_stats(jetson):
    """
    This is your callback function where you can read all files when are availables.
    """
    print(jetson.stats)


if __name__ == "__main__":
    print("Initialize jtop callback")
    # Open the jtop
    jetson = jtop()
    # Attach a function where you can read the status of your jetson
    jetson.attach(read_stats)

    # This try excpet will catch jtop exception
    try:
        # This loop will manage the jtop status all the time
        # This is a blocking a function, if you do not want use you can use as well
        # start: jetson.start()
        # stop: jetson.stop()
        jetson.loop_for_ever()
    except JtopException as e:
        print(e)
# EOF
