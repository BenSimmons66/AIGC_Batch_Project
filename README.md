# AIGC 批量创意素材生成管线

这是一个使用智谱AI免费API和Python PIL库，实现批量生成并处理品牌宣传图片的个人项目。

## 项目目的
该项目旨在学习并实践AIGC相关API的调用，模拟了针对电商/社交媒体等场景，快速、批量生产规范宣传素材的自动化流程。

## 技术栈
- **编程语言**: Python 3
- **核心库**: 
  - `requests`: 调用智谱AI的图片生成API。
  - `Pillow (PIL)`: 批量处理图片（缩放、添加水印）。
  - `python-dotenv`: 安全管理环境变量。

## 主要功能
1.  **批量生成**: 根据预设的5个主题，自动调用智谱AI的`CogView-3-Flash`免费模型生成品牌宣传图。
2.  **批量处理**: 对生成的原始图片进行自动化后期处理，包括统一尺寸和添加半透明水印。
3.  **全自动管线**: 从文字创意到最终成品，一键运行，即可获得可直接使用的素材文件。

## 快速开始

### 1. 环境准备
确保已安装Python 3.8+。

### 2. 安装依赖库
```bash
pip install requests Pillow python-dotenv
```
### 3. 配置API密钥
在 智谱AI开放平台 注册并获取你的 API Key。

在项目根目录下创建一个 .env 文件，并写入你的密钥：
ZHIPU_API_KEY=你的API_Key
### 4. 运行脚本
生成图片: python generate_batch.py

处理图片: python process_batch.py

### 项目结构
text
AIGC_Batch_Project/
├── .env                # 存储API Key
├── generate_batch.py   # 批量生成图片脚本
├── process_batch.py    # 批量处理图片脚本
├── images/             # 存放生成的原始图片
├── final_output/       # 存放处理后的成品图片
└── README.md           # 项目说明文件