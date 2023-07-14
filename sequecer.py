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
event_trigger=unreal.MovieSceneEventTrackExtensions.add_event_trigger_section(event_track)
     event_trigger.set_display_name("Event Captions")



