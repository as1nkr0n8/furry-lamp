import os
import subprocess
from os import listdir
from os.path import isfile, join
from pathlib import Path, PureWindowsPath

def CreateVideoDetail(corePath, inputVideoName, mediaInfo, video_dataframe):
    videoPath = '"' + corePath + "\\Input\\" + inputVideoName + '"'
    print("Creating input video details")
    print(videoPath)
    os.chdir(mediaInfo.replace("\\", "/"))
    os.getcwd()
    name = subprocess.check_output('MediaInfo.exe --Inform="General;%FileNameExtension%" "$@" ' + videoPath, shell=True).decode('utf-8')
    duration = subprocess.check_output('MediaInfo.exe --Inform="General;%Duration%" "$@" ' + videoPath, shell=True).decode('utf-8')
    vbitrate = subprocess.check_output('MediaInfo.exe --Inform="Video;%BitRate%" "$@" ' + videoPath, shell=True).decode('utf-8')
    width = subprocess.check_output('MediaInfo.exe --Inform="Video;%Width%" "$@" ' + videoPath, shell=True).decode('utf-8')
    height = subprocess.check_output('MediaInfo.exe --Inform="Video;%Height%" "$@" ' + videoPath, shell=True).decode('utf-8')
    framerate = subprocess.check_output('MediaInfo.exe --Inform="General;%FrameRate%" "$@" ' + videoPath, shell=True).decode('utf-8')
    size = subprocess.check_output('MediaInfo.exe --Inform="General;%FileSize%" "$@" ' + videoPath, shell=True).decode('utf-8')
    format = subprocess.check_output('MediaInfo.exe --Inform="General;%Format%" "$@" ' + videoPath, shell=True).decode('utf-8')
    print(size)

    index_list = video_dataframe.index[video_dataframe['Video Name'] == videoPath].tolist()

    for i in index_list:
        video_dataframe['Video Length'][i] = duration
        video_dataframe['Original Bitrate'][i] = vbitrate
        video_dataframe['Width'][i] = width
        video_dataframe['Height'][i] = height
        video_dataframe['Frames per Second'][i] = framerate
        video_dataframe['Original Size'][i] = size

def CreateCompVideoDetail(corePath, inputVideoName, mediaInfo,  video_dataframe):
    # videoPath = '"' + corePath + "\\Input\\" + inputVideoName + '"'
    compressedVideosPath = corePath + "\\Output\\" + inputVideoName.split('.')[0] + "\\"  # path to compressed videos
    print("Creating compressed video details")
    print(compressedVideosPath)
    videoFileList = [f for f in listdir(compressedVideosPath) if isfile(join(compressedVideosPath, f))]
    for video in videoFileList:
        os.chdir(mediaInfo.replace("\\", "/"))
        os.getcwd()
        videoPath = '"' + compressedVideosPath + "\\" + video + '"'
        name = subprocess.check_output('MediaInfo.exe --Inform="General;%FileNameExtension%" "$@" ' + videoPath,
                                       shell=True).decode('utf-8')
        duration = subprocess.check_output('MediaInfo.exe --Inform="General;%Duration%" "$@" ' + videoPath,
                                           shell=True).decode('utf-8')
        vbitrate = subprocess.check_output('MediaInfo.exe --Inform="Video;%BitRate%" "$@" ' + videoPath,
                                           shell=True).decode('utf-8')
        width = subprocess.check_output('MediaInfo.exe --Inform="Video;%Width%" "$@" ' + videoPath,
                                        shell=True).decode('utf-8')
        height = subprocess.check_output('MediaInfo.exe --Inform="Video;%Height%" "$@" ' + videoPath,
                                         shell=True).decode('utf-8')
        framerate = subprocess.check_output('MediaInfo.exe --Inform="General;%FrameRate%" "$@" ' + videoPath,
                                            shell=True).decode('utf-8')
        size = subprocess.check_output('MediaInfo.exe --Inform="General;%FileSize%" "$@" ' + videoPath,
                                       shell=True).decode('utf-8')
        format = subprocess.check_output('MediaInfo.exe --Inform="General;%Format%" "$@" ' + videoPath,
                                         shell=True).decode('utf-8')
        print(vbitrate)

        # index_for_preset = df.index[df['Video Name'] == videoPath].tolist()

def retrieveCompressionDetail(corePath, inputVideoName, video_dataframe):
    compressionDetailPath = corePath + "\\Stats\\" + inputVideoName.split('.')[0] + "\\"   #path to compressed videos
    txtFileList = [f for f in listdir(compressionDetailPath) if isfile(join(compressionDetailPath, f))]
    for txtFile in txtFileList:
        f = open(compressionDetailPath + txtFile, "r")
        searchlines2 = f.readlines()
        f.close()
        for line in searchlines2:
            if "encoded" in line:
                r6=line
                break
        print(r6)
        flag=0
        fram=""
        totaltime=""
        c=2
        for i in r6:
            if i is " " and flag is 0:
                flag=1
                continue
            if flag is 1:
                if i is " ":
                    flag=2
                    continue
                fram+=i
            if flag is 2:
                if i is " ":
                    c-=1
                if c is 0:
                    if i is 's':
                        break
                    totaltime+=i
        compressionTime = totaltime.replace(" ", "")
        print(compressionTime)
        totalFrames = fram.replace(" ", "")
        print(totalFrames)
