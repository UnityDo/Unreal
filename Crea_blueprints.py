import unreal

def make_blueprint_small(asset_name, package_path):
    factory = unreal.BlueprintFactory()
    factory.set_editor_property("parent_class", unreal.Actor)
    
    # Crear el Blueprint
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    blueprint = asset_tools.create_asset(asset_name, package_path, None, factory)
    
    # Agregar componentes al Blueprint
    root_component = blueprint.simple_construct_default_scene_root()    
    # Guardar el Blueprint
    unreal.EditorAssetLibrary.save_asset(package_path + "/" + asset_name)

# Nombres de los Blueprints
blueprint_names = ["Devil", "Justice", "Magician", "Priestess", "Death"]

# Carpeta donde se guardarán los Blueprints
package_path = "/Game/Blueprints/Interactives/Puzzles/Automatons/"

# Recorrer los nombres y crear los Blueprints
for name in blueprint_names:
    # Nombre del Blueprint
    blueprint_name = f"BP_Body_{name}"
    
    # Crear el Blueprint
    make_blueprint_small(blueprint_name, package_path)
    
    print(f"Blueprint '{blueprint_name}' creado y guardado en '{package_path}/{blueprint_name}'")
