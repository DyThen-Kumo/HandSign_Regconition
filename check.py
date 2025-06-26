import os

link = r"C:\D\UIT\HOC KI 6\CS431\HandSign\data_gen"
for folder in os.listdir(link):
    print(folder)
    for file_img in os.listdir(os.path.join(link,folder)):
        names = file_img.split('.')[0].split('_')
        if names[-1] == 'd':
            new_name = f"{names[0]}_{int(names[1])+1000}.jpg"
            os.rename(os.path.join(link, folder, file_img), os.path.join(link, folder, new_name))