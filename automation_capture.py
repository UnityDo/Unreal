BAD
import unreal

capture = unreal.AutomatedLevelSequenceCapture()
level_sequence_path = "/Game/Cinematics/Takes/MySequence.MySequence"
level_sequence_soft_path = unreal.SoftObjectPath(level_sequence_path)
capture.level_sequence_asset = level_sequence_soft_path
capture.shot_name = 'MyShot'
capture.use_custom_start_frame = True
capture.custom_start_frame = unreal.FrameNumber(10)  # Crear objeto FrameNumber con valor 10
capture.use_custom_end_frame = True
capture.custom_end_frame = unreal.FrameNumber(100)  # Crear objeto FrameNumber con valor 100
capture.warm_up_frame_count = 10
capture.write_edit_decision_list = True

capture.initialize()
capture.start_capture()

