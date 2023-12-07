import unreal
import pickle

# Obtener el esqueleto seleccionado en el editor

skeleton = unreal.EditorUtilityLibrary.get_selected_assets()[0]

# Crear un diccionario vacío para almacenar la información del esqueleto
skeleton_data = {}

# optiene el modificador
skeleton_modifier = unreal.SkeletonModifier()

# Obtener la lista de todos los nombres de los huesos del esqueleto
bone_names = skeleton_modifier.get_all_bone_names()

# Iterar sobre cada nombre de hueso
for bone_name in bone_names:
    # Obtener la transformación del hueso en el espacio del esqueleto
    bone_transform = skeleton.get_bone_transform(bone_name, unreal.Skeleton.BoneSpace.SKELETON)
    # Obtener el nombre del hueso padre, si existe
    parent_bone = skeleton.get_parent_bone(bone_name)
    # Guardar la información del hueso en el diccionario, usando el nombre del hueso como clave
    skeleton_data[bone_name] = {"transform": bone_transform, "parent": parent_bone}

# Abrir un archivo en modo escritura binaria
with open("C:/Users/Usuario/Documents/Unreal Projects/Adventcode2023/Content/Data/skeleton_data.pkl", "wb") as file:
    # Serializar el diccionario y guardarlo en el archivo
    pickle.dump(skeleton_data, file)

