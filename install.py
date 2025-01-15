import os
import subprocess
import sys

def ensure_dependencies():
    """Ensure all dependencies are installed in the correct Python environment"""
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Get Python executable path from ComfyUI's environment
    python = sys.executable
    
    print("Installing dependencies...")
    
    try:
        # Install dependencies using pip in the correct Python environment
        subprocess.check_call([python, '-m', 'pip', 'install', '-r', 
                             os.path.join(script_dir, 'requirements.txt')])
        print("Dependencies installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        print("Please try installing them manually using:")
        print(f"'{python} -m pip install -r requirements.txt'")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    ensure_dependencies() 