import os



current_dir = os.getcwd()  # 获取当前目录, -> list

create_dirs = ['book', 'document', 'video']


def find_father_dir(current_path):
    dir_list = [os.path.join(current_path, item) for item in os.listdir(current_path) if
                item not in create_dirs]  # 获取当前目录下的item
    sundir = hSumDir(dir_list)  # 判断当前目录下是否存在子目录
    if sundir:
        for sun in dir_list:
            if os.path.isdir(sun):
                find_father_dir(os.path.join(current_path, sun))
            else:
                continue
    else:
        create_dir(current_path, create_dirs)


def hSumDir(dirlist):
    return any(diritem for diritem in dirlist if os.path.isdir(diritem))


def create_dir(create_path, create_dirs):
    for path in create_dirs:
        item_path = os.path.join(create_path, path)
        if create_path == item_path:
            continue

        print("create start")
        if not os.path.exists(item_path):
            os.makedirs(item_path)


find_father_dir(current_dir)
