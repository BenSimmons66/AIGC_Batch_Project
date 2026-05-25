import os
import requests
import time
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("ZHIPU_API_KEY")

if not API_KEY:
    print(" 错误：没有找到 ZHIPU_API_KEY，请检查 .env 文件")
    exit(1)

def generate_image(prompt, save_name):
    print(f"🎨 正在生成 {save_name} ...")
    url = "https://open.bigmodel.cn/api/paas/v4/images/generations"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "cogview-3-flash",
        "prompt": prompt,
        "size": "1024x1024",
        "n": 1
    }

    try:
        # 设置 30 秒超时
        resp = requests.post(url, headers=headers, json=data, timeout=30)
        if resp.status_code != 200:
            print(f"   HTTP {resp.status_code}: {resp.text[:200]}")
            return False
        img_url = resp.json()["data"][0]["url"]
        img_data = requests.get(img_url, timeout=30).content
        os.makedirs("images", exist_ok=True)
        with open(f"images/{save_name}.png", "wb") as f:
            f.write(img_data)
        print(f"   成功: images/{save_name}.png")
        return True
    except requests.exceptions.Timeout:
        print("   请求超时（30秒），请检查网络或代理")
        return False
    except requests.exceptions.ConnectionError:
        print("   网络连接错误，无法访问智谱 API")
        return False
    except Exception as e:
        print(f"   错误: {e}")
        return False

topics = [
    "夏日冰咖啡，清爽玻璃杯，冰块，阳光，现代风格",
    "超薄笔记本，金属质感，科技感，蓝色调",
    "环保帆布袋，极简设计，绿色植物背景",
    "瑜伽垫，柔和色彩，自然光线，宁静氛围",
    "智能手表，圆形表盘，运动场景，动感"
]

print("开始批量生成...")
for i, topic in enumerate(topics, 1):
    generate_image(topic, f"product_{i}")
    time.sleep(1)
print("完成")