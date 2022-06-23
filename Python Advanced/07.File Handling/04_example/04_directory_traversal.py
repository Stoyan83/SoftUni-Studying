# from os import listdir, path
#
# full_path = path.dirname(path.abspath("Example"))
#
# def traverse_dir(current_path, ext):
#     for el in listdir(current_path):
#         if path.isdir(path.join(current_path, el)):
#             traverse_dir(path.join(current_path, el), ext)
#         else:
#             extension = el.split('.')[-1]
#             if extension not in ext:
#                 ext[extension] = []
#             ext[extension].append(el)
#
#
# ext = {}
# traverse_dir(full_path, ext)
#
# for e, files in sorted(ext.items()):
#     print(f"{e}")
#     for f in sorted(files):
#         print(f"--- {f}")


from os import walk, path

ext = {}

full_path = path.dirname(path.abspath("Example"))

for _, _, files in walk(full_path):
    for f in files:
        file_path = path.join(full_path, f)
        extension = file_path.split(".")[-1]
        if extension not in ext:
            ext[extension] = []
        ext[extension].append(f)

for e, files in sorted(ext.items()):
    print(f"{e}")
    for f in sorted(files):
        print(f"--- {f}")
