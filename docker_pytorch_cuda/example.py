import torch
import cv2
import open3d as o3d

# Print the versions of the libraries
print("PyTorch Version:", torch.__version__)
print("OpenCV Version:", cv2.__version__)
print("Open3D Version:", o3d.__version__)

# Check if CUDA is available
if torch.cuda.is_available():
    print("CUDA is available")
    print("CUDA Version:", torch.version.cuda)
    print("GPU Name:", torch.cuda.get_device_name(0))
else:
    print("CUDA is not available")
