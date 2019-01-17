# User defined tags writing

## 查看所有的tag
```bash
exiftool ch_2.jpg
exiftool -s ch_2.jpg

exiftool -a -u -g1 ch_2.jpg  # 可以看到大类
```
## 查看xmp信息
```bash
exiftool -XMP -b ch_2.jpg
```
## 查看某个标签的信息
```bash
exiftool -ImageWidth ch_2.jpg
```

## 给已有的tag写信息
exiftool -GPSLongitude=180.1888 -GPSLatitude=32.8888 -GPSAltitude=55.2101 ch_2.jpg
exiftool -FlightPitchDegree=1.526 -FlightRollDegree=24.631 -FlightYawDegree=-275.54 -GimbalPitchDegree=1.082 -GimbalRollDegree=0.0 -GimbalYawDegree=90.65 ch_2.jpg

## 新建tag，并写入信息

For examples of how to add user-defined tags, see the ExifTool_config file in the ExifTool distribution. To activate this file, rename it to `.ExifTool_config` and copy it to your HOME directory. With this installed, you should be able to write and read the example tags (such as `NewXMPxxxTag1`). Try this first before you attempt to define your own tags.
If this doesn't work, the most common problem is that the `.ExifTool_config` configuration file isn't getting loaded properly, and there are two things you can try: 1) Set either the HOME or the EXIFTOOL_HOME environment variable to the name of the directory where you put your `.ExifTool_config` file, or 2) put the config file in the same directory as the exiftool script. (Also, be sure the config filename starts with a dot! In the Windows GUI you may be not be able to generate a file name that starts with a `.`, but it can be done from the command line using the `rename` command.)
If necessary, you can verify that ExifTool is loading your config file by adding the following line to your file:
print "LOADED!\n";
If you see a `LOADED!` message when you run exiftool, but your new tags still don't work, make sure you are using the proper tag name and that the file you are writing can support these names. Try copying the `t/images/Writer.jpg` file from the distribution and running exiftool with the following command:
```bash
exiftool -v3 -NewXMPxxxTag1=test Writer.jpg
```
If ExifTool recognizes the new tag, the first line of output from this command should be
`Writing XMP-xxx:NewXMPxxxTag1`
Then you can read back the new tag with `exiftool -s Writer.jpg`.

### Reference
- [http://web.mit.edu/jhawk/mnt/cgs/Image-ExifTool-6.99/html/faq.html](http://web.mit.edu/jhawk/mnt/cgs/Image-ExifTool-6.99/html/faq.html)


