# pyopengl-sample.py
# 
# [2021/02/08] OSHIRO Naoki.

import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def display(): # 表示用
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)

    glLoadIdentity() # 変換行列初期化
    gluLookAt(3.0, 4.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0) # カメラ設定

    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, (0.8, 0.0, 0.0, 1.0)) # 色付け
    #glutSolidSphere(1.0, 32, 32) # 球（サイズ、分割数, 分割数）
    #glutSolidTorus(0.25, 0.80, 32, 32) # トーラス（サイズ, 分割数, 分割数）
    glutSolidTeapot(1.0) # ティーポット（サイズ）

    glFlush() # 表示更新

def reshape(w, h): # 再描画設定
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(30.0, 1.0*w/h, 1.0, 100.0) # 透視投影設定

# GLUT初期設定
glutInit(sys.argv) # GLUT初期化 
glutInitWindowSize(300, 300) # 表示ウィンドウのサイズ指定
glutInitWindowPosition(100, 100) # 表示ウィンドウの位置指定
glutCreateWindow(b"Hello") # 表示ウィンドウの生成（ウィンドウタイトルに指定する文字列指定はb"..."としないとダメ）

# コールバック関数の指定
glutDisplayFunc(display)
glutReshapeFunc(reshape)

# ３次元表示設定
glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0)

# GLUTイベント処理の開始（抜けるには glutLeaveMainLoop()）
glutMainLoop()
