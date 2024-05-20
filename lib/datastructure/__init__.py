import pickle


def dump(Obj, file):
    with open(file, 'wb') as f:
        pickle.dump(Obj, f)


def load(file):
    with open(file, 'rb') as f:
        Obj = pickle.load(f)
    return Obj
