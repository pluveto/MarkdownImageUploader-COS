# MarkdownImageUploader-COS
将 markdown 文件里的本地图片上传到腾讯云对象储存，以便发布到博客。请搭配 Typora 食用。目前由于正则只匹配形如 X:\ 的路径，请别在 Linux/Mac 上使用，如果需要，请自行修改代码，也欢迎提交 PR。

## 食用方法

安装 sdk

```py
pip install -U cos-python-sdk-v5
```

编辑本脚本，填写相关配置信息。

执行下列命令运行

```
py run.py <your_file.md>
```

之后会输出文件 `your_file.out.md`，即可发布到你的博客啦。

**务必使用 POWERSHELL, 一律 UTF-8 编码**
