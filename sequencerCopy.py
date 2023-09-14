import unreal

# Obtén las referencias a las secuencias de nivel

secuencia_origen = unreal.LevelSequence.cast(unreal.load_asset('/Game/Cinematics/Takes/2023-09-14/SQ_TestCopy.SQ_TestCopy'))
secuencia_destino = unreal.LevelSequence.cast(unreal.load_asset('/Game/Cinematics/Takes/2023-09-14/SQ_TestPaste.SQ_TestPaste'))

# Asegúrate de que ambas secuencias existen
if not secuencia_origen or not secuencia_destino:
    print("No se pudo encontrar una o ambas secuencias de nivel.")
else:
    # Copia todos los tracks de la secuencia origen a la secuencia destino
    for track_origen in secuencia_origen.get_master_tracks():
        track_destino = secuencia_destino.add_master_track(type(track_origen))

        # Copia todos los fotogramas de cada track
        for row_origen in track_origen.get_rows():
            row_destino = track_destino.add_row()

            for key_origen in row_origen.get_keys():
                time = key_origen.get_time()
                value = key_origen.get_value()
                key_destino = row_destino.add_key(time)
                key_destino.set_value(value)

    print("Se han copiado todos los tracks y fotogramas.")
