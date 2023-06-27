import cv2
import argparse
import os


def main(args):
    vid_file = '/mnt/Data/Datasets/Own/RGB/' + args.file
    output_dir = '/mnt/Data/Datasets/Own/img/' + args.file[:-4] + '/'
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
            print(f"processed file {args.file} frame #{count}")
            count += 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=str, default='0608-yzk-walk')
    args = parser.parse_args()
    main(args)
