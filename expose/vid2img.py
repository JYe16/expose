import cv2
import argparse
import os
from multiprocessing import Pool



def main(path, worker):
    multiproc_args = []
    train_files = os.listdir('/mnt/h/Datasets/NTU/mesh_pt_all/train/')
    test_files = os.listdir('/mnt/h/Datasets/NTU/mesh_pt_all/test/')
    # tr_c = 0
    # te_c = 0
    for filename in os.listdir(path):
        output_dir = ''
        if filename + '.pt' in train_files:
            output_dir = '/mnt/h/Datasets/NTU/rgb_img_single/train/' + filename[:-8] + '/'
            # tr_c += 1
            print(f'File {filename} has been assigned to training folder')
        elif filename + '.pt' in test_files:
            output_dir = '/mnt/h/Datasets/NTU/rgb_img_single/test/' + filename[:-8] + '/'
            # te_c += 1
            print(f'File {filename} has been assigned to testing folder')
        else:
            print(f'File {filename} is ignored.')
        if output_dir != '':
            multiproc_args.append([path, filename, output_dir])
    # print(f'train {tr_c} test {te_c}')
    p = Pool(worker)
    p.map(get_frames_into_img, multiproc_args)



def get_frames_into_img(p_args):
    path = p_args[0]
    filename = p_args[1]
    output_dir = p_args[2]
    vid_file = path + filename
    os.makedirs(output_dir, exist_ok=True)
    vidcap = cv2.VideoCapture(vid_file)
    success = True
    count = 0
    while success:
        success, image = vidcap.read()
        if success is True:
            img_name = str(count)
            while len(img_name) != 4:
                img_name = "0" + img_name
            # filename = args.file + "_" + filename + ".jpg"
            img_name = img_name + '.jpg'
            cv2.imwrite(output_dir + img_name, image)
            count += 1
    print(f"processed file {filename} with {count} frames")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str, default='/mnt/h/Datasets/NTU/rgb_avi_all/60/')
    parser.add_argument('--worker', type=int, default=6)
    args = parser.parse_args()
    folders = os.listdir(args.path)
    folders.sort()
    for i in range(0, len(folders), 1):
        folder = folders[i]
        path = args.path + folder + '/nturgb+d_rgb/'
        main(path, args.worker)
