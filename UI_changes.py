
from aqt import mw
from aqt.utils import showInfo, qconnect
from aqt.qt import *

def display_kanji() -> None:
    showInfo("This is were the kanji heatmap will be displayed")

# create a new menu item
action = QAction("Kanji heatmap", mw)
# set it to call display_kanji when it's clicked
qconnect(action.triggered, display_kanji())
# and add it to the tools menu
mw.form.menuTools.addAction(action)
