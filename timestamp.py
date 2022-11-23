import datetime


def timeStamped(fname, fmt='%Y-%m-%d-%H-%M-%S-{fname}'):
    # This creates a timestamped filename so we don't overwrite our good work
    return datetime.datetime.now().strftime(fmt).format(fname=fname)


if __name__ == "__main__":
    run_name = timeStamped("test", fmt="{fname}_%Y%m%d_%H%M")
    print("Test output:", run_name)