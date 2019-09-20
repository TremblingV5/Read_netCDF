import sys
import os

root = sys.path[0]

print("读取netCDF4文件程序")
start = input("第一步：输入开始时间（输入样式：1990-1） --->")
end = input("第二步：输入开始时间（输入样式：1990-1） --->")

lat = input("第三步：输入纬度（输入样式：-88到88之前，必须是偶数） --->")
lon = input("第四步：输入经度（输入样式：0到358之前，必须是偶数） --->")

name = input("第五步：输入存储名称（得到的数据的文件名） --->")

command = "python.exe \"" + root + "\\" + "ReadNC.py\" " + "--start=\"" + start + "\" --end=\"" + end + "\" --lat=\"" + lat + "\" --lon=\"" + lon + "\" --name=\"" + name + "\""

os.system(command)