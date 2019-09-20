import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt
import argparse
import csv
import sys

class ReadNCdata:
    def __init__(self, start_time, end_time, lat, lon, pic_name):
        self.start_time = start_time
        self.end_time = end_time
        self.lat = int(lat)
        self.lon = int(lon)
        self.pic_name = pic_name

    def draw(self):
        data, start, end = self.readnc()

        # x = np.array(range(start + 1, end + 1))
        date = self.GetTime(end - start)
        x = np.array(date)
        y = np.array(data)

        length = (end - start) / 12
        # print(length)

        plt.rcParams['figure.figsize'] = (24.0, 4.0)
        plt.title("From " + self.start_time + " to " + self.end_time + " sst data ")
        plt.axis('equal')
        plt.plot(x, y,  color='r')

        ax = plt.gca()
        # plt.ylim(-3, 30)
        x_major_locator = plt.MultipleLocator(int(length))
        ax.xaxis.set_major_locator(x_major_locator)
        # ax.set_ylim(-3, 30)
        # plt.ylim(-3, 35)
        # for a, b in zip(x, y):
        #     plt.text(a, b, (a, b), ha='center', va='bottom', fontsize=8)
        # plt.show()
        plt.savefig(sys.path[0] + "/Pics/" + self.pic_name + ".jpg")
        with open(sys.path[0] + '/Temp_data/' + self.pic_name + ".csv", "w", encoding = "utf-8") as csvfile:
            w = csv.writer(csvfile)
            writerows = [["lat is " + str(self.lat)], ["lon is " + str(self.lon)], ["From " + str(self.start_time) + " to " + self.end_time + " sst data "],["time", "sst"]]
            for i in range(len(data)):
                writerows.append([date[i], data[i]])

            for row in writerows:
                w.writerow(row)


    def GetTime(self, num):
        result = []
        time = self.start_time.split('-')
        year = int(time[0])
        month = int(time[1])
        for i in range(num):
            if month != 12:
                result.append(str(year) + "-" + str(month))
                month += 1
            else:
                result.append(str(year) + "-" + str(month))
                month = 1
                year += 1
        return result


    def readnc(self):
        start = self.GetDay(self.start_time)
        end = self.GetDay(self.end_time)
        ncfile = nc.Dataset(sys.path[0] + "\\sst.mnmean.nc")
        sst = ncfile.variables['sst'][start:end]

        result = []
        for temp in sst:
            result.append(temp[self.GetLat()][self.GetLon()])
        # print(result)
        return result, start, end

    def GetLat(self):
        if self.lat == 0:
            return 0
        else:
            if self.lat > 0:
                return 44 - int(self.lat / 2)
            else:
                return 44 - int(self.lat / 2)

    def GetLon(self):
        return int(self.lon / 2)

    def GetDay(self, time):
        # days since 1800-1-1
        time = time.split("-")

        year = int(time[0])
        month = int(time[1])

        return (year - 1854) * 12 + month - 1


if __name__ == "__main__":
    # ncfile = nc.Dataset("sst.mnmean.nc")
    # print(ncfile.variables['sst'])
    parser = argparse.ArgumentParser()

    parser.add_argument("--start", required=True,
                        default='1854-1',
                        help='path to weight .h5 file')
    parser.add_argument("--end", required=True,
                        default='1857-1',
                        help="input the test image")
    parser.add_argument('--lat', required=True,
                        default='2',
                        help="output the result image")
    parser.add_argument('--lon', required=True,
                        default='358',
                        help="output the result image")
    parser.add_argument('--name', required=True,
                        default='From 1854-1 to 1857-1',
                        help="output the result image")

    args = parser.parse_args()

    r = ReadNCdata(args.start, args.end, args.lat, args.lon, args.name)
    r.draw()
