import os
from PIL import Image
import numpy as np

class ImageInfoNode:
    """
    A simple node that retrieves basic information from an input image
    """
    
    # Define node's basic information
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),  # Input image
            }
        }
    
    RETURN_TYPES = ("STRING",)  # Output a string
    FUNCTION = "get_image_info"  # Processing function name
    
    CATEGORY = "image"  # Node category
    TITLE = "Image Info"  # Node title
    DESCRIPTION = "Get basic information from the input image"  # Node description
    
    def get_image_info(self, image):
        # Convert numpy array to PIL Image
        # Image format in ComfyUI is [batch, height, width, channels]
        pil_image = Image.fromarray(np.clip(image[0] * 255., 0, 255).astype(np.uint8))
        
        # Get image information
        width, height = pil_image.size
        mode = pil_image.mode
        format = pil_image.format if pil_image.format else "Unknown"
        
        # Build information string
        info = f"""Image Information:
- Size: {width}x{height}
- Color Mode: {mode}
- Format: {format}
- Memory Size: {image.nbytes / (1024*1024):.2f}MB"""
        
        return (info,)  # Return value must be a tuple

# This dictionary will be imported in __init__.py for node registration
NODE_CLASS_MAPPINGS = {
    "ImageInfo": ImageInfoNode
}

# Node display names
NODE_DISPLAY_NAME_MAPPINGS = {
    "ImageInfo": "Image Info"
} 