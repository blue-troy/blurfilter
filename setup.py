from setuptools import setup, find_packages

setup(
    name='blurfilter',  # 应用名
    version='1.0',  # 版本号
    packages=find_packages(),
    install_requires=[  # 依赖列表
        'opencv-python'
    ]
)
