def fileNaming(names):
    used_names = dict()
    new_names = []
    for name in names:
        if used_names.get(name) is None:
            used_names[name] = 1
            new_names.append(name)
            continue

        new_name = name
        c = 0
        while used_names.get(new_name) is not None:
            c += 1
            new_name = name + '(' + str(c) + ')'

        new_names.append(new_name)
        used_names[new_name] = 1

    return new_names


"""
You are given an array of desired filenames in the order of their creation. Since two files cannot have equal names,
the one which comes later will have an addition to its name in a form of (k), where k is the smallest positive
integer such that the obtained name is not used yet.

Return an array of names that will be given to the files.

Example

For names = ["doc", "doc", "image", "doc(1)", "doc"], the output should be
fileNaming(names) = ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"].
"""