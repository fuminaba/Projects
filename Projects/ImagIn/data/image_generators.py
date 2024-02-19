'''Defines generator functions to generate/load image data.

'''
import numpy as np
from scipy import ndimage 
from typing import Generator

def infer_rotation_axes(
    image: np.ndarray
) -> tuple:
    image_dims = image.shape
    rotation_axes = ((0, 1) 
                     if 1 < len(image_dims) <= 3
                     else (1,2) 
                     if len(image_dims) == 4
                     else None)
    
    # >>> Check dimensions and rotation axes <<< #
    try:
        assert not (rotation_axes is None)
    except AssertionError:
        raise AssertionError(f"Incompatible image dimensions: {image_dims}")

    return rotation_axes

def rot90_generator(
    image: np.ndarray,
    rotation_k: list = None
) -> Generator[np.ndarray]:
    '''Generator function for 90 degree rotations

    Args:
        image (np.ndarray) - A 2 to 4D matrix of an image. Should be in the 
            format of [batch_size, height, width, channels]
        
    
    '''
    # >>> Number of 90 degree rotations <<< #
    rotation_k = [0, 1, 2, 3] if rotation_k is None else rotation_k

    # >>> Check dims of image <<< #
    rotation_axes = infer_rotation_axes(image)
    
    # >>> Yield rotations <<< #
    for k_rot in rotation_k:
        yield np.rot90(image, k = k_rot, axes = rotation_axes)
    
def angular_rotation_generator(
    image: np.ndarray,
    rotation_angles: list[int] = [15, 30, 45],
    add_90deg_offsets: int = 0
) -> Generator[np.ndarray]:
    '''Rotates the image by the angles provided to function.

    Args:
        image (np.ndarray): A 2-4D matrix of the image in the format
            [batch, height, width, channels] or [height, width, channels]
        rotation_angles (list): A list of angles to rotate the matrix by. The
            angles are integers in degrees
        add_90deg_offsets (int): Adds 90 degree offsets to each rotation angle. 
            Value should be 0-3. Value of 0 adds no 90 degree offsets, whereas
            for each increment in this argument value adds one 90 degree offset.
            
    Example:
        # Yields im_matrix rotated by 15, (90 + 15), (180 + 15), (270 + 15) degs
        >>> angular_rotation_generator(im_matrix, [15], 3)
    '''
    # >>> 90 degree offsets <<< #
    offset_images = (
        [np.rot90(image, k = offset) for offset in range(add_90deg_offsets)]
        if add_90deg_offsets >= 1
        else [image]
    )
    
    rotation_angles = ([0] + rotation_angles 
                       if rotation_angles[0] != 0 
                       else rotation_angles)
    
    rotation_axes = infer_rotation_axes(image)

    # >>> 90 degree offset iteration <<< #
    for offset_image in offset_images: 
        # >>> Angular Rotations <<< #
        for angle in rotation_angles:
            rotated_image = ndimage.rotate(offset_image, 
                                           angle = angle, 
                                           axes = rotation_axes, 
                                           mode = 'nearest')
            yield rotated_image