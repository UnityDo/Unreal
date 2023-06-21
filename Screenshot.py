import unreal

# Obtener el mundo actual del viewport
viewport = unreal.Viewport()

# Obtener la posición y rotación de la cámara actual
camera_location = viewport.get_view_location()
camera_rotation = viewport.get_view_rotation()

# Crear una cámara en la posición actual del mundo y mirando hacia donde se esté mirando
camera = unreal.CineCameraActor(viewport.get_viewport_world())
camera.set_actor_location(camera_location)
camera.set_actor_rotation(camera_rotation)
file_path = "/Game/Screenshots/screenshot.png"
# Hacer una captura de la cámara creada
unreal.AutomationLibrary.take_high_res_screenshot(1920, 1080, file_path, camera=camera)
