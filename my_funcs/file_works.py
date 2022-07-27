def files(filepatch):
    with open(filepatch, "r") as f_o:
        return f_o.readlines()
