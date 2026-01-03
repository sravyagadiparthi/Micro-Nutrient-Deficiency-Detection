import os
import shutil
import random

# Set seed for reproducibility
random.seed(42)

# Paths
source_dir = "Augmented Images of Nutrient Deficient Banana Leaves"
output_dir = "dataset"
train_ratio = 0.8  # 80% for training, 20% for validation

# Create output directories
train_dir = os.path.join(output_dir, "train")
val_dir = os.path.join(output_dir, "validation")
os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)

# Loop through each class folder
for class_name in os.listdir(source_dir):
    class_path = os.path.join(source_dir, class_name)
    if not os.path.isdir(class_path):
        continue

    # List all image files
    images = [f for f in os.listdir(class_path) if os.path.isfile(os.path.join(class_path, f))]
    random.shuffle(images)

    # Split images
    split_index = int(len(images) * train_ratio)
    train_images = images[:split_index]
    val_images = images[split_index:]

    # Create class folders in train and validation directories
    train_class_dir = os.path.join(train_dir, class_name)
    val_class_dir = os.path.join(val_dir, class_name)
    os.makedirs(train_class_dir, exist_ok=True)
    os.makedirs(val_class_dir, exist_ok=True)

    # Copy training images
    for img in train_images:
        src = os.path.join(class_path, img)
        dst = os.path.join(train_class_dir, img)
        shutil.copy2(src, dst)

    # Copy validation images
    for img in val_images:
        src = os.path.join(class_path, img)
        dst = os.path.join(val_class_dir, img)
        shutil.copy2(src, dst)

    print(f"✅ {class_name}: {len(train_images)} train, {len(val_images)} validation")

print("\n🎉 Dataset split complete!")
