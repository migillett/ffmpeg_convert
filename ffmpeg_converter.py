import os
import subprocess


def ffmpeg_converter(file_location):
    for root, dirs, files in os.walk(file_location):
        for file in files:
            if file.endswith('.VOB'):
                start_file = os.path.join(root, file)
                dest_file = os.path.join(root, os.path.splitext(file)[0] + '.mp4')
                
                command = 'ffmpeg -i "{0}" "{1}"'.format(start_file, dest_file)
                os.system(command)
                print('Conversion complete.')


if __name__ == '__main__':
    ffmpeg_converter('/test/location/')
