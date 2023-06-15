import unreal

capture = unreal.AutomatedLevelSequenceCapture()
capture.level_sequence_asset = unreal.LevelSequence'Game/Cinematics/Takes/MySequence.MySequence'
capture.shot_name = 'MyShot'
capture.use_custom_start_frame = True
capture.custom_start_frame = 10
capture.use_custom_end_frame = True
capture.custom_end_frame = 100
capture.warm_up_frame_count = 10
capture.write_edit_decision_list = True
capture.write_subtitles = True
capture.write_final_image = True

capture.initialize()
capture.start_capture()
