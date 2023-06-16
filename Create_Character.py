import unreal

# Crear un Personaje Character

# Crear una nueva clase Blueprint
blueprint_factory = unreal.BlueprintFactory()
blueprint_factory.set_editor_property("parent_class", unreal.Character)

# Establecer el nombre y la ruta del Blueprint
blueprint_name = "Personaje1"
blueprint_path = "/Game/Blueprints/NPC"

# Crear el Blueprint
new_blueprint = unreal.AssetToolsHelpers.get_asset_tools().create_asset(blueprint_name, blueprint_path, unreal.Blueprint, blueprint_factory)

#Crea un AI Controller



blueprint_factory_controller = unreal.BlueprintFactory()
blueprint_factory_controller.set_editor_property("parent_class", unreal.AIController)

# Establecer el nombre y la ruta del Blueprint
blueprint_name_controller = "AI_Personaje1"
blueprint_path_controller = "/Game/Blueprints/NPC"

# Crear el Blueprint
new_blueprint = unreal.AssetToolsHelpers.get_asset_tools().create_asset(blueprint_name_controller , blueprint_path_controller, unreal.Blueprint, blueprint_factory_controller)


#Crea un Behaviour Tree

blueprint_factory_controller = unreal.BlueprintFactory()
blueprint_factory_controller.set_editor_property("parent_class", unreal.AIController)

# Establecer el nombre y la ruta del Blueprint
blueprint_name_controller = "AI_Personaje1"
blueprint_path_controller = "/Game/Blueprints/NPC"

# Crear el Blueprint
new_blueprint = unreal.AssetToolsHelpers.get_asset_tools().create_asset(blueprint_name_controller , blueprint_path_controller, unreal.Blueprint, blueprint_factory_controller)


blueprint_factory_behavior = unreal.BehaviorTreeFactory()
# Obtener la instancia de Asset Tools
asset_tools = unreal.AssetToolsHelpers.get_asset_tools()

# Crear un nuevo Behavior Tree
behavior_tree = asset_tools.create_asset("BTT_Personaje", "/Game/Blueprints/NPC", unreal.BehaviorTree, blueprint_factory_controller)


