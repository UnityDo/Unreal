class Subtitle:
    def __init__(self, sequence, start_time, end_time, text):
        self.sequence = sequence
        self.start_time = start_time
        self.end_time = end_time
        self.text = text


def parse_srt(file_path):
    subtitles = []
    with open(file_path, 'r') as f:
        sequence = start_time = end_time = text = None
        for line in f:
            line = line.strip()
            if not line and sequence and start_time and end_time and text:
                subtitles.append(Subtitle(sequence, start_time, end_time, text))
                sequence = start_time = end_time = text = None
            elif line.isdigit():
                sequence = int(line)
            elif '-->' in line:
                start_time, end_time = line.split('-->')
            else:
                text = line if not text else text + ' ' + line
        if sequence and start_time and end_time and text:
            subtitles.append(Subtitle(sequence, start_time, end_time, text))
    return subtitles

def time_to_frames(time_str, frame_rate=24):
    # Este es solo un ejemplo. Necesitarás ajustar esta función según tus necesidades.
    hours, minutes, seconds = map(int, time_str.split(':'))
    frames = hours * 3600 * frame_rate + minutes * 60 * frame_rate + seconds * frame_rate
    return frames



import unreal
level_sequence = unreal.load_asset("/Game/Sequencer/Test/SQ_Sincro_Captions.SQ_Sincro_Captions")
event_channel = level_sequence.get_movie_scene().get_event_channel()
subtitles = parse_srt(file_path)

for subtitle in subtitles:
    # Convertimos los tiempos de los subtítulos a frames
    # Necesitaremos definir una función 'time_to_frames' que convierta los tiempos de los subtítulos a frames
    start_frame = time_to_frames(subtitle.start_time)
    end_frame = time_to_frames(subtitle.end_time)

    # Creamos el evento de inicio
    start_event = event_channel.add_key(start_frame)
    start_event.set_editor_property('function_name', 'ExecutePlayerCaption')
    start_event.set_editor_property('payload_variables', [subtitle.text])

    # Creamos el evento de finalización
    end_event = event_channel.add_key(end_frame)
    end_event.set_editor_property('function_name', 'StopCaption')
