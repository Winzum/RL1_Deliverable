# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deliverable_4.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QListWidget, QDialog
import pandas
import datetime
import webbrowser

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.weekbox = QtWidgets.QGroupBox(self.centralwidget)
        self.weekbox.setGeometry(QtCore.QRect(-1, 69, 1921, 961))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Typewriter")
        font.setPointSize(24)
        self.weekbox.setFont(font)
        self.weekbox.setAlignment(QtCore.Qt.AlignCenter)
        self.weekbox.setObjectName("weekbox")
        self.widget = QtWidgets.QWidget(self.weekbox)
        self.widget.setGeometry(QtCore.QRect(0, 20, 1921, 91))
        self.widget.setObjectName("widget")
        self.gridLayout__daylabels = QtWidgets.QGridLayout(self.widget)
        self.gridLayout__daylabels.setContentsMargins(0, 0, 0, 0)
        self.gridLayout__daylabels.setObjectName("gridLayout__daylabels")
        self.monday_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.monday_label.setFont(font)
        self.monday_label.setAlignment(QtCore.Qt.AlignCenter)
        self.monday_label.setObjectName("monday_label")
        self.gridLayout__daylabels.addWidget(self.monday_label, 0, 0, 1, 1)
        self.tuesday_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.tuesday_label.setFont(font)
        self.tuesday_label.setAlignment(QtCore.Qt.AlignCenter)
        self.tuesday_label.setObjectName("tuesday_label")
        self.gridLayout__daylabels.addWidget(self.tuesday_label, 0, 1, 1, 1)
        self.friday_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.friday_label.setFont(font)
        self.friday_label.setAlignment(QtCore.Qt.AlignCenter)
        self.friday_label.setObjectName("friday_label")
        self.gridLayout__daylabels.addWidget(self.friday_label, 0, 4, 1, 1)
        self.thursday_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.thursday_label.setFont(font)
        self.thursday_label.setAlignment(QtCore.Qt.AlignCenter)
        self.thursday_label.setObjectName("thursday_label")
        self.gridLayout__daylabels.addWidget(self.thursday_label, 0, 3, 1, 1)
        self.wednesday_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.wednesday_label.setFont(font)
        self.wednesday_label.setAlignment(QtCore.Qt.AlignCenter)
        self.wednesday_label.setObjectName("wednesday_label")
        self.gridLayout__daylabels.addWidget(self.wednesday_label, 0, 2, 1, 1)
        self.saturday_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.saturday_label.setFont(font)
        self.saturday_label.setAlignment(QtCore.Qt.AlignCenter)
        self.saturday_label.setObjectName("saturday_label")
        self.gridLayout__daylabels.addWidget(self.saturday_label, 0, 5, 1, 1)
        self.sunday_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.sunday_label.setFont(font)
        self.sunday_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sunday_label.setObjectName("sunday_label")
        self.gridLayout__daylabels.addWidget(self.sunday_label, 0, 6, 1, 1)
        self.widget1 = QtWidgets.QWidget(self.weekbox)
        self.widget1.setGeometry(QtCore.QRect(0, 110, 1921, 851))
        self.widget1.setObjectName("widget1")
        self.gridLayout_weeklists = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_weeklists.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_weeklists.setObjectName("gridLayout_weeklists")
        self.listWidget_monday = QtWidgets.QListWidget(self.widget1)
        self.listWidget_monday.setObjectName("listWidget_monday")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(16)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(223, 223, 223))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 62, 62))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.listWidget_monday.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(28)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        self.listWidget_monday.addItem(item)
        self.gridLayout_weeklists.addWidget(self.listWidget_monday, 0, 0, 1, 1)
        self.listWidget_tuesday = QtWidgets.QListWidget(self.widget1)
        self.listWidget_tuesday.setObjectName("listWidget_tuesday")
        self.gridLayout_weeklists.addWidget(self.listWidget_tuesday, 0, 1, 1, 1)
        self.listWidget_wednesday = QtWidgets.QListWidget(self.widget1)
        self.listWidget_wednesday.setObjectName("listWidget_wednesday")
        self.gridLayout_weeklists.addWidget(self.listWidget_wednesday, 0, 2, 1, 1)
        self.listWidget_thursday = QtWidgets.QListWidget(self.widget1)
        self.listWidget_thursday.setObjectName("listWidget_thursday")
        self.gridLayout_weeklists.addWidget(self.listWidget_thursday, 0, 3, 1, 1)
        self.listWidget_friday = QtWidgets.QListWidget(self.widget1)
        self.listWidget_friday.setObjectName("listWidget_friday")
        self.gridLayout_weeklists.addWidget(self.listWidget_friday, 0, 4, 1, 1)
        self.listWidget_saturday = QtWidgets.QListWidget(self.widget1)
        self.listWidget_saturday.setObjectName("listWidget_saturday")
        self.gridLayout_weeklists.addWidget(self.listWidget_saturday, 0, 5, 1, 1)
        self.listWidget_sunday = QtWidgets.QListWidget(self.widget1)
        self.listWidget_sunday.setObjectName("listWidget_sunday")
        self.gridLayout_weeklists.addWidget(self.listWidget_sunday, 0, 6, 1, 1)
        self.previous_button = QtWidgets.QPushButton(self.centralwidget)
        self.previous_button.setGeometry(QtCore.QRect(0, 0, 141, 81))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(18)
        self.previous_button.setFont(font)
        self.previous_button.setObjectName("previous_button")
        self.next_button = QtWidgets.QPushButton(self.centralwidget)
        self.next_button.setGeometry(QtCore.QRect(1780, 0, 141, 81))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(18)
        self.next_button.setFont(font)
        self.next_button.setObjectName("next_button")
        self.UULogo = QtWidgets.QLabel(self.centralwidget)
        self.UULogo.setGeometry(QtCore.QRect(1520, -10, 261, 111))
        self.UULogo.setText("")
        self.UULogo.setPixmap(QtGui.QPixmap("UU_logo_EN_BLACK.png"))
        self.UULogo.setScaledContents(True)
        self.UULogo.setObjectName("UULogo")
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget3 = QtWidgets.QWidget(self.centralwidget)
        self.widget3.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.widget3.setObjectName("widget3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 21))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionInfo = QtWidgets.QAction(MainWindow)
        self.actionInfo.setObjectName("actionInfo")
        self.menuAbout.addAction(self.actionInfo)
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
        self.actionInfo.triggered.connect(lambda: self.info_popup())

        self.main_df = open_excel_df("LeidseRijnNieuws_articles.xlsx")
        self.start_week_date = self.main_df.iloc[0]['date'] + datetime.timedelta(days = 1)
        self.end_week_date = ""
        self.articles_df = ""
        self.select_previous_week()

        #connect previous button to the selection ofthe previous week
        ui.retitle_labels()
        self.previous_button.clicked.connect(self.select_previous_week)
        self.next_button.clicked.connect(self.select_next_week)

        #adding event listeners to articles
        self.listWidget_monday.itemDoubleClicked.connect(lambda: self.showPopup(self.listWidget_monday))
        self.listWidget_tuesday.itemDoubleClicked.connect(lambda: self.showPopup(self.listWidget_tuesday))
        self.listWidget_wednesday.itemDoubleClicked.connect(lambda: self.showPopup(self.listWidget_wednesday))
        self.listWidget_thursday.itemDoubleClicked.connect(lambda: self.showPopup(self.listWidget_thursday))
        self.listWidget_friday.itemDoubleClicked.connect(lambda: self.showPopup(self.listWidget_friday))
        self.listWidget_saturday.itemDoubleClicked.connect(lambda: self.showPopup(self.listWidget_saturday))
        self.listWidget_sunday.itemDoubleClicked.connect(lambda: self.showPopup(self.listWidget_sunday))


    def info_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("About")
        msg.setText("This program was created by Lennart van Winzum\nUtrecht University")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setInformativeText("Research Lab 1")
        x = msg.exec_()

    def showPopup(self, QListWidget):
        msg = QMessageBox()
        #print(self.articles_df)
        current_entry = self.articles_df.loc[self.articles_df['title'] == QListWidget.currentItem().text()]
        for index, row in current_entry.iterrows():
            #print(row)
            msg.setWindowTitle("Artikel")
            print(row['url'])
            msg.setText(row['title'])
            #msg.setIcon(QMessageBox.information)
            url= str(row['url'])
            msg.setStandardButtons(QMessageBox.Open|QMessageBox.Close)
            msg.setDefaultButton(QMessageBox.Close)
            msg.setInformativeText(str(int(row['Like'])) + " Likes")
            msg.setDetailedText(row['content'])
            msg.accepted.connect(lambda: self.open_url(url))
            #msg.buttonClicked.connect(self.popup_button)
            x = msg.exec_()

    def open_url(self, url):
        webbrowser.open_new(url)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.weekbox.setTitle(_translate("MainWindow", "Week"))
        self.monday_label.setText(_translate("MainWindow", "Monday\ndate"))
        self.tuesday_label.setText(_translate("MainWindow", "Tuesday\ndate"))
        self.friday_label.setText(_translate("MainWindow", "Friday\ndate"))
        self.thursday_label.setText(_translate("MainWindow", "Thursday\ndate"))
        self.wednesday_label.setText(_translate("MainWindow", "Wednesday\ndate"))
        self.saturday_label.setText(_translate("MainWindow", "Saturday\ndate"))
        self.sunday_label.setText(_translate("MainWindow", "Sunday\ndate"))
        __sortingEnabled = self.listWidget_monday.isSortingEnabled()
        self.listWidget_monday.setSortingEnabled(False)
        item = self.listWidget_monday.item(0)
        item.setText(_translate("MainWindow", "Popular Article"))
        item = self.listWidget_monday.item(1)
        item.setText(_translate("MainWindow", "Unpopular Article"))
        self.listWidget_monday.setSortingEnabled(__sortingEnabled)
        self.previous_button.setText(_translate("MainWindow", "Previous"))
        self.previous_button.setShortcut(_translate("MainWindow", "Left"))
        self.next_button.setText(_translate("MainWindow", "Next"))
        self.next_button.setShortcut(_translate("MainWindow", "Right"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionInfo.setText(_translate("MainWindow", "Info"))
        self.actionInfo.setStatusTip(_translate("MainWindow", "This shows you the info about the creators"))
        self.actionInfo.setShortcut(_translate("MainWindow", "Ctrl+I"))

    def retitle_labels(self):
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        months = ["January", "February", "March", "April", "May","June", "July", "August", "September", "October", "November", "December"]

        #empty all labels
        self.monday_label.setText("")
        self.tuesday_label.setText("")
        self.wednesday_label.setText("")
        self.thursday_label.setText("")
        self.friday_label.setText("")
        self.saturday_label.setText("")
        self.sunday_label.setText("")

        #empty all lists
        self.listWidget_monday.clear()
        self.listWidget_tuesday.clear()
        self.listWidget_wednesday.clear()
        self.listWidget_thursday.clear()
        self.listWidget_friday.clear()
        self.listWidget_saturday.clear()
        self.listWidget_sunday.clear()
        
        #pick year for first and change text of
        year = str(self.articles_df.iloc[0]['date'])[:4]
        self.weekbox.setTitle(year)

        for index, row in self.articles_df.iterrows():
            wday = (row['date']).weekday()
            day = str(int(str(row['date'])[8:10]))

            month = int(str(row['date'])[5:7]) - 1
            month = months[month]

            #monday
            if wday == 0:
                self.monday_label.setText("Monday\n" + month + " " +  day)
                #generate item first, then add it to the list
                
                
                self.listWidget_monday.addItem(self.generate_item(row))

                #add entry for current article 
                #self.listWidget_monday.addItem(row['title'])
                #change color and size based on inverse popularity
                #count = self.listWidget_monday.count()
                #self.listWidget_monday.item(self.listWidget_monday.currentItem()).setText("test")

                

            #tuesday
            if wday == 1:
                self.tuesday_label.setText("Tuesday\n" + month + " " +  day)
                #add entry for current article 
                self.listWidget_tuesday.addItem(self.generate_item(row))
                #change color and size based on inverse popularity
                #self.calculate_popularity(row)


            #wednesday
            if wday == 2:
                self.wednesday_label.setText("Wednesday\n" + month + " " +  day)
                #add entry for current article 
                self.listWidget_wednesday.addItem(self.generate_item(row))
                #change color and size based on inverse popularity


            #thursday
            if wday == 3:
                self.thursday_label.setText("Thursday\n" + month + " " +  day)
                #add entry for current article 
                self.listWidget_thursday.addItem(self.generate_item(row))
                #change color and size based on inverse popularity
            #friday
            if wday == 4:
                self.friday_label.setText("Friday\n" + month + " " +  day)
                #add entry for current article 
                self.listWidget_friday.addItem(self.generate_item(row))
                #change color and size based on inverse popularity

            #saturday
            if wday == 5:
                self.saturday_label.setText("Saturday\n" + month + " " +  day)
                #add entry for current article 
                self.listWidget_saturday.addItem(self.generate_item(row))
                #change color and size based on inverse popularity
            #sunday
            if wday == 6:
                self.sunday_label.setText("Sunday\n" + month + " " +  day)
                #add entry for current article 
                self.listWidget_sunday.addItem(self.generate_item(row))
                #change color and size based on inverse popularity


    def generate_item(self, row):
        item = QtWidgets.QListWidgetItem()
        likes = row['Like']
        #print(row['Like'])
        font = QtGui.QFont()
        if likes < 10: 
            font.setPointSize(30)
            brush = QtGui.QBrush(QtGui.QColor(116, 255, 65))
        elif likes < 50:
            font.setPointSize(26)
            brush = QtGui.QBrush(QtGui.QColor(115, 231, 127))
        elif likes < 100:
            font.setPointSize(22)
            brush = QtGui.QBrush(QtGui.QColor(169, 218, 151))
        elif likes < 200:
            font.setPointSize(16)
            brush = QtGui.QBrush(QtGui.QColor(167, 185, 160))
        else:
            font.setPointSize(12)
            brush = QtGui.QBrush(QtGui.QColor(164, 164, 164))

        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setFont(font)
        
        item.setBackground(brush)
        
        
        
        # brush = QtGui.QBrush(QtGui.QColor(62, 62, 62))
        # brush.setStyle(QtCore.Qt.SolidPattern)
        # item.setForeground(brush)
        item.setText(row['title'])
        return item

    def select_previous_week(self):
        day = datetime.timedelta(days=1)
        start_date = self.start_week_date - day
        
        while (start_date - day).weekday() != 6:
            start_date = start_date - day

        mask = (self.main_df['date'] >= start_date) & (self.main_df['date'] < self.start_week_date)
        self.articles_df = self.main_df.loc[mask]

        if self.articles_df.empty:
            self.start_week_date = start_date

            self.select_previous_week()
        

        print(self.articles_df.head)

        self.start_week_date = start_date
        self.end_week_date = start_date + datetime.timedelta(days = 6)
        print(self.start_week_date)
        print(self.end_week_date)
        self.retitle_labels()
        
        
    def select_next_week(self):
        day = datetime.timedelta(days=1)
        #calculate ending date
        end_date = self.end_week_date + day
        
        while (end_date + day).weekday() != 0:
            end_date = end_date + day
        
        mask = (self.main_df['date'] > self.end_week_date) & (self.main_df['date'] <=end_date)
        self.articles_df = self.main_df.loc[mask]

        if self.articles_df.empty:
            self.end_week_date = end_date
            self.select_next_week()

        print(self.articles_df.head)
        self.end_week_date = end_date + day
        self.start_week_date = end_date - datetime.timedelta(days = 6)
        self.retitle_labels()

"""retrieves dataframe from local excelfile"""
def open_excel_df(fn):
    df = pandas.ExcelFile.parse(pandas.ExcelFile(fn))
    df['date'] = pandas.to_datetime(df['date'], format= f'%d-%m-%Y')
    df = df.sort_values(['date'], ascending = False)
    return df

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
