import cv2
import argparse
import os
import torch


def main(args):
    vid_file = '../data/rgb_ntu_selected/' + args.file
    output_dir = '/media/persec/Data/yzk/img_ntu_selected/' + args.file + '/'
    os.makedirs(output_dir, exist_ok=True)
    vidcap = cv2.VideoCapture(vid_file)
    success = True
    count = 0
    while success:
        success, image = vidcap.read()
        if success is True:
            filename = str(count)
            while len(filename) != 4:
                filename = "0" + filename
            # filename = args.file + "_" + filename + ".jpg"
            filename = filename + '.jpg'
            cv2.imwrite(output_dir + filename, image)
            count += 1
    print(f"Converted file {args.file} to images. {count} frames captured.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=str)
    args = parser.parse_args()
    main(args)
