# 使用Exiftool给图片添加个性化Tag
[TOC]

## `Exiftool`的简介


## `Exiftool`的安装
- Ubuntu 16.04的安装
- 1. *Download* the *Image-ExifTool* distribution from the [ExifTool home page](https://sno.phy.queensu.ca/~phil/exiftool/index.html)
(The file you download should be named `Image-ExifTool-11.25.tar.gz`.)
-    2.*Unpack the distribution* and *make it your current directory* by typing:
```bash
cd <your download directory>
gzip -dc Image-ExifTool-11.25.tar.gz | tar -xf -
cd Image-ExifTool-11.25
```
(At this point you may run exiftool by typing`./exiftool <image file name>` .)
-    3.*Test and install ExifTool* by typing:
```bash
perl Makefile.PL
make test
sudo make install
```
(Note: The `make test` step is not required, but useful because it runs a full suite of tests to verify that ExifTool is working properly on your system. The `sudo make install` command requires that you have su access, and will prompt for your password. This will make ExifTool and its documentation accessible to all users on your system. If you don't have su access, you can run ExifTool in your own account by moving `exiftool` and its `lib` directory to any convienient location, preferably somewhere in your PATH.)
You can now run exiftool by typing `exiftool`. Also, you can consult the ExifTool documentation with commands like:
```bash
perldoc exiftool
perldoc Image::ExifTool
perldoc Image::ExifTool::TagNames
```
or
```bash
man exiftool
man Image::ExifTool
man Image::ExifTool::TagNames
```

## Reference
- [https://sno.phy.queensu.ca/~phil/exiftool/install.html#Unix](https://sno.phy.queensu.ca/~phil/exiftool/install.html#Unix)

## `Exiftool`提取图片的Tag信息
```bash
exiftool -a -u -g1 ch_2.jpg
```

## `Exiftool`添加图片的Tag信息
```bash
exiftool -GPSLongitude=180.1888 -GPSLatitude=32.8888 -GPSAltitude=55.2101 ch_2.jpg
exiftool -FlightPitchDegree=1.526 -FlightRollDegree=24.631 -FlightYawDegree=-275.54 -GimbalPitchDegree=1.082 -GimbalRollDegree=0.0 -GimbalYawDegree=90.65 ch_2.jpg
```

## `Exiftool`添加自定义的Tag信息
- 步骤
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

- 参考
    - [http://web.mit.edu/jhawk/mnt/cgs/Image-ExifTool-6.99/html/faq.html](http://web.mit.edu/jhawk/mnt/cgs/Image-ExifTool-6.99/html/faq.html)


