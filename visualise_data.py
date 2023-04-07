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

    df_basic_info = pd.read_csv(filename)
    df_progress_info = pd.DataFrame(
        columns=['days','streak','missed', 'percentage'],
    )
    # this datafreame will be used in creating plot showing user's regularity
    df_progress_info['days'] = [1]
    df_progress_info['streak'] = [1]
    df_progress_info['missed'] = [0]
    df_progress_info['percentage'] = 100 - (df_progress_info['missed'] / df_progress_info['days']) * 100

    progress_track_file = df_progress_info.to_csv(progress_filename, index=False)

    # create_objective_plot(progress_filename,  data['name'][0])


# plots should be generated dynamically when clicking the objective name.
# Plot generating lines shall be moved to different functions later so it'll be generated only when needed


def create_objective_plot(progress_filename):
    df = pd.read_csv(progress_filename + '_progress.csv')
    df['percentage'] = 100 - (df['missed'] / df['days']) * 100
    print(df)
    plt.plot(df['percentage'][0:])
    plt.ylim(0, 105)
    plt.xlim(0, None)
    plt.title(progress_filename)
    plt.show()
    # print(pd.read_csv(progress_filename))
    return


def delete_save_file():
    pass


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