import unreal

# Obtén las referencias a las secuencias de nivel
secuencia_origen = unreal.load_asset("/Game/Sequencer/Test/CopyPaste/SQ_Copy.SQ_Copy")
secuencia_destino = unreal.load_asset("/Game/Sequencer/Test/CopyPaste/SQ_Paste.SQ_Paste")
# unreal.LevelSequenceEditorBlueprintLibrary.open_level_sequence(secuencia_destino)
binds=secuencia_origen.get_bindings() 
# Asegúrate de que ambas secuencias existen
if not secuencia_origen or not secuencia_destino:
    print("No se pudo encontrar una o ambas secuencias de nivel.")
else:
    # Copia todos los tracks de la secuencia origen a la secuencia destino
    for binds_origen in binds:
        print(binds_origen.get_display_name())
        tracks=binds_origen.get_tracks()
        for track in tracks:
            print(track.get_display_name())
            secuencia_destino.AddTrack(track)
