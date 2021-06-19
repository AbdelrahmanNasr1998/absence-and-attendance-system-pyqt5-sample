stylesheet = """

        QWidget{
            background: #262d37;
            border: 0px solid #262d37;
            padding: 5px 5px 5px 5px;
            font-family: 'Tajawal', sans-serif;
            font-size:15px
        }
        QTableWidgetItem
        {
            color:#fff
        }
        QGroupBox
        {
            padding-bottom:5px;
            color:#fff;
            font-size: 9pt;
        }
        QGridLayout
        {
            
        }
        QLabel{
            color: #fff;
        }
        QLabel#round_count_label, QLabel#highscore_count_label{
            border: 1px solid #fff;
            border-radius: 8px;
            padding: 2px;
        }
        QPushButton
        {
            margin-top:5px;
            color: white;
            background: #0577a8;
            border: 1px #DADADA solid;
            padding: 5px 10px;
            border-radius: 2px;
            font-weight: bold;
            font-size: 8pt;
            outline: none;
            font-family: 'Tajawal', sans-serif;
            font-size:15px
        }
        QPushButton:hover{
            border: 1px #C6C6C6 solid;
            color: #fff;
            background: #deab04;
        }
        QLineEdit {
            padding: 1px;
            color: #fff;
            border-style: solid;
            border: 2px solid #0577a8;
            border-radius: 8px;
        }
        QComboBox
        {
            padding: 1px;
            color: #fff;
            border-style: solid;
            border: 2px solid #0577a8;
            border-radius: 8px;
        }
        QComboBox::drop-down{
            border:none;
            background-color: #0577a8;
            color: rgb(255, 255, 255);
            font-weight:bold;
            padding:0px;
        }
        QListView{
            border: none;
            color:#fff;
            background-color:#0577a8;
            font-weight:bold;
            selection-color:#262d37;
            selection-background-color:#deab04;
            show-decoration-selected: 1;
            margin-left:-10px;
            padding-left: 15px;
        }
        QListView::item:hover{
            background-color: rgb(47, 175, 178);
            border:none;
        }
        QPlainTextEdit
        {
            margin-top:5px;
            padding: 1px;
            color: #fff;
            border-style: solid;
            border: 2px solid #0577a8;
            border-radius: 8px;
        }

"""