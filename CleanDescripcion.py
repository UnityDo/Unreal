import unreal

# Obtén la referencia al asset
#asset = unreal.load_asset("/Game/Blueprints/Systems/InventorySystem/Items/Clues/Page1/DAP_P_C_1.DAP_P_C_1")

table_base = unreal.Name("/Game/String_Tables/ST_Text.ST_Text")
selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()

# Itera sobre los assets seleccionados
for asset in selected_assets:
    # Haz algo con cada asset
    print(asset.get_name())

   
    asset.set_editor_property("Descripcion", "")


# Guarda los cambios en el asset
unreal.EditorAssetLibrary.save_loaded_asset(asset)
