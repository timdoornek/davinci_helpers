import helper_methods
import constant
import pandas as pd

def _build_triple_slash_string_from_statcast_dataframe(df):
    distance_string = str(int(df.iloc[0][constant.DISTANCE_KEY])) + 'ft'
    ev_string = str(df.iloc[0][constant.EXIT_VELOCITY_KEY]) + ' EV'
    la_string = str(int(df.iloc[0][constant.DISTANCE_KEY])) + ' LA'
    return ' / '.join([distance_string, ev_string, la_string])

def _get_stat_string_with_label_from_dataframe(df, stat_constant, index):
    filtered_df = df[df['hit_index'] == index]
    return str(filtered_df.iloc[0][stat_constant['key']]) + stat_constant['label']

def adding_home_run_comp(project):
    #read in data for text
    df = pd.read_csv(helper_methods._get_csv_path_from_path(constant.VIDEO_PATH))

    #get current timeline
    timeline = project.GetCurrentTimeline()

    timeline_items = timeline.GetItemListInTrack("video", 1)
    comp_index = 0
    for timeline_item in timeline_items:
        comp = timeline_item.ImportFusionComp(constant.HOME_RUN_COMP_PATH)
        
        #find Text1 and change input text
        text1 = comp.FindTool("Text1")
        distance_string = _get_stat_string_with_label_from_dataframe(df, constant.DISTANCE_KEY, comp_index)
        la_string = _get_stat_string_with_label_from_dataframe(df, constant.LAUNCH_ANGLE_KEY, comp_index)
        wpa_string = _get_stat_string_with_label_from_dataframe(df, constant.WPA_KEY, comp_index)
        final_string = ' / '.join([distance_string, la_string]) + '\n' + wpa_string
        text1.SetInput('StyledText', final_string)
        print(final_string)

        #find Text2 and change input text
        text2 = comp.FindTool("Text2")
        ev_string = _get_stat_string_with_label_from_dataframe(df, constant.EXIT_VELOCITY_KEY, comp_index)
        text2.SetInput('StyledText', ev_string)
        print(ev_string)
        comp_index += 1
