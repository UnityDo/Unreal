import unreal

# Crear un Personaje Character

# Crear una nueva clase Blueprint
blueprint_factory = unreal.BlueprintFactory()
blueprint_factory.set_editor_property("parent_class", unreal.Character)

# Establecer el nombre y la ruta del Blueprint
blueprint_name = "Personaje1"
blueprint_path = "/Game/Blueprints"

# Crear el Blueprint
new_blueprint = unreal.AssetToolsHelpers.get_asset_tools().create_asset(blueprint_name, blueprint_path, unreal.Blueprint, blueprint_factory)

#Crea un AI Controller



blueprint_factory_controller = unreal.BlueprintFactory()
blueprint_factory_controller.set_editor_property("parent_class", unreal.AIController)
