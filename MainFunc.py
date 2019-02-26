import pandas as pd
import time
import datetime
from os import listdir
from os.path import isfile, join
from Compression import compressFunc,CreateVideoDetails,vqmt
from FeatureExtraction import Feature_Extraction
from pathlib import Path, PureWindowsPath
from Dataset import Update_CSV

corePath = str(PureWindowsPath(Path("E:/New folder")))
ffmpeg = '"E:\\N.I.B.B.A.S\\StaxRip 1.9.0.0\\Apps\\ffmpeg\\ffmpeg.exe"'
mkvmerge = '"E:\\N.I.B.B.A.S\\StaxRip 1.9.0.0\\Apps\\MKVToolNix\\mkvmerge.exe"'
mediaInfo = "E:\\New folder\\MediaInfo\\"
VQMT = '"E:\\VQMT\\VQMT.exe"'
videoFileList = [f for f in listdir(corePath + "\\Input\\") if isfile(join(corePath + "\\Input\\", f))]
presets = ['superfast', 'veryfast', 'faster', 'fast', 'medium', 'slow', 'slower']
presets1 = ['superfast', 'veryfast', 'medium']
df_for_video_data = pd.DataFrame(columns=['Video Name','Width', 'Height', 'Video Length', 'Frames per Second',
                'Frame Count', 'Original Bitrate', 'Original Size', 'Scene Count', 'Avg Motion %',
                'Avg PCC', 'Compression Preset','Compression Duration', 'Compressed Bitrate', 'Compressed Size'])
print('Obtained videos are : ',videoFileList)
for video in videoFileList:
    print("Processing file : " + video)
    start = time.time()
    features_of_original_video = Feature_Extraction.feature_extr(corePath + "\\Input\\" + video)
    end = time.time()
    feTime = end - start
    print('Feature Extraction took ' + time.strftime("%H:%M:%S", time.gmtime(feTime)))

    start = time.time()
    compressFunc.compressdis(corePath, video, presets1, ffmpeg, mkvmerge)
    details_of_original_video = CreateVideoDetails.CreateVideoDetail(corePath, video, mediaInfo)
    preset_wise_bitrate_and_size = CreateVideoDetails.CreateCompVideoDetail(corePath, video, mediaInfo)
    preset_wise_duration_and_frames = CreateVideoDetails.retrieveCompressionDetail(corePath, video)
    end = time.time()
    clTime = end - start
    print('Compression and Logging took ' + time.strftime("%H:%M:%S", time.gmtime(clTime)))

    start = time.time()
    vqmt.videoQualityMeasure(corePath, video, presets1, details_of_original_video[2], details_of_original_video[3], preset_wise_duration_and_frames[0][2], ffmpeg, VQMT)
    end = time.time()
    vqmtTime = str(datetime.timedelta(end - start))
    print('Video Quality Measurement took ' + vqmtTime + ' seconds')
    vqmtTime = end - start
    print('Video Quality Measurement took ' + time.strftime("%H:%M:%S", time.gmtime(vqmtTime)))
    totalProcessTime = float(feTime) + float(clTime) + (vqmtTime)
    print('Processing complete\nTotal Processing Time : ' + time.strftime("%H:%M:%S", time.gmtime(totalProcessTime)))
    Update_CSV.push_data_to_csv(presets, features_of_original_video, details_of_original_video, preset_wise_bitrate_and_size, preset_wise_duration_and_frames)

