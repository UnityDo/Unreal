import unreal

# Obtén la referencia al asset
asset = unreal.load_asset("/Game/Blueprints/Systems/InventorySystem/Items/Clues/Page1/DAP_P_C_1.DAP_P_C_1")

table_base = unreal.Name("/Game/String_Tables/ST_Voices.ST_Voices")
selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()

# Itera sobre los assets seleccionados
for asset in selected_assets:
    # Haz algo con cada asset
    print(asset.get_name())

    # Coge el text ya guardado y sacamos el key
    texto = asset.get_editor_property('Text')
    tupla = unreal.TextLibrary.string_table_id_and_key_from_text(texto)
    out_table_id, out_key = tupla

    print("externa")
    print(out_table_id)
    print(out_key)

    # Coge el text ya guardado y sacamos el key
    new_text = unreal.TextLibrary.text_from_string_table(table_base, out_key)
    print(new_text)
    asset.set_editor_property("Text", "")
    asset.set_editor_property("Text", new_text)

# Guarda los cambios en el asset
unreal.EditorAssetLibrary.save_loaded_asset(asset)
