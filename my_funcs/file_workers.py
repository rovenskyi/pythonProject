def read_from_files(filepatch):
    with open(filepatch, "r") as f_o:
        return f_o.readlines()


print(read_from_files("prodfile.txt"))
