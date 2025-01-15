# ComfyUI Node Sample

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