import os

ROOT = os.path.dirname(__file__)
project_name = 'my_project1'
paths = [os.path.join(project_name, 'setting'),
         os.path.join(project_name, 'adminapp'),
         os.path.join(project_name, 'authapp'),
         os.path.join(project_name, 'mainapp')]
for _path in paths:
    os.makedirs(os.path.join(ROOT, _path), exist_ok=True)



def create_parent(dir_name):
    try:
        os.mkdir(dir_name)
    except FileExistsError as e:
        print(f'dir exist: {e.filename}')
    return 0


def create_child_dirs(parent, *dirs):
    for el in dirs:
        try:
            dir_path = os.path.join(parent, el)
            os.mkdir(dir_path)
        except FileExistsError as e:
            print(f'dir exist: {e.filename}')
        return 0


def create_starter(main_dir):
    create_parent(main_dir)
    create_child_dirs(main_dir, 'settings', 'mainapp', 'authapp', 'adminapp')


if __name__ == '__main__':
    create_starter('my_project1')