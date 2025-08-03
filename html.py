#!/usr/bin/env python3
import os
import glob
import json

print("开始生成 index.html 文件...")

# 获取所有图片文件
image_files = []
for ext in ('*.jpg', '*.jpeg', '*.JPG', '*.JPEG'):
    image_files.extend(glob.glob(f'images/{ext}', recursive=True))

print(f"找到 {len(image_files)} 张图片")

# 生成图片数组的 JavaScript 代码
images_js = ",\n            ".join([f'"{img}"' for img in image_files])

# HTML 模板
html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>随机图片</title>
    <script>
        // 自动生成的图片列表
        const images = [
            {images_js}
        ];
        
        // 页面加载后立即重定向
        window.onload = function() {{
            if(images.length === 0) {{
                document.body.innerHTML = '<h1 style="color:red;text-align:center;margin-top:100px;">错误：没有可用图片</h1>';
                return;
            }}
            
            // 随机选择一张图片
            const randomIndex = Math.floor(Math.random() * images.length);
            const randomImage = images[randomIndex];
            
            // 立即重定向
            window.location.href = randomImage;
        }};
    </script>
    <style>
    </style>
</head>
<body>
</body>
</html>
"""

# 写入文件
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("index.html 文件生成完成")
