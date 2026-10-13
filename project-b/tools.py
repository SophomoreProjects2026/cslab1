


def read_file(path):
    if ".." in path:
        return (False, "Path may not go up a level.")

    try:
        file = open(path)
        return (True, file.read())
    except Exception as err:
        return (False, str(err))
    finally:
        file.close()


def write_file(path, data):
    if ".." in path:
        return (False, "Path may not go up a level.")

    try:
        file = open(path, "w")
        file.write(data)
        return (True, None)
    except Exception as err:
        return (False, str(err))
    finally:
        file.close()

def count_matching_lines(path, word):
    if ".." in path:
        return (False, "Path may not go up a level.")

    try:
        file = open(path)
        count = [(word in line) for line in file.read().split("\n")].count(True)
        return (True, count)
    except Exception as err:
        return (False, str(err))
    finally:
        file.close()
    