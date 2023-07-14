import unreal

# Obtener el secuenciador seleccionado desde el Content Browser
selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()
sequencer = None
for asset in selected_assets:
    if isinstance(asset, unreal.LevelSequence):
        sequencer = asset
        break

if not sequencer:
    unreal.log_warning("No se ha seleccionado un secuenciador en el Content Browser.")
else:
    # Crear un nuevo evento de pista
    event_track = sequencer.add_master_track(unreal.MovieSceneEventTrack)
    event_track.set_display_name("ActivaSonido")

  # Agregar una sección al evento de pista
    section = event_track.add_event_trigger_section()
    section.set_start_frame_seconds(0)

   # Buscar o crear un canal de eventos
    event_channel = None
    for channel in section.get_channels():
        if isinstance(channel, unreal.MovieSceneScriptingEventChannel):
            event_channel = channel
            break

    if not event_channel:
        event_channel = section.add_channel(unreal.MovieSceneScriptingEventChannel)
        key = event_channel.add_key(unreal.FrameNumber(0))
        key.set_event_name("ActivaSonido")
    



