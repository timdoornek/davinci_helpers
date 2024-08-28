#!/usr/bin/env python

import constant
import helper_methods
from pprint import pprint
import sys

def add_videos_to_media_pool(resolve):
    media_storage = resolve.GetMediaStorage()

    video_path = helper_methods._get_video_subfolder(constant.VIDEO_PATH).path
    media_storage.AddItemListToMediaPool(video_path)

def add_videos_to_timeline_from_media_pool(project):
    media_pool = project.GetMediaPool()
    root_folder = media_pool.GetRootFolder()

    #get all clips currently in media pool, then sort them by name
    clip_list = root_folder.GetClipList()
    clip_list = sorted(clip_list, key = lambda clip : clip.GetClipProperty()['File Name'])

    #get frame rate of the videos in the clip list
    frame_rate = clip_list[0].GetClipProperty()['FPS']
    project.SetSetting('timelineFrameRate', str(frame_rate))

    #Create timeline:
    timelineName = "Timeline 1"
    timeline = media_pool.CreateEmptyTimeline(timelineName)
    if not timeline:
        print("Unable to create timeline '" + timelineName + "'")
        sys.exit()

    for clip in clip_list:
        media_pool.AppendToTimeline(clip)
