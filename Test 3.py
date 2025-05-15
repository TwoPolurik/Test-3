import math

def is_object_in_camera_view(camera_position, camera_direction, object_position, camera_fov):
    """
    Определяет, попадает ли объект в поле зрения камеры.

    Args:
        camera_position: (x, y) - позиция камеры.
        camera_direction: (dx, dy) - единичный вектор направления взгляда камеры.
        object_position: (x, y) - позиция объекта.
        camera_fov: Угол обзора камеры в градусах.

    Returns:
        True, если объект в поле зрения камеры, False - в противном случае.
    """

    # 1. Вычислить вектор от камеры к объекту
    vector_to_object = (object_position[0] - camera_position[0], object_position[1] - camera_position[1])

    # 2. Найти угол между направлением камеры и вектором к объекту
    dot_product = camera_direction[0] * vector_to_object[0] + camera_direction[1] * vector_to_object[1]
    magnitude_camera_direction = math.sqrt(camera_direction[0]**2 + camera_direction[1]**2)
    magnitude_vector_to_object = math.sqrt(vector_to_object[0]**2 + vector_to_object[1]**2)

    # Check for zero magnitude to prevent division by zero
    if magnitude_camera_direction == 0 or magnitude_vector_to_object == 0:
        return False  # Or raise an exception, depending on the desired behavior

    cosine_angle = dot_product / (magnitude_camera_direction * magnitude_vector_to_object)
    angle_radians = math.acos(cosine_angle)
    angle_degrees = math.degrees(angle_radians)

    # 3. Если угол меньше или равен α / 2, объект находится в поле зрения
    return angle_degrees <= camera_fov / 2


# Входные данные
camera_position = (0, 0)
camera_direction = (1, 0)
object_position = (2, 1)
camera_fov = 60

# Проверяем, видит ли камера объект
if is_object_in_camera_view(camera_position, camera_direction, object_position, camera_fov):
    print("Объект в поле зрения камеры")
else:
    print("Объект вне поля зрения камеры")