import unreal

# Obtén la referencia al asset
table_base = unreal.Name("/Game/String_Tables/ST_Text.ST_Text")
selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()

# Itera sobre los assets seleccionados
for asset in selected_assets:
    # Haz algo con cada asset
    print(asset.get_name())

    # Coge el text ya guardado y sacamos el key
    texto_chap = asset.get_editor_property('Chapter')
    texto_name = asset.get_editor_property('NameOfTheLevel')
    texto_long = asset.get_editor_property('Longdescription')
    texto_places = asset.get_editor_property('Places')

    tupla = unreal.TextLibrary.string_table_id_and_key_from_text(texto_chap)
    tupla2 = unreal.TextLibrary.string_table_id_and_key_from_text(texto_name)
    
    if texto_long and not texto_long.is_empty():
        tupla3 = unreal.TextLibrary.string_table_id_and_key_from_text(texto_long)
        out_table_id3, out_key3 = tupla3
        new_text3 = unreal.TextLibrary.text_from_string_table(table_base, out_key3)
        asset.set_editor_property("Longdescription", "")
        asset.set_editor_property("Longdescription", new_text3)
    tupla4 = unreal.TextLibrary.string_table_id_and_key_from_text(texto_places)

    out_table_id, out_key = tupla
    out_table_id2, out_key2 = tupla2
   
    out_table_id4, out_key4 = tupla4

    # Coge el text ya guardado y sacamos el key
    new_text = unreal.TextLibrary.text_from_string_table(table_base, out_key)
    new_text2 = unreal.TextLibrary.text_from_string_table(table_base, out_key2)
   
    new_text4 = unreal.TextLibrary.text_from_string_table(table_base, out_key4)

    print(new_text)

    asset.set_editor_property("Chapter", "")
    asset.set_editor_property("Chapter", new_text)
    asset.set_editor_property("NameOfTheLevel", "")
    asset.set_editor_property("NameOfTheLevel", new_text2)

    asset.set_editor_property("Places", "")
    asset.set_editor_property("Places", new_text4)

# Guarda los cambios en el asset
unreal.EditorAssetLibrary.save_loaded_asset(asset)
