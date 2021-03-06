jobs_btn_redo_style = '''
    QPushButton {
        color: white;
        background-color: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #38d,
            stop: 0.1 #93e, stop: 0.49 #77c, stop: 0.5 #16b, stop: 1 #07c);
        border-width: 1px;
        border-color: #339;
        border-style: solid;
        border-radius: 7;
        padding: 3px;
        font-size: 13px;
        padding-left: 5px;
        padding-right: 5px;
        min-width: 20px;
        min-height: 14px;
        max-height: 14px;
    }
'''
jobs_btn_completed_style = '''
    QPushButton {
        color: white;
        background-color: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #18d,
            stop: 0.1 #9ae, stop: 0.49 #97c, stop: 0.5 #16b, stop: 1 #77c);
        border-width: 1px;
        border-color: #339;
        border-style: solid;
        border-radius: 7;
        padding: 3px;
        font-size: 13px;
        padding-left: 5px;
        padding-right: 5px;
        min-width: 20px;
        min-height: 14px;
        max-height: 14px;
    }
'''
jobs_btn_processing_style = '''
    QPushButton {
        color: white;
        background-color: QLinearGradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(9, 41, 4, 255), stop:0.085 rgba(2, 79, 0, 255), stop:0.19 rgba(50, 147, 22, 255), stop:0.275 rgba(236, 191, 49, 255), stop:0.39 rgba(243, 61, 34, 255), stop:0.555 rgba(135, 81, 60, 255), stop:0.667 rgba(121, 75, 255, 255), stop:0.825 rgba(164, 255, 244, 255), stop:0.885 rgba(104, 222, 71, 255), stop:1 rgba(93, 128, 0, 255));
        border-width: 1px;
        border-color: #339;
        border-style: solid;
        border-radius: 7;
        padding: 3px;
        font-size: 13px;
        padding-left: 5px;
        padding-right: 5px;
        min-width: 20px;
        min-height: 14px;
        max-height: 14px;
    }
'''

qssStyle = '''
    QPushButton {
        background-color: rgba(255, 130, 71, 100);
    }
    #table_share, #table_jobs, #table_disk, #table_rec {
        background-color: rgba(255, 255, 255, 150);
    }
    QTabWidget::pane {
        border: 1px;
        /* background:transparent;  # 完全透明 */
        background-color: rgba(255, 255, 255, 100);
    }
    QTabWidget::tab-bar {
        background:transparent;
        subcontrol-position:center;
    }
    QTabBar::tab {
        min-width:150px;
        min-height:30px;
        background:transparent;
    }
    QTabBar::tab:selected {
        color: rgb(153, 50, 204);
        background:transparent;
        font-weight:bold;
    }
    QTabBar::tab:!selected {
        color: rgb(28, 28, 28);
        background:transparent;
    }
    QTabBar::tab:hover {
        color: rgb(0, 0, 205);
        background:transparent;
    }
    #MainWindow {
        border-image:url(./src/default_background_img.jpg);
    }
    #tabWidget QTabBar{
        background-color: #AEEEEE;
    }
    #statusbar {
        font: 14px;
        color: white;
    }
    #msg_label, #msg_movie_lb {
        font: 14px;
        color: white;
        background:transparent;
    }
'''
