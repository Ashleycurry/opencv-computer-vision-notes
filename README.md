# OpenCV 计算机视觉学习笔记

[中文](README.md) | [English](README-English.md)

本仓库用于整理 OpenCV 计算机视觉入门和基础图像处理学习资料。课程内容从图片与视频的加载、显示和绘制开始，逐步覆盖像素操作、颜色空间转换、几何变换、图像平滑、边缘检测、形态学处理、阈值分割、轮廓分析、特征匹配和角点检测。

课件位于 `docs/`，对应示例位于 `src/`。每个章节都使用英文目录名保存源码，并通过真实文件路径连接到对应脚本和示例图片。

## 资料与环境

- 课件目录：[docs](docs)
- 示例源码目录：[src](src)
- 课件数量：12 份 PDF，共 121 页
- 编程语言：Python 3
- 核心库：OpenCV、NumPy
- 可视化库：Matplotlib
- 运行方式：独立 Python 脚本和 OpenCV GUI 窗口
- 摄像头示例：需要可用的本地摄像头

## 学习路线

```text
输入与显示
    -> 图片读取、视频读取、摄像头访问
    -> OpenCV 窗口、键盘事件和资源释放
            |
            v
图像基础
    -> 几何图形与文字绘制
    -> 像素访问、图像属性和通道操作
    -> BGR、GRAY、HSV、Lab、YCrCb
            |
            v
图像处理
    -> 缩放、平移、旋转、透视变换和重映射
    -> 均值、高斯和中值滤波
    -> Canny 边缘检测
    -> 腐蚀、膨胀、开闭运算和顶帽/黑帽
            |
            v
目标分析
    -> 全局、自适应和 Otsu 阈值
    -> 轮廓、矩、凸包和外接矩形
    -> ORB 特征、BF/FLANN 匹配
    -> Harris 角点检测
```

## 章节与源码

| 编号 | 课件 | 页数 | 源码目录 | 主要内容 |
| --- | --- | ---: | --- | --- |
| 001 | [图片&视频加载及展示](docs/001-图片%26视频加载及展示.pdf) | 2 | [`001-image-video-io`](src/001-image-video-io) | 图片读取、显示、摄像头读取和视频帧处理 |
| 002 | [图像的绘制方法](docs/002-图像的绘制方法.pdf) | 3 | [`002-image-drawing`](src/002-image-drawing) | 直线、矩形、圆、多边形和文本绘制 |
| 003 | [图像的基础操作](docs/003-图像的基础操作.pdf) | 2 | [`003-basic-image-operations`](src/003-basic-image-operations) | 像素访问、图像属性、通道拆分合并和颜色转换 |
| 004 | [图像处理-颜色空间转换](docs/004-图像处理——颜色空间转换.pdf) | 11 | [`004-color-space-conversion`](src/004-color-space-conversion) | GRAY、Lab、YCrCb、HSV 等颜色空间 |
| 005 | [图像处理-几何变换](docs/005-图像处理-几何变换.pdf) | 35 | [`005-geometric-transformation`](src/005-geometric-transformation) | 缩放、平移、旋转、透视变换和重映射 |
| 006 | [图像处理-平滑](docs/006-图像处理-平滑.pdf) | 11 | [`006-image-smoothing`](src/006-image-smoothing) | 噪声、均值滤波、高斯滤波和中值滤波 |
| 007 | [图像处理-边缘检测](docs/007-图像处理-边缘检测.pdf) | 9 | [`007-edge-detection`](src/007-edge-detection) | 边缘检测原理和 Canny 算法 |
| 008 | [图像处理-形态学处理](docs/008-图像处理-形态学处理.pdf) | 13 | [`008-morphological-operations`](src/008-morphological-operations) | 腐蚀、膨胀、开运算、闭运算、顶帽和黑帽 |
| 009 | [图像处理-阈值处理](docs/009-图像处理-阈值处理.pdf) | 8 | [`009-thresholding`](src/009-thresholding) | 全局阈值、自适应阈值和 Otsu 阈值 |
| 010 | [图像处理-轮廓介绍及特征](docs/010-图像处理-轮廓介绍及特征.pdf) | 13 | [`010-contours-and-features`](src/010-contours-and-features) | 轮廓、矩、多边形逼近、凸包和外接矩形 |
| 011 | [图像处理-特征匹配](docs/011-图像处理-特征匹配.pdf) | 7 | [`011-feature-matching`](src/011-feature-matching) | ORB 特征、暴力匹配和 FLANN 最近邻匹配 |
| 012 | [图像处理-角点检测](docs/012-图像处理-角点检测.pdf) | 7 | [`012-corner-detection`](src/012-corner-detection) | 角点概念、检测思路和 Harris 角点检测 |

## 示例说明

### 001 图片与视频 I/O

- [`image_read.py`](src/001-image-video-io/image_read.py)：使用 `cv.imread` 读取图片，创建窗口并显示图像。
- [`video_read.py`](src/001-image-video-io/video_read.py)：使用 `cv.VideoCapture(0)` 读取摄像头帧，按 `q` 退出并释放设备。
- [`opencv.png`](src/001-image-video-io/opencv.png)：图片读取示例的输入文件。

### 002 图像绘制

- [`drawing.py`](src/002-image-drawing/drawing.py)：使用 `line`、`rectangle`、`circle`、`polylines` 和 `putText` 绘制图形与文本。
- [`test.jpg`](src/002-image-drawing/test.jpg)：绘制示例的输入图片。

### 003 基础图像操作

- [`basic_operations.py`](src/003-basic-image-operations/basic_operations.py)：访问和修改像素，读取 `shape`、`size`、`dtype`，拆分/合并 BGR 通道，并转换到 HSV。
- [`test.jpg`](src/003-basic-image-operations/test.jpg)：基础操作示例的输入图片。

### 004 颜色空间转换

- [`color_conversion.py`](src/004-color-space-conversion/color_conversion.py)：将 BGR 图像转换为 GRAY、Lab、YCrCb 和 HSV，并显示转换结果。
- [`img.jpg`](src/004-color-space-conversion/img.jpg)：颜色空间转换示例的输入图片。

### 005 几何变换

源码目录中包含以下几类变换：

- [`Scale/Scale.py`](src/005-geometric-transformation/Scale/Scale.py)：使用 `cv.resize` 放大和缩小图像。
- [`Translation/Translation.py`](src/005-geometric-transformation/Translation/Translation.py)：使用仿射矩阵平移图像。
- [`Revolve/Revolve.py`](src/005-geometric-transformation/Revolve/Revolve.py)：围绕中心旋转图像并调整缩放比例。
- [`Perspective/Perspective.py`](src/005-geometric-transformation/Perspective/Perspective.py)：使用四组对应点计算透视变换矩阵。
- [`Remap/copy.py`](src/005-geometric-transformation/Remap/copy.py)：将多个输出像素映射到原图像中的指定位置。
- [`Remap/copy_all.py`](src/005-geometric-transformation/Remap/copy_all.py)：构造完整坐标映射并执行重映射。
- [`Remap/x_rotation.py`](src/005-geometric-transformation/Remap/x_rotation.py)：沿 X 方向翻转坐标。
- [`Remap/y_rotation.py`](src/005-geometric-transformation/Remap/y_rotation.py)：沿 Y 方向翻转坐标。
- [`Remap/xy_rotation.py`](src/005-geometric-transformation/Remap/xy_rotation.py)：同时翻转 X、Y 方向坐标。
- [`Remap/half_size.py`](src/005-geometric-transformation/Remap/half_size.py)：通过坐标映射演示图像压缩。
- [`1.jpg`](src/005-geometric-transformation/Scale/1.jpg)：缩放示例输入图片；其他几何变换目录中也包含对应的 `1.jpg` 输入文件。

章节补充说明见 [`readme.txt`](src/005-geometric-transformation/readme.txt)。

### 006 图像平滑

- [`filtering.py`](src/006-image-smoothing/filtering.py)：对含噪图片分别执行均值、高斯和中值滤波，并使用 Matplotlib 对比结果。
- [`noise.jpg`](src/006-image-smoothing/noise.jpg)：平滑处理示例的输入图片。

### 007 边缘检测

- [`edge_detection.py`](src/007-edge-detection/edge_detection.py)：使用 Canny 算法提取图像边缘，并通过 Matplotlib 显示结果。
- [`luna.jpg`](src/007-edge-detection/luna.jpg)：边缘检测示例的输入图片。

### 008 形态学处理

- [`morphology_operations.py`](src/008-morphological-operations/morphology_operations.py)：使用统一结构元素演示腐蚀、膨胀、开运算、闭运算、顶帽和黑帽。
- [`example_org.jpg`](src/008-morphological-operations/example_org.jpg)：原始图像示例。
- [`example_noise.jpg`](src/008-morphological-operations/example_noise.jpg)：噪声图像示例。
- [`example_cave.jpg`](src/008-morphological-operations/example_cave.jpg)：闭运算和黑帽示例。

### 009 阈值处理

- [`threshold.py`](src/009-thresholding/threshold.py)：使用固定阈值执行全局二值化。
- [`adaptive_threshold.py`](src/009-thresholding/adaptive_threshold.py)：使用局部区域统计量执行自适应阈值处理。
- [`otsu_threshold.py`](src/009-thresholding/otsu_threshold.py)：使用 Otsu 算法自动计算阈值并二值化。
- [`test.jpg`](src/009-thresholding/test.jpg)：阈值处理示例的输入图片。

### 010 轮廓与特征

- [`contours.py`](src/010-contours-and-features/contours.py)：二值化后查找并绘制轮廓。
- [`moments.py`](src/010-contours-and-features/moments.py)：计算轮廓矩、面积和周长。
- [`approx_polygon.py`](src/010-contours-and-features/approx_polygon.py)：使用 `approxPolyDP` 进行多边形逼近。
- [`convex_hull.py`](src/010-contours-and-features/convex_hull.py)：计算并绘制轮廓凸包。
- [`bounding_rect.py`](src/010-contours-and-features/bounding_rect.py)：计算常规外接矩形和最小旋转外接矩形。
- [`test.jpg`](src/010-contours-and-features/test.jpg)：轮廓分析示例的输入图片。

章节文件说明见 [`readme.txt`](src/010-contours-and-features/readme.txt)。

### 011 特征匹配

- [`bf_matcher.py`](src/011-feature-matching/bf_matcher.py)：使用 ORB 提取特征，并通过汉明距离和交叉检查执行暴力匹配。
- [`flann_matcher.py`](src/011-feature-matching/flann_matcher.py)：使用 FLANN 的 LSH 索引执行 ORB 描述符的 KNN 最近邻匹配。
- [`test.jpg`](src/011-feature-matching/test.jpg) 和 [`test1.jpg`](src/011-feature-matching/test1.jpg)：特征匹配示例的两张输入图片。

### 012 角点检测

- [`harris_corner_detection.py`](src/012-corner-detection/harris_corner_detection.py)：将图像转换为灰度图，使用 Harris 算法检测角点，并在原图中标记结果。
- [`test.jpg`](src/012-corner-detection/test.jpg)：角点检测示例的输入图片。

## 安装依赖

建议使用 Python 虚拟环境：

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install opencv-python numpy matplotlib
```

Windows PowerShell 可使用：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install opencv-python numpy matplotlib
```

说明：

- `opencv-python` 提供 `cv2` 模块和基础 GUI 能力。
- `numpy` 用于数组、坐标和结构元素处理。
- `matplotlib` 用于平滑和边缘检测示例的结果对比。
- 在没有桌面环境的服务器或容器中，`cv.imshow`、`cv.waitKey` 和 `plt.show` 可能无法正常显示。

## 运行示例

源码中的图片路径大多是相对当前工作目录解析的，因此运行脚本前应进入对应章节目录。例如：

```bash
cd src/001-image-video-io
python image_read.py
```

运行绘图、颜色转换和阈值示例：

```bash
cd src/002-image-drawing
python drawing.py

cd ../004-color-space-conversion
python color_conversion.py

cd ../009-thresholding
python otsu_threshold.py
```

运行特征匹配和角点检测：

```bash
cd src/011-feature-matching
python bf_matcher.py

cd ../012-corner-detection
python harris_corner_detection.py
```

运行摄像头示例：

```bash
cd src/001-image-video-io
python video_read.py
```

按 `q` 退出摄像头窗口。运行完成后，示例会释放摄像头和 OpenCV 窗口资源。

## OpenCV 使用要点

- OpenCV 默认使用 BGR 通道顺序，而 Matplotlib 通常按 RGB 解释彩色图像；跨库显示时需要注意颜色顺序。
- `cv.imread` 读取失败时会返回空对象，运行新图片时应先确认路径和文件名。
- 图像数组的坐标通常按照 `[行, 列]` 访问，对应 `[y, x]`，不要与笛卡尔坐标顺序混淆。
- 阈值、边缘和轮廓处理通常需要先进行灰度化、滤波或二值化。
- 轮廓索引、输入图像内容和阈值参数会影响示例结果，不能假设不同图片一定具有相同的轮廓数量。
- ORB、BF 和 FLANN 匹配效果会受到关键点数量、描述符类型、图像尺度和视角变化影响。
- 摄像头、GUI 窗口和 Matplotlib 交互显示属于运行时资源，脚本退出前应及时释放。

## 仓库结构

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

## 当前范围

当前仓库聚焦 OpenCV 基础图像处理和传统计算机视觉算法，包含课件、示例源码和输入图片。暂未包含深度学习目标检测、语义分割、相机标定、立体视觉、视频跟踪、部署优化或完整应用工程。

## 关键词

`OpenCV` `Python` `Computer Vision` `Image Processing` `Video I/O` `Color Space` `Geometric Transformation` `Smoothing` `Canny` `Morphology` `Thresholding` `Contours` `ORB` `BFMatcher` `FLANN` `Harris Corner`
