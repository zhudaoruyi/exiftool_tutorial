# 查看所有的tag
exiftool ch_2.jpg
exiftool -s ch_2.jpg

exiftool -a -u -g1 ch_2.jpg  # 可以看到大类
# 查看xmp信息
exiftool -XMP -b ch_2.jpg
# 查看某个标签的信息
exiftool -ImageWidth ch_2.jpg
