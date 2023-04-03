import pandas as pd
import matplotlib.pyplot as plt
import os as os


# Add validation to check if the file already exists
def create_save_file(data):
    filename = data['name'][0] + '.csv'
    progress_filename = data['name'][0] + '_progress' + '.csv'

    data.to_csv(filename, index=False)
    obj_path = os.path.join(filename)
    data.to_csv(filename, index=False)
    
    create_objective_plot(obj_path)


def delete_save_file():
    pass


def create_objective_plot(filename):
    df_basic_info = pd.read_csv(filename)
    # df_progress_info = pd.DataFrame(
    #     columns=['streak']
    # )

    print(df_basic_info)
    plt.plot([1, 2, 3], [4, 5, 6])
    plt.title(df_basic_info['name'][0])
    plt.show()
    return


# this function creates folder for saves only if user has not done it before
# def create_saves_folder():
#     if os.path.isdir("C:\\HbtsApp"):
#         return
#     else:
#         check_path = os.path.join("C:\\", "HbtsApp")
#         os.makedirs(check_path)
#         source_directory = filedialog.askdirectory(title="Selected Directory will be used to save your data and settings")
#         path = os.path.join(source_directory, "Saves")
#         os.makedirs(path)
#     return path


# this function sets the saves folder arbitraily  
# def create_saves_folder():
#     if os.path.isdir("C:\\HbtsApp"):
#         return
#     else:
#         check_path = os.path.join("C:\\", "HbtsApp")
#         os.makedirs(check_path)
#         path = os.path.join(check_path, "Saves")
#         os.makedirs(path)
#     return path