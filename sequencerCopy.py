import unreal

# Obtén las referencias a las secuencias de nivel
# Necesita que los dos sequencers tengan los mismos bindings metidos
secuencia_origen = unreal.load_asset("/Game/Sequencer/Test/CopyPaste/SQ_Copy.SQ_Copy")
secuencia_destino = unreal.load_asset("/Game/Sequencer/Test/CopyPaste/SQ_Paste.SQ_Paste")

binds_origen = secuencia_origen.get_bindings() 
binds_destino = secuencia_destino.get_bindings()

# Asegúrate de que ambas secuencias existen
if not secuencia_origen or not secuencia_destino:
    print("No se pudo encontrar una o ambas secuencias de nivel.")
else:
    # Copia todos los bindings y tracks de la secuencia origen a la secuencia destino
    for bind_origen, bind_destino in zip(binds_origen, binds_destino):
        if bind_origen.get_name() == bind_destino.get_name():
            for track_origen, track_destino in zip(bind_origen.get_tracks(), bind_destino.get_tracks()):
                # Copia los fotogramas del track origen al track destino
                    for section_origen, section_destino in zip(track_origen.get_sections(), track_destino.get_sections()):
                        for channel_origen, channel_destino in zip(section_origen.get_all_channels(), section_destino.get_all_channels()):
                            for key in channel_origen.get_keys():
                            # Crea un nuevo fotograma en el canal destino
                                new_key = channel_destino.add_key(key.get_time().get_editor_property("frame_number"), key.get_value())
                            

    # Guarda los cambios en la secuencia destino
    unreal.EditorAssetLibrary.save_loaded_asset(secuencia_destino)

    print("Se han copiado todos los fotogramas de transformación de secuencia_origen a secuencia_destino.")
