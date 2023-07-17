import unreal

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

# Cargar la secuencia de nivel
level_sequence = unreal.load_asset("/Game/Sequencer/Test/SQ_Sincro_Captions.SQ_Sincro_Captions")

# Agregar pista de eventos a la secuencia
sequencer = unreal.LevelSequenceEditorToolkit(level_sequence)
event_track = sequencer.add_master_track(unreal.MovieSceneEventTrack)

# Crear un nuevo canal de eventos en la pista de eventos
section = event_track.create_new_section()
event_channel = section.add_channel(unreal.MovieSceneScriptingEventChannel)

# Suponiendo que 'file_path' es la ruta al archivo .srt
subtitles = parse_srt(file_path)

for subtitle in subtitles:
    # Convertir los tiempos de los subtítulos a frames
    start_frame = time_to_frames(subtitle.start_time)
    end_frame = time_to_frames(subtitle.end_time)

    # Crear el evento de inicio
    start_event = event_channel.add_key(start_frame)
    start_event.set_editor_property('function_name', 'ExecutePlayerCaption')
    start_event.set_editor_property('payload_variables', [subtitle.text])

    # Crear el evento de finalización
    end_event = event_channel.add_key(end_frame)
    end_event.set_editor_property('function_name', 'StopCaption')
