# ComfyUI Node Sample

[English](README.md) | [中文](README.zh-CN.md)

A simple ComfyUI node example project to help beginners learn how to develop ComfyUI nodes.

## Features

The project contains a simple example node `ImageInfoNode` that:
- Accepts an input image
- Outputs basic information about the image (size, format, etc.)

## Installation

### Method 1: Manual Installation
1. Locate your ComfyUI custom nodes directory (usually at `ComfyUI/custom_nodes/`)
2. Clone this project in that directory:
```bash
cd custom_nodes
git clone https://github.com/yourusername/ComfyUI-NodeSample
```

### Method 2: Install via ComfyUI Manager
1. Open ComfyUI
2. Open ComfyUI Manager
3. Go to "Install Custom Nodes" tab
4. Search for "ComfyUI Node Sample"
5. Click Install

## Dependencies Management

This project demonstrates how to properly manage dependencies in your ComfyUI custom nodes.

### Method 1: Using requirements.txt
1. Create a `requirements.txt` file in your project root:
```txt
Pillow>=9.0.0
numpy>=1.21.0
```
ComfyUI Manager will automatically install these dependencies when users install your node.

### Method 2: Using install.py
For more complex dependency management:

1. Create an `install.py` script in your project root:
```python
import os
import subprocess
import sys

def ensure_dependencies():
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Get Python executable path from ComfyUI's environment
    python = sys.executable
    
    print("Installing dependencies...")
    
    # Install dependencies using pip in the correct Python environment
    subprocess.check_call([python, '-m', 'pip', 'install', '-r', 
                          os.path.join(script_dir, 'requirements.txt')])

if __name__ == "__main__":
    ensure_dependencies()
```

### Best Practices for Dependency Management
1. **Version Specification**:
   - Always specify minimum version requirements
   - Use `>=` for minimum version requirements
   - Example: `Pillow>=9.0.0`

2. **Dependency Isolation**:
   - Use ComfyUI's Python environment
   - Don't modify system-wide Python packages
   - Test your dependencies with different ComfyUI versions

3. **Conflict Prevention**:
   - Check for existing dependencies in ComfyUI
   - Use compatible versions with ComfyUI's requirements
   - Document any potential conflicts

4. **Error Handling**:
   - Add proper error messages for missing dependencies
   - Provide troubleshooting steps in documentation
   - Example code for checking dependencies:
```python
try:
    import PIL
    import numpy as np
except ImportError:
    print("Required dependencies are not installed. Please install them using:")
    print("pip install -r requirements.txt")
```

## Usage

1. Start ComfyUI
2. Find "Image Info" node in the node list
3. Connect an image node to the Image Info node's input
4. Run the workflow to see the image information

## Development Guide

This project demonstrates the basic structure of creating a ComfyUI node, including:
- Node class definition
- Input/output interface definition
- Node registration process

You can use this template to develop your own nodes.

## Publishing to ComfyUI Manager

To make your node available in ComfyUI Manager:

1. Create a GitHub repository for your node
2. Add a `ComfyUI` tag to your repository
3. Create a custom_nodes.json file in your repository root:
```json
{
    "your_node_name": {
        "title": "Your Node Title",
        "description": "A brief description of your node",
        "tags": ["image", "utility"],
        "repository": "github_username/repository_name",
        "install_type": "git_clone"
    }
}
```
4. Submit your repository to the [ComfyUI Manager Custom Nodes List](https://github.com/ltdrdata/ComfyUI-Manager/blob/main/custom-node-list.json) via pull request 