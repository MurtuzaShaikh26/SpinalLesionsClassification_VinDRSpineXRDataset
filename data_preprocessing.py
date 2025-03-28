"""Description: Handles data loading, augmentation, and preprocessing of spinal X-ray images for model training.

Functions:
SpineXRayDataset: Custom dataset class for loading images and labels.
load_image(path): Loads an image from the given path.
get_dataloader(batch_size): Returns a DataLoader with transformations and batching."""