import serial
import copy
import math
import numpy as np
import open3d as o3d

number=74
round=4

if __name__ == "__main__":

    s = serial.Serial("COM4", 115200)
    lines = []
    print("Opening: " + s.name)
    f = open("400198775.xyz","w")
    for i in range(number*round):
        x = s.readline()        # read one line
        c = x.decode()      # convert byte type to str
        print(c)
        f.write(c)
        lines.append(c)

    print("Closing: " + s.name) 
    s.close()
    f.close()
    
    pcd = o3d.io.read_point_cloud("400198775.xyz")
    print(pcd)
    print(np.asarray(pcd.points))
    
    pt1 = 0
    pt2 = 1
    pt3 = 2
    pt4 = 3
    po = 0

    lines = []
    # create planes
    for x in range(number*round):
        lines.append([pt1+po,pt2+po])
        lines.append([pt2+po,pt3+po])
        lines.append([pt3+po,pt4+po])
        lines.append([pt4+po,pt1+po])
        po += 4;

    #reset var
    pt1 = 0
    pt2 = 1
    pt3 = 2
    pt4 = 3
    po = 0
    do = 4
    # connect lines
    for x in range(number*round-1):
        lines.append([pt1+po,pt1+do+po])
        lines.append([pt2+po,pt2+do+po])
        lines.append([pt3+po,pt3+do+po])
        lines.append([pt4+po,pt4+do+po])
        po += 4;

    line_set = o3d.geometry.LineSet(points = o3d.utility.Vector3dVector(np.asarray(pcd.points)), lines = o3d.utility.Vector2iVector(lines))

    #Show results
    
    o3d.visualization.draw_geometries([line_set])