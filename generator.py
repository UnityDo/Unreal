import unreal


def spawnActor(times, separationx,separationy):
    obj = unreal.load_asset( "/Game/Geometry/Meshes/1M_Cube.1M_Cube")
   
    for x in range(6):
        actor_location = unreal.Vector(separationx*x,separationy*x,0.0)
        actor_rotation = unreal.Rotator(0.0,0.0,0.0)
        unreal.EditorLevelLibrary.spawn_actor_from_object(obj, actor_location, actor_rotation)

spawnActor(5)
