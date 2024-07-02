file_path = "/home/user/docs/my.file.with.dots.py"


def get_file_info(file_path: str):
    *path, file_ = file_path.split("/")
    #print(path, file_)
    c = "." + file_[len(file_) - file_[::-1].find(".") : :]
    b = file_[: len(file_) - file_[::-1].find(".") - 1 :]
    a = ""
    for item in path:
        a += item + "/"
    #print(a, " ", b, " ", c)
    return (a, b, c)


get_file_info(file_path)


# *path, file_ = file_path.split("/")
# print(file_)
# b = file_[::-1].find(".")
# n = file_[len(file_) - file_[::-1].find(".") : :]
# v = file_[file_[::-1].find(".") : :]

# print(b, "\n", n, "\n", v)
