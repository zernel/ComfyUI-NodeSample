# ComfyUI Node Sample

这是一个简单的 ComfyUI 节点示例项目，用于帮助初学者学习如何开发 ComfyUI 节点。

## 功能特点

项目包含一个简单的示例节点 `ImageInfoNode`，它可以：
- 接收一张输入图片
- 输出该图片的基本信息（尺寸、格式等）

## 安装方法

### 方法一：手动安装
1. 找到你的 ComfyUI 自定义节点目录（通常在 `ComfyUI/custom_nodes/`）
2. 在该目录下克隆本项目：
```bash
cd custom_nodes
git clone https://github.com/yourusername/ComfyUI-NodeSample
```

### 方法二：通过 ComfyUI Manager 安装
1. 打开 ComfyUI
2. 打开 ComfyUI Manager
3. 进入 "Install Custom Nodes" 标签页
4. 搜索 "ComfyUI Node Sample"
5. 点击安装

## 依赖管理

本项目演示了如何正确管理 ComfyUI 自定义节点的依赖。

### 方法一：使用 requirements.txt
1. 在项目根目录创建 `requirements.txt` 文件：
```txt
Pillow>=9.0.0
numpy>=1.21.0
```
当用户通过 ComfyUI Manager 安装你的节点时，这些依赖会被自动安装。

### 方法二：使用 install.py
对于更复杂的依赖管理：

1. 在项目根目录创建 `install.py` 脚本：
```python
import os
import subprocess
import sys

def ensure_dependencies():
    # 获取脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 从 ComfyUI 环境获取 Python 可执行文件路径
    python = sys.executable
    
    print("正在安装依赖...")
    
    # 在正确的 Python 环境中使用 pip 安装依赖
    subprocess.check_call([python, '-m', 'pip', 'install', '-r', 
                          os.path.join(script_dir, 'requirements.txt')])

if __name__ == "__main__":
    ensure_dependencies()
```

### 依赖管理最佳实践
1. **版本指定**：
   - 始终指定最低版本要求
   - 使用 `>=` 指定最低版本要求
   - 示例：`Pillow>=9.0.0`

2. **依赖隔离**：
   - 使用 ComfyUI 的 Python 环境
   - 不要修改系统级 Python 包
   - 在不同 ComfyUI 版本中测试你的依赖

3. **冲突预防**：
   - 检查 ComfyUI 中已存在的依赖
   - 使用与 ComfyUI 要求兼容的版本
   - 在文档中说明潜在的冲突

4. **错误处理**：
   - 为缺失的依赖添加适当的错误信息
   - 在文档中提供故障排除步骤
   - 依赖检查示例代码：
```python
try:
    import PIL
    import numpy as np
except ImportError:
    print("必需的依赖未安装。请使用以下命令安装：")
    print("pip install -r requirements.txt")
```

## 使用方法

1. 启动 ComfyUI
2. 在节点列表中找到 "Image Info" 节点
3. 将图片节点连接到 Image Info 节点的输入端
4. 运行工作流，查看输出的图片信息

## 开发指南

本项目展示了创建 ComfyUI 节点的基本结构，包括：
- 节点类的定义
- 输入输出接口的定义
- 节点的注册方式

你可以基于这个模板开发自己的节点。

## 发布到 ComfyUI Manager

要将你的节点发布到 ComfyUI Manager：

1. 为你的节点创建一个 GitHub 仓库
2. 为仓库添加 `ComfyUI` 标签
3. 在仓库根目录创建 custom_nodes.json 文件：
```json
{
    "your_node_name": {
        "title": "你的节点标题",
        "description": "节点的简要描述",
        "tags": ["image", "utility"],
        "repository": "github用户名/仓库名",
        "install_type": "git_clone"
    }
}
```
4. 通过 Pull Request 将你的仓库提交到 [ComfyUI Manager Custom Nodes List](https://github.com/ltdrdata/ComfyUI-Manager/blob/main/custom-node-list.json) 