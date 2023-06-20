import unreal
# Definir la posición y rotación deseada de la cámara

# Cadena de valores
cadena = "X=85.763 Y=0.277 Z=708.182 P=-28.407657 Y=-4.580966 R=-0.264463"

# Extraer los valores de la cadena
valores = cadena.split()

# Obtener la posición de la cámara
camera_location = unreal.Vector(float(valores[0].split('=')[1]), float(valores[1].split('=')[1]), float(valores[2].split('=')[1]))

# Obtener la rotación de la cámara
camera_rotation = unreal.Rotator(float(valores[3].split('=')[1]), float(valores[4].split('=')[1]), float(valores[5].split('=')[1]))
unreal.EditorLevelLibrary.set_level_viewport_camera_info(camera_location, camera_rotation)
