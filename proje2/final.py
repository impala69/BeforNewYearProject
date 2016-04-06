# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebView
from PyQt4 import QtCore, QtGui
from search import Search
from Portal import Window
from searcher import searchclass
from history import history_window
import os, re
from threading import Thread

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(762, 563)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(208, 208, 208);"))
        MainWindow.setFixedSize(762,563)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.commandLinkButton = QtGui.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(30, 10, 131, 48))
        self.commandLinkButton.setStyleSheet(_fromUtf8("font: 16pt \"Agency FB\";"))
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.commandLinkButton_2 = QtGui.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(590, 10, 131, 48))
        self.commandLinkButton_2.setStyleSheet(_fromUtf8("font: 15pt \"Agency FB\";"))
        self.commandLinkButton_2.setObjectName(_fromUtf8("commandLinkButton_2"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 130, 751, 301))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.treeView = Main(self.verticalLayoutWidget)
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.verticalLayout_4.addWidget(self.treeView)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(200, 30, 351, 91))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.webView = QtWebKit.QWebView(self.verticalLayoutWidget_2)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.verticalLayout.addWidget(self.webView)
        self.webView.load(QUrl('hello.html'))

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolBar.setStyleSheet(_fromUtf8("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));"))
        self.toolBar.setIconSize(QtCore.QSize(51, 55))
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 762, 26))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menuBar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuView = QtGui.QMenu(self.menuBar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuTools = QtGui.QMenu(self.menuBar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionSettings = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Project/settings_icon.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings.setIcon(icon)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionSettings_2 = QtGui.QAction(MainWindow)
        self.actionSettings_2.setIcon(icon)
        self.actionSettings_2.setObjectName(_fromUtf8("actionSettings_2"))
        self.actionSearch = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/Project/search_icon3.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSearch.setIcon(icon1)
        self.actionSearch.setObjectName(_fromUtf8("actionSearch"))
        self.actionHome = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/Project/home_icon.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHome.setIcon(icon2)
        self.actionHome.setObjectName(_fromUtf8("actionHome"))
        self.actionSave = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/Project/save_icon.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon3)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionCut = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/Project/cut_icon.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut.setIcon(icon4)
        self.actionCut.setObjectName(_fromUtf8("actionCut"))
        self.actionCopy = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/Project/copy_icon2.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon5)
        self.actionCopy.setObjectName(_fromUtf8("actionCopy"))
        self.actionExit = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/Project/exit_icon.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon6)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionPaste = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/Project/paste.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaste.setIcon(icon7)
        self.actionPaste.setObjectName(_fromUtf8("actionPaste"))
        self.actionDelete = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/Project/delete.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete.setIcon(icon8)
        self.actionDelete.setObjectName(_fromUtf8("actionDelete"))
        self.actionNewfolder = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/Project/folder.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewfolder.setIcon(icon9)
        self.actionNewfolder.setObjectName(_fromUtf8("actionNewfolder"))
        self.actionHistory = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/Project/history.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHistory.setIcon(icon10)
        self.actionHistory.setObjectName(_fromUtf8("actionHistory"))
        self.actionRename = QtGui.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/Project/rename.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRename.setIcon(icon11)
        self.actionRename.setObjectName(_fromUtf8("actionRename"))
        self.toolBar.addAction(self.actionHome)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSettings_2)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionRename)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionHistory)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionDelete)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPaste)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCut)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCopy)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionNewfolder)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSearch)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExit)
        self.toolBar.addSeparator()
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuTools.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QObject.connect(self.actionSettings_2, QtCore.SIGNAL(_fromUtf8("triggered()")), self.toolBar.hide)
        QtCore.QObject.connect(self.commandLinkButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.toolBar.show)
        QtCore.QObject.connect(self.commandLinkButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.toolBar.hide)
        QtCore.QObject.connect(self.actionCopy, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.copy)
        QtCore.QObject.connect(self.actionPaste, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.paste)
        QtCore.QObject.connect(self.actionCut, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.cut)
        QtCore.QObject.connect(self.actionDelete, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.delete)
        QtCore.QObject.connect(self.actionRename, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.rename)
        QtCore.QObject.connect(self.actionNewfolder, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.newFolder)
        QtCore.QObject.connect(self.actionSearch, QtCore.SIGNAL(_fromUtf8("triggered()")), self.openSearch)
        QtCore.QObject.connect(self.actionHistory, QtCore.SIGNAL(_fromUtf8("triggered()")), self.openHistory)
        QtCore.QObject.connect(self.actionHome, QtCore.SIGNAL(_fromUtf8("triggered()")), self.searchtest)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.commandLinkButton.setText(_translate("MainWindow", "HideMenu", None))
        self.commandLinkButton_2.setText(_translate("MainWindow", "ShowMenu", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.menuTools.setTitle(_translate("MainWindow", "Tools", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionSettings.setText(_translate("MainWindow", "settings", None))
        self.actionSettings.setToolTip(_translate("MainWindow", "settings", None))
        self.actionSettings_2.setText(_translate("MainWindow", "settings", None))
        self.actionSettings_2.setToolTip(_translate("MainWindow", "Settings", None))
        self.actionSearch.setText(_translate("MainWindow", "search", None))
        self.actionSearch.setToolTip(_translate("MainWindow", "Search", None))
        self.actionHome.setText(_translate("MainWindow", "home", None))
        self.actionHome.setToolTip(_translate("MainWindow", "Home", None))
        self.actionSave.setText(_translate("MainWindow", "save", None))
        self.actionSave.setToolTip(_translate("MainWindow", "Save", None))
        self.actionCut.setText(_translate("MainWindow", "cut", None))
        self.actionCut.setToolTip(_translate("MainWindow", "Cut", None))
        self.actionCopy.setText(_translate("MainWindow", "copy", None))
        self.actionCopy.setToolTip(_translate("MainWindow", "Copy", None))
        self.actionExit.setText(_translate("MainWindow", "exit", None))
        self.actionExit.setToolTip(_translate("MainWindow", "Exit", None))
        self.actionPaste.setText(_translate("MainWindow", "paste", None))
        self.actionDelete.setText(_translate("MainWindow", "delete", None))
        self.actionNewfolder.setText(_translate("MainWindow", "newfolder", None))
        self.actionHistory.setText(_translate("MainWindow", "history", None))
        self.actionRename.setText(_translate("MainWindow", "rename", None))




    def copyScript(self):
        self.webView.load(QUrl('copy.html'))
        print 1
    def cutScript(self):
        self.webView.load(QUrl('cut.html'))
    def pasteScript(self):
        self.webView.load(QUrl('paste.html'))

    def searchtest(self):
        #sure searching here:
        def suresearcher(item,names):
            print names
            deleter=[]
            for unit in names:
                if not (item in unit):
                    print item +" is not in "+ unit
                    deleter.append(unit)
                else:
                    print  item +" is in " + unit
            for unit in deleter:
                names.remove(unit)
        test = searchclass()
        test.main()
        path=str(self.treeView.getFilePath())
        text1=test.text
        names=[]
        print path
        from os import walk
        f = {}
        def walker(f):
            for (dirpath, dirnames, filenames) in walk(path):
                print "dirpath"
                print dirpath
                print "dirnames"
                print dirnames
                print "filenames"
                print filenames
                dirpath=dirpath.replace("/","\\")
                for file in filenames:
                    if f.get(file,0):
                        f[file].append(dirpath+"\\"+file)
                    else:
                        f[file]=[dirpath+"\\"+file]
                    if (file[-4:]==".txt"):
                        print "txt found"
                        txt=open(dirpath+'\\'+file)
                        tmp=txt.readlines()
                        print "#########################"
                        print tmp
                        print type(tmp)
                        print "#########################"
                        if tmp!=[]:
                            if f.get(tmp[0],0):
                                f[tmp[0]].append(dirpath+"\\"+file)
                            else:
                                f[tmp[0]]=[dirpath+"\\"+file]
                        txt.close()
                for dir in dirnames:
                    if f.get(dir,0):
                        f[dir].append(dirpath+"\\"+dir)
                    else:
                        f[dir]=[dirpath+"\\"+dir]

        walkthread=Thread(target=walker,args=(f,))
        walkthread.start()


        def surer(text,names):
            text=str(text).split()
            for item in text:
                if names!=[]:
                    print "this item in for: "+item
                    suresearcher(item,names)
                    print "done"
            print "text is "
            print text
            print "names are"
            print  names

        #not searching here:
        def notsearcher(item,names):
            print names
            deleter=[]
            for unit in names:
                if (item in unit):
                    print item +" is  in "+ unit
                    deleter.append(unit)
                else:
                    print  item +" is not in " + unit
            for unit in deleter:
                names.remove(unit)

        test = searchclass()
        test.main()
        text2=test.text
        print path
        from os import walk
        def noter(text,names):
            text=str(text).split()
            for item in text:
                if names!=[]:
                    print "this item in for: "+item
                    notsearcher(item,names)
                    print "done"
            print "text is "
            print text
            print "names are"
            print  names

        #at least one searching here:
        def oncesearch(item,text,names,deleter):
            flag=False
            for unit in text:
                if unit in item:
                    flag=True
                    print "unit "+unit+ " is in item "+item
                    break
            if flag==False:
                deleter.append(item)

        test = searchclass()
        test.main()
        text3=test.text
        print path
        from os import walk
        def oncer(text,names):
            text=str(text).split()
            deleter=[]
            i=[]
            for item in names:
                if names!=[]:
                    print "this item in for: "+item
                    i.append(Thread(target=oncesearch,args=(item,text,names,deleter)))
                    i[-1].start()
                    #oncesearch(item,text,names,deleter)
                    print "done"
            for tred in i:
                tred.join()
            for unit in deleter:
                names.remove(unit)
        #showing results
        names=f.keys()
        surethread=Thread(target=surer,args=(text1,names))
        notthread=Thread(target=noter,args=(text2,names))
        oncethread=Thread(target=oncer,args=(text3,names))
        walkthread.join()
        print "f is this!!!!!:"
        print f
        print "with walk names are:"
        print names
        surethread.start()
        surethread.join()
        print "with suresearch names are:"
        print names
        notthread.start()
        notthread.join()
        print "with notsearch names are:"
        print names
        oncethread.start()
        oncethread.join()
        print "names are this: "
        print  names
        print "########################"
        for i in names:
            print "result "+i+"in location: "+str(f[i])


    def copy(self):
        print "copy"
        instance = self.treeView
        PATH = instance.getFilePath()
        file = open('DB.txt', "w")
        file.write(PATH)
        NAME = instance.getFileName()
        file.write("\n")
        file.write(NAME)
        file.write("\n")
        file.write("0")
        file.close()
        self.copyScript()


    def cut(self):
        print "cut"
        instance = self.treeView
        PATH = instance.getFilePath()
        file = open('DB.txt', "w")
        file.write(PATH)
        NAME = instance.getFileName()
        file.write("\n")
        file.write(NAME)
        file.write("\n")
        file.write("1")
        file.close()
        self.cutScript()

    def paste(self):
        print "paste"
        instance = self.treeView
        lastPATH = instance.getFilePath()
        file=open('DB.txt',"r")
        try:
            firstPATH=file.readline().strip()
            NAME=file.readline().strip()
            mode=file.readline()
            firstPATH=firstPATH.replace("/",'\\')
            lastPATH=str(lastPATH).replace("/",'\\')
            print firstPATH
            print NAME
            if(int(mode)==0):
                print "copy"
                if (os.path.isfile(str(firstPATH))):
                    print "file"
                    os.system("copy "+str(firstPATH)+" "+str(lastPATH))
                    print "copy "+str(firstPATH)+" "+str(lastPATH)
                else:
                    print "foldere"
                    os.system("md "+str(lastPATH)+'\\'+str(NAME))
                    print "md "+str(lastPATH)+'\\'+str(NAME)
                    os.system("copy "+str(firstPATH)+" "+str(lastPATH)+"\\"+str(NAME))
                    print "copy "+str(firstPATH)+" "+str(lastPATH)+"\\"+str(NAME)
                file.close()
            elif(int(mode)==1):
                print "cut"
                os.system("move "+str(firstPATH)+" "+str(lastPATH))
                print "move "+str(firstPATH)+" "+str(lastPATH)
                file.close()
        except:
            print "exception"

        self.pasteScript()

    def delete(self):
        instance =  self.treeView
        PATH = instance.getFilePath()
        new_path = str(PATH).replace('/', "\\")
        if (os.path.isfile(str(new_path))):

            if ' ' in str(new_path):

                os.system("DEL /F /Q /A " + '"' + str(new_path) + '"')

            else:

                os.system("DEL /F /Q /A " + str(new_path) )

        else:
            os.system('RD /S /Q ' + '"' + str(PATH) + '"')

    def newFolder(self):
        instance = self.treeView
        PATH = instance.getFilePath()
        new_path = str(PATH).replace('/', "\\")
        if (os.path.isfile((str(new_path)))):
            print "khodet khari"
        else:

            os.system("md " +'"' + str(new_path) + "\New folder" + '"' )

    def openSearch(self):
        MainWindow = QtGui.QMainWindow()
        ui = Search()
        ui.setupUi(MainWindow)
        MainWindow.show()
        Error      #put the error to stay in window :) :D :P


    def openHistory(self):
        MainWindow = QtGui.QMainWindow()
        ui = history_window()
        ui.setupUi(MainWindow)
        MainWindow.show()
        Error      #put the error to stay in window :) :D :P

    def rename(self):
        r_ins = Window()
        r_ins.main()
        new_name = r_ins.text

        instance = self.treeView
        PATH = instance.getFilePath()
        new_path = str(PATH).replace('/', "\\")
        if (os.path.isfile((str(new_path)))):
            print "REN" + '"' + str(new_path) + '"' + ' "' + str(new_name) + '"'
            extension = ""
            for i in range(len(new_path)-1,0,-1):
                if new_path[i] == '.':
                    break
                else:
                    extension += new_path[i]
            new_ext = "."
            for j in range(len(extension)):
                new_ext += extension[len(extension)-j-1]
            print new_ext

            os.system("REN " + '"' + str(new_path) + '"' + ' "' + str(new_name) + new_ext + '"' )


        else:

            os.system("md " +'"' + str(new_path) + "\New folder" + '"' )




from PyQt4 import QtWebKit
from QTree import Main
import iman_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    app.setWindowIcon(QtGui.QIcon("skymanager1.jpg"))
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

