# AI-Generated Art with Style Transfer

## Overview
This project applies **Neural Style Transfer (NST)** to transform an image by blending it with an artistic style. It utilizes **TensorFlow's VGG19 model** to extract features and generate a stylized version of the content image.

## Features
✅ Uses **VGG19** for feature extraction  
✅ Transfers artistic styles to any image  
✅ Adjustable content & style weights  
✅ Option to use a **pre-trained Fast Style Transfer model** for instant results  

## Requirements
Install the required dependencies using:
```bash
pip install tensorflow opencv-python matplotlib numpy
```

## Usage
1. Place your content and style images in the project folder.
2. Rename them as:
   - `content.jpg` (image to transform)
   - `style.jpg` (artwork style to apply)
3. Run the script:
python style_transfer.py
```
4. The output image will be displayed and saved.

## Customization
- **Adjust Iterations**: Change `iterations=1000` for better results.
- **Modify Style Weight**: Increase `style_weight=1e-1` for stronger stylization.
- **Use Pre-trained Model**: Run `fast_style_transfer.py` for real-time results.

## Output Example
After processing, your content image will have the visual style of the chosen artwork.

---
### Notes
- Works best with **high-resolution images**.
- Higher iterations improve details but increase processing time.
- The **pre-trained model** offers fast, high-quality stylization.



