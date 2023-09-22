import unreal

table_base = unreal.Name("/Game/String_Tables/ST_Voices.ST_Voices")
selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()

# Itera sobre los assets seleccionados
for asset in selected_assets:
    # Haz algo con cada asset
    print(asset.get_name())

    # Coge el text ya guardado y sacamos el key
    texto = asset.get_editor_property('FrontText')
    tupla = unreal.TextLibrary.string_table_id_and_key_from_text(texto)
    out_table_id, out_key = tupla

    print("externa")
    print(out_table_id)
    print(out_key)

    # Coge el text ya guardado y sacamos el key
    new_text = unreal.TextLibrary.text_from_string_table(table_base, out_key)
    print(new_text)
    asset.set_editor_property("FrontText", "")
    asset.set_editor_property("FrontText", new_text)
    
    # Subtitulos
    subtitulos = asset.get_editor_property("Subtitulos")
    
    if len(subtitulos) > 0:
        subtitulo =  asset.get_editor_property("Subtitulos")[0].get_editor_property("Texto")
        asset.set_editor_property(unreal.Text(subtitulo), new_text)

# Guarda los cambios en el asset
unreal.EditorAssetLibrary.save_loaded_asset(asset)
