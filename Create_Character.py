import unreal

# Obtener el paquete de nivel actual
current_level = unreal.EditorLevelLibrary().get_editor_world().get_current_level()

# Crear una nueva clase Blueprint
blueprint_factory = unreal.BlueprintFactory()
blueprint_factory.set_editor_property("parent_class", unreal.Character)

# Establecer el nombre y la ruta del Blueprint
blueprint_name = "Personaje1"
blueprint_path = "/Game/Blueprints"

# Crear el Blueprint
new_blueprint = unreal.AssetToolsHelpers.get_asset_tools().create_asset(blueprint_name, blueprint_path, unreal.Blueprint, blueprint_factory)

# Asignar el nuevo Blueprint al paquete de nivel actual
unreal.EditorLevelLibrary().replace_actor_with_blueprint(current_level, new_blueprint.get_editor_property("generated_class"), unreal.Transform(), unreal.EditorReplaceActorOptions(keep_scale=True))
