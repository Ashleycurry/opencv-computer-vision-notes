# OpenCV Computer Vision Learning Notes

[中文](README.md) | [English](README-English.md)

This repository organizes introductory OpenCV and computer vision learning materials. The course starts with image and video loading, display, and drawing, then covers pixel operations, color-space conversion, geometric transformations, image smoothing, edge detection, morphology, thresholding, contour analysis, feature matching, and corner detection.

Course materials are stored in `docs/`, and the corresponding examples are stored in `src/`. Each chapter uses an English directory name for source code, with links pointing to the actual scripts and sample images in the repository.

## Materials and Environment

- Course materials: [docs](docs)
- Example source: [src](src)
- Material collection: 12 PDF files, 121 pages in total
- Language: Python 3
- Core libraries: OpenCV and NumPy
- Visualization library: Matplotlib
- Execution model: standalone Python scripts and OpenCV GUI windows
- Camera examples: require an available local camera

## Learning Roadmap

```text
Input and Display
    -> Image loading, video loading, and camera access
    -> OpenCV windows, keyboard events, and resource cleanup
            |
            v
Image Fundamentals
    -> Geometric shapes and text drawing
    -> Pixel access, image properties, and channel operations
    -> BGR, GRAY, HSV, Lab, and YCrCb
            |
            v
Image Processing
    -> Scaling, translation, rotation, perspective, and remapping
    -> Mean, Gaussian, and median filtering
    -> Canny edge detection
    -> Erosion, dilation, opening, closing, top-hat, and black-hat
            |
            v
Object Analysis
    -> Global, adaptive, and Otsu thresholding
    -> Contours, moments, convex hulls, and bounding rectangles
    -> ORB features and BF/FLANN matching
    -> Harris corner detection
```

## Chapters and Source

| No. | Course material | Pages | Source directory | Main topics |
| --- | --- | ---: | --- | --- |
| 001 | [Image and Video Loading](docs/001-图片%26视频加载及展示.pdf) | 2 | [`001-image-video-io`](src/001-image-video-io) | Image loading, display, camera access, and video-frame processing |
| 002 | [Image Drawing](docs/002-图像的绘制方法.pdf) | 3 | [`002-image-drawing`](src/002-image-drawing) | Lines, rectangles, circles, polygons, and text |
| 003 | [Basic Image Operations](docs/003-图像的基础操作.pdf) | 2 | [`003-basic-image-operations`](src/003-basic-image-operations) | Pixel access, image properties, channel split/merge, and color conversion |
| 004 | [Color-Space Conversion](docs/004-图像处理——颜色空间转换.pdf) | 11 | [`004-color-space-conversion`](src/004-color-space-conversion) | GRAY, Lab, YCrCb, HSV, and related color spaces |
| 005 | [Geometric Transformations](docs/005-图像处理-几何变换.pdf) | 35 | [`005-geometric-transformation`](src/005-geometric-transformation) | Scaling, translation, rotation, perspective, and remapping |
| 006 | [Image Smoothing](docs/006-图像处理-平滑.pdf) | 11 | [`006-image-smoothing`](src/006-image-smoothing) | Noise, mean filtering, Gaussian filtering, and median filtering |
| 007 | [Edge Detection](docs/007-图像处理-边缘检测.pdf) | 9 | [`007-edge-detection`](src/007-edge-detection) | Edge-detection principles and the Canny algorithm |
| 008 | [Morphological Processing](docs/008-图像处理-形态学处理.pdf) | 13 | [`008-morphological-operations`](src/008-morphological-operations) | Erosion, dilation, opening, closing, top-hat, and black-hat |
| 009 | [Thresholding](docs/009-图像处理-阈值处理.pdf) | 8 | [`009-thresholding`](src/009-thresholding) | Global, adaptive, and Otsu thresholding |
| 010 | [Contours and Features](docs/010-图像处理-轮廓介绍及特征.pdf) | 13 | [`010-contours-and-features`](src/010-contours-and-features) | Contours, moments, polygon approximation, convex hulls, and bounding rectangles |
| 011 | [Feature Matching](docs/011-图像处理-特征匹配.pdf) | 7 | [`011-feature-matching`](src/011-feature-matching) | ORB features, brute-force matching, and FLANN nearest-neighbor matching |
| 012 | [Corner Detection](docs/012-图像处理-角点检测.pdf) | 7 | [`012-corner-detection`](src/012-corner-detection) | Corner concepts, detection intuition, and Harris corner detection |

## Example Reference

### 001 Image and Video I/O

- [`image_read.py`](src/001-image-video-io/image_read.py): reads an image with `cv.imread`, creates a window, and displays it.
- [`video_read.py`](src/001-image-video-io/video_read.py): captures camera frames with `cv.VideoCapture(0)`, exits on `q`, and releases the device.
- [`opencv.png`](src/001-image-video-io/opencv.png): input image for the image-loading example.

### 002 Image Drawing

- [`drawing.py`](src/002-image-drawing/drawing.py): draws lines, rectangles, circles, polylines, and text with `line`, `rectangle`, `circle`, `polylines`, and `putText`.
- [`test.jpg`](src/002-image-drawing/test.jpg): input image for the drawing example.

### 003 Basic Image Operations

- [`basic_operations.py`](src/003-basic-image-operations/basic_operations.py): accesses and modifies pixels, reads `shape`, `size`, and `dtype`, splits/merges BGR channels, and converts to HSV.
- [`test.jpg`](src/003-basic-image-operations/test.jpg): input image for the basic-operations example.

### 004 Color-Space Conversion

- [`color_conversion.py`](src/004-color-space-conversion/color_conversion.py): converts a BGR image to GRAY, Lab, YCrCb, and HSV and displays the results.
- [`img.jpg`](src/004-color-space-conversion/img.jpg): input image for the color-conversion example.

### 005 Geometric Transformations

The source directory contains the following transformation examples:

- [`Scale/Scale.py`](src/005-geometric-transformation/Scale/Scale.py): enlarges and reduces an image with `cv.resize`.
- [`Translation/Translation.py`](src/005-geometric-transformation/Translation/Translation.py): translates an image with an affine matrix.
- [`Revolve/Revolve.py`](src/005-geometric-transformation/Revolve/Revolve.py): rotates an image around its center and changes the scale.
- [`Perspective/Perspective.py`](src/005-geometric-transformation/Perspective/Perspective.py): computes a perspective transform from four corresponding point pairs.
- [`Remap/copy.py`](src/005-geometric-transformation/Remap/copy.py): maps output pixels to a selected location in the source image.
- [`Remap/copy_all.py`](src/005-geometric-transformation/Remap/copy_all.py): builds a complete coordinate map and performs remapping.
- [`Remap/x_rotation.py`](src/005-geometric-transformation/Remap/x_rotation.py): reverses the coordinate along the X direction.
- [`Remap/y_rotation.py`](src/005-geometric-transformation/Remap/y_rotation.py): reverses the coordinate along the Y direction.
- [`Remap/xy_rotation.py`](src/005-geometric-transformation/Remap/xy_rotation.py): reverses both X and Y coordinates.
- [`Remap/half_size.py`](src/005-geometric-transformation/Remap/half_size.py): demonstrates image compression through coordinate mapping.
- [`1.jpg`](src/005-geometric-transformation/Scale/1.jpg): input image for scaling; the other transformation directories also contain their own `1.jpg` inputs.

Additional chapter notes are available in [`readme.txt`](src/005-geometric-transformation/readme.txt).

### 006 Image Smoothing

- [`filtering.py`](src/006-image-smoothing/filtering.py): applies mean, Gaussian, and median filters to a noisy image and compares the results with Matplotlib.
- [`noise.jpg`](src/006-image-smoothing/noise.jpg): input image for the smoothing example.

### 007 Edge Detection

- [`edge_detection.py`](src/007-edge-detection/edge_detection.py): extracts edges with Canny and displays the result with Matplotlib.
- [`luna.jpg`](src/007-edge-detection/luna.jpg): input image for the edge-detection example.

### 008 Morphological Processing

- [`morphology_operations.py`](src/008-morphological-operations/morphology_operations.py): demonstrates erosion, dilation, opening, closing, top-hat, and black-hat with a shared structuring element.
- [`example_org.jpg`](src/008-morphological-operations/example_org.jpg): original-image example.
- [`example_noise.jpg`](src/008-morphological-operations/example_noise.jpg): noisy-image example.
- [`example_cave.jpg`](src/008-morphological-operations/example_cave.jpg): closing and black-hat example.

### 009 Thresholding

- [`threshold.py`](src/009-thresholding/threshold.py): performs global binary thresholding with a fixed threshold.
- [`adaptive_threshold.py`](src/009-thresholding/adaptive_threshold.py): performs adaptive thresholding from local-region statistics.
- [`otsu_threshold.py`](src/009-thresholding/otsu_threshold.py): computes a threshold with Otsu's method and binarizes the image.
- [`test.jpg`](src/009-thresholding/test.jpg): input image for the thresholding examples.

### 010 Contours and Features

- [`contours.py`](src/010-contours-and-features/contours.py): finds and draws contours after thresholding.
- [`moments.py`](src/010-contours-and-features/moments.py): calculates contour moments, area, and perimeter.
- [`approx_polygon.py`](src/010-contours-and-features/approx_polygon.py): approximates a contour with `approxPolyDP`.
- [`convex_hull.py`](src/010-contours-and-features/convex_hull.py): calculates and draws a contour convex hull.
- [`bounding_rect.py`](src/010-contours-and-features/bounding_rect.py): calculates an axis-aligned rectangle and a minimum-area rotated rectangle.
- [`test.jpg`](src/010-contours-and-features/test.jpg): input image for the contour examples.

Additional file notes are available in [`readme.txt`](src/010-contours-and-features/readme.txt).

### 011 Feature Matching

- [`bf_matcher.py`](src/011-feature-matching/bf_matcher.py): extracts ORB features and performs brute-force matching with Hamming distance and cross-checking.
- [`flann_matcher.py`](src/011-feature-matching/flann_matcher.py): performs KNN nearest-neighbor matching of ORB descriptors with a FLANN LSH index.
- [`test.jpg`](src/011-feature-matching/test.jpg) and [`test1.jpg`](src/011-feature-matching/test1.jpg): input images for feature matching.

### 012 Corner Detection

- [`harris_corner_detection.py`](src/012-corner-detection/harris_corner_detection.py): converts the image to grayscale, detects corners with Harris, and marks the result on the original image.
- [`test.jpg`](src/012-corner-detection/test.jpg): input image for the corner-detection example.

## Install Dependencies

Create a Python virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install opencv-python numpy matplotlib
```

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install opencv-python numpy matplotlib
```

Notes:

- `opencv-python` provides the `cv2` module and basic GUI support.
- `numpy` is used for arrays, coordinates, and structuring elements.
- `matplotlib` is used to compare smoothing and edge-detection results.
- On a headless server or container, `cv.imshow`, `cv.waitKey`, and `plt.show` may not be able to display windows.

## Run the Examples

Most scripts resolve image paths relative to the current working directory. Change into the relevant chapter directory before running a script. For example:

```bash
cd src/001-image-video-io
python image_read.py
```

Run drawing, color-conversion, and thresholding examples:

```bash
cd src/002-image-drawing
python drawing.py

cd ../004-color-space-conversion
python color_conversion.py

cd ../009-thresholding
python otsu_threshold.py
```

Run feature matching and corner detection:

```bash
cd src/011-feature-matching
python bf_matcher.py

cd ../012-corner-detection
python harris_corner_detection.py
```

Run the camera example:

```bash
cd src/001-image-video-io
python video_read.py
```

Press `q` to exit the camera window. The example releases the camera and OpenCV windows before exiting.

## OpenCV Notes

- OpenCV uses BGR channel order by default, while Matplotlib usually interprets color images as RGB. Convert the channel order when displaying a color image across the two libraries.
- `cv.imread` returns an empty object when loading fails. Check the path and filename before processing a new image.
- Image arrays are commonly indexed as `[row, column]`, corresponding to `[y, x]`; do not confuse this with Cartesian coordinate order.
- Thresholding, edge detection, and contour processing commonly require grayscale conversion, filtering, or binarization first.
- Contour indexes, input-image content, and threshold parameters affect the result. The same contour index cannot be assumed for arbitrary images.
- ORB, BF, and FLANN matching quality depends on keypoint count, descriptor type, scale, and viewpoint changes.
- Camera access, GUI windows, and Matplotlib interactive display are runtime resources and should be released or closed when a script exits.

## Repository Structure

```text
opencv-computer-vision-notes/
├── README.md
├── README-English.md
├── docs/
│   ├── 001-图片&视频加载及展示.pdf
│   ├── 002-图像的绘制方法.pdf
│   ├── ...
│   └── 012-图像处理-角点检测.pdf
└── src/
    ├── 001-image-video-io/
    ├── 002-image-drawing/
    ├── 003-basic-image-operations/
    ├── 004-color-space-conversion/
    ├── 005-geometric-transformation/
    ├── 006-image-smoothing/
    ├── 007-edge-detection/
    ├── 008-morphological-operations/
    ├── 009-thresholding/
    ├── 010-contours-and-features/
    ├── 011-feature-matching/
    └── 012-corner-detection/
```

## Current Scope

This repository focuses on basic OpenCV image processing and traditional computer vision algorithms. It includes course materials, example source files, and input images. It does not currently include deep-learning object detection, semantic segmentation, camera calibration, stereo vision, video tracking, deployment optimization, or a complete application project.

## Keywords

`OpenCV` `Python` `Computer Vision` `Image Processing` `Video I/O` `Color Space` `Geometric Transformation` `Smoothing` `Canny` `Morphology` `Thresholding` `Contours` `ORB` `BFMatcher` `FLANN` `Harris Corner`
