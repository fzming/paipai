#coding=utf8

import imtool
import ocr

from win.capture import capture_window
from win.browser import open_ie
from win.window import find_sub_hwnd

import time

if __name__ == '__main__':
    # 51hupai.org
    # (left, top), w, h
    pos_info = [
            ((125, 291), 62, 13),
            ((139, 307), 62, 13),
            ((123, 402), 83, 13),
            ((152, 420), 83, 13),
            ((183, 434), 83, 13),
            ]

    ie = open_ie(url="http://moni.51hupai.org")
    #hwnd = window.find_sub_hwnd(ie.HWND, [("Frame Tab", 0),
    #    ("TabWindowClass", 0),
    #    ("Shell DocObject View", 0),
    #    ("Internet Explorer_Server", 0)])
    hwnd = find_sub_hwnd(ie.HWND, [("Frame Tab", 0)])
    print "%x" % (hwnd)

    time.sleep(3)

    for i in xrange(100):
        img = capture_window(hwnd)
        images = imtool.find_images(img, pos_info)
        data = []
        for j in xrange(len(images)):
            images[j].save('%s-%s.png' % (i,j))
            data.append(ocr.recog(images[j]))
        print ','.join(data)
        time.sleep(0.4)

