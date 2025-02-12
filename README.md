# Squirtle Counting with Image Segmentation

### Overview

This project focuses on counting the number of Squirtle Pokémon present in images using image segmentation techniques. The dataset for this task is located in the `pictures1` folder, and the correct Squirtle counts for each image are provided in `squirtle_count.csv`. The goal is to develop an algorithm that achieves the lowest possible Mean Absolute Error (MAE) while maintaining a generic approach.

### Objective

- Count the number of Squirtles in each image.
- Ensure the solution is **generic**, meaning the same operations are applied to all images.

---

## Project Structure

```
📂 Pokemon-Counting
 ├── 📂 pictures1               # Folder containing images
 ├── 📝 squirtle_count.csv      # CSV file with correct Squirtle counts per image
 ├── 📜 SC23-G3-RA-186-2020.py  # Main Python script for segmentation & counting
 ├── 📜 README.md               # Project documentation
```

---

## Requirements

To run this project, ensure you have the following dependencies installed:

```bash
pip install numpy opencv-python matplotlib scikit-learn
```

---

## How to Run

1. Open a terminal and navigate to the project directory:
   ```bash
   cd Pokemon-Counting
   ```
2. Run the script with the image directory as an argument:
   ```bash
   python SC23-G3-RA-186-2020.py pictures1
   ```

---

## Implementation Details

- The program reads images from `pictures1` and processes them using **OpenCV**.
- **Preprocessing techniques** include:
  - Conversion to grayscale
  - Thresholding for segmentation
  - Morphological operations (dilation and erosion) to refine segmentation
- Contours are extracted and filtered based on size to count Squirtles.
- The results are compared with `squirtle_count.csv`, and the **Mean Absolute Error (MAE)** is calculated.

---

## Example Output

```
image1.jpg - Actual: 5 - Predicted: 6
image2.jpg - Actual: 4 - Predicted: 4
...
Mean Absolute Error (MAE): 1.8
```

---

## Results & Optimization

- The segmentation thresholds were fine-tuned to ensure accurate object detection.
- Various thresholding techniques and contour filtering criteria were tested to minimize MAE.
- The final implementation achieves a **MAE < 1**, meeting the highest accuracy criteria.

---

## Future Improvements

- Experiment with **deep learning-based** object detection models (e.g., YOLO, Faster R-CNN).
- Optimize morphological operations for better segmentation under varying lighting conditions.
- Use adaptive thresholding for more robust preprocessing.

---

## Author

- **Katarina Perović**

---

## License

This project is for educational purposes only and follows the guidelines set for the Soft Computing 2023/24 course.

