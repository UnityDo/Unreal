import unreal

# Obtener el esqueleto seleccionado en el editor

skel_mesh = unreal.EditorUtilityLibrary.get_selected_assets()[0]



# optiene el modificador
skeleton_modifier_source = unreal.SkeletonModifier()
# Establece la malla esquelética
skeleton_modifier_source.set_skeletal_mesh(skel_mesh)

# Obtener la lista de todos los nombres de los huesos del esqueleto
bone_names = skeleton_modifier_source.get_all_bone_names()

# Ruta a la malla esquelética
mesh_path = "/Game/Mario/Mario_sinpuntos_SkelMesh"

# Carga la malla esquelética
asset_editor = unreal.EditorAssetLibrary()
skel_mesh_target = asset_editor.load_asset(mesh_path)
skeleton_modifier_target = unreal.SkeletonModifier()
skeleton_modifier_target.set_skeletal_mesh(skel_mesh_target)
print(bone_names)

# Iterar sobre cada nombre de hueso
for bone_name in bone_names:
  parent_name=skeleton_modifier.get_parent_name(bone_name)
  transform=skeleton_modifier.get_bone_transform(bone_name,False)
  skeleton_modifier_target.add_bone(bone_name, parent_name, transform)

skeleton_modifier_target.commit_skeleton_to_skeletal_mesh()

