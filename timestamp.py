import datetime


def timeStamped(fname, fmt='%Y-%m-%d-%H-%M-%S-{fname}'):
    """
        Creates a timestamped filename, so we don't override our good work
        
        Input:
            fname: the given file name
            fmt: the format of timestamp
        Output:
            a new file name with timestamp added
    """
    return datetime.datetime.now().strftime(fmt).format(fname=fname)


if __name__ == "__main__":
    run_name = timeStamped("test", fmt="{fname}_%Y%m%d_%H%M")
    print("Test output:", run_name)