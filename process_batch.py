import os
from PIL import Image, ImageDraw, ImageFont

def resize_and_watermark(input_dir="images", output_dir="final_output", 
                         size=(1024, 1024), text="AIGC Intern Demo"):
    # 创建输出文件夹
    os.makedirs(output_dir, exist_ok=True)
    
    # 尝试加载字体，如果系统中没有指定字体，则使用默认字体
    try:
        font = ImageFont.truetype("arial.ttf", 36)
    except:
        font = ImageFont.load_default()
    
    # 遍历images文件夹中的所有图片
    for fname in os.listdir(input_dir):
        if not fname.lower().endswith((".png", ".jpg", ".jpeg")):
            continue
            
        img_path = os.path.join(input_dir, fname)
        print(f" 处理图片: {fname}")
        
        # 1. 打开图片并缩放
        img = Image.open(img_path).convert("RGBA")
        img = img.resize(size, Image.Resampling.LANCZOS) # 使用 LANCZOS 算法保证高质量缩放[reference:11]
        
        # 2. 创建水印图层
        watermark = Image.new("RGBA", img.size, (0,0,0,0))
        draw = ImageDraw.Draw(watermark)
        
        # 计算文字水印的尺寸和位置（右下角，留20像素边距）
        bbox = draw.textbbox((0, 0), text, font=font)
        text_w, text_h = bbox[2] - bbox[0], bbox[3] - bbox[1]
        x = img.width - text_w - 20
        y = img.height - text_h - 20
        
        # 绘制半透明白色水印
        draw.text((x, y), text, font=font, fill=(255, 255, 255, 128))
        
        # 3. 合并原图与水印，并保存
        out = Image.alpha_composite(img, watermark).convert("RGB")
        output_path = os.path.join(output_dir, f"final_{fname}")
        out.save(output_path)
        print(f"  已保存: {output_path}")

if __name__ == "__main__":
    resize_and_watermark()
    print("所有图片处理完毕！")