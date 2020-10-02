import os

def general_modify(folder_dir: str, fn):
    """
    Single directory, non-recursive
    Must be complete directory
    """
    if os.path.isdir(folder_dir):
        for sub_dir in sorted(os.listdir(folder_dir)):
            true_sub_dir = os.path.join(folder_dir, sub_dir)  # 不要用拼接字符串来组子路径
            if os.path.isfile(true_sub_dir):
                fn(true_sub_dir)
    else:
        raise FileNotFoundError



folder = r"D:\Pictures\National Geography HD"
prefix = r"\NationalGeoHD-"
count = 1


for sub_dir in sorted(os.listdir(folder)):
    true_sub_dir = os.path.join(folder, sub_dir)
    os.rename(true_sub_dir, folder + prefix + str(count).rjust(3, "0") + ".jpg")
    count += 1

