import os
templates_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../templates')


if __name__ == '__main__':
    # os.system('python ./model_generate/db2model.py')
    # os.system('python ./model_generate/db2model_view.py')
    print(templates_path)
    print(os.listdir(templates_path))