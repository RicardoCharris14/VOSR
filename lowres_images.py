import os
from PIL import Image

gt_dir = "preset/datasets/test_gt"
lr_dir = "preset/datasets/test_lr"
os.makedirs(lr_dir, exist_ok=True)

for fname in os.listdir(gt_dir):
    if fname.lower().endswith((".jpg")):
        img = Image.open(os.path.join(gt_dir, fname)).convert("RGB")
        # Reducción bicúbica x4 (1024 -> 256)
        w, h = img.size
        img_lr = img.resize((w // 4, h // 4), Image.BICUBIC)
        img_lr.save(os.path.join(lr_dir, fname))