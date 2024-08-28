import sys
import os

def _get_video_subfolder(path):
    #scans for folder in statcast_video_builder containing "videos"
    for f in os.scandir(path):
        if f.is_dir() and 'videos' in f.name:
            return f
        
def _get_csv_path_from_path(path):
    #scans for folder in statcast_video_builder containing "videos"
    for f in os.scandir(path):
        if f.is_file and '.csv' in f.name:
            return f.path
        
def _get_current_timeline(project):
    timeline = project.GetCurrentTimeline()
    if not timeline:
        if project.GetTimelineCount() > 0:
            timeline = project.GetTimelineByIndex(1)
            project.SetCurrentTimeline(timeline)

    if not timeline:
        print("Current project has no timelines")
        sys.exit()

    return timeline

def _properly_format_standard_brewers_text(text_tool, text_string, position):
    text_tool.SetInput('StyledText', text_string)
    text_tool.SetInput('Center', position)
    text_tool.SetInput('Font', 'Brewers Industrial')
    text_tool.SetInput('Style', 'Book')
    text_tool.SetInput('VerticalJustificationTop', 1)
    text_tool.SetInput('HorizontalJustificationLeft', 1)
    text_tool.SetInput('Size', .07)
    return text_tool