# Unix Platforms
## Installing
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
## Uninstalling
Type `sudo make uninstall` from the distribution directory. 

## Reference
- [https://sno.phy.queensu.ca/~phil/exiftool/install.html#Unix](https://sno.phy.queensu.ca/~phil/exiftool/install.html#Unix)
