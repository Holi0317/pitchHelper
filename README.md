pitchHelper
===========

用來方(作)便(弊)mswLogo音樂創作的工具

系統需求
========
Windows / Mac / GNU/Linux / Unix-like 作業系統\n
Python 3  (注: 可在python2中執行, 但是會出現計算結果錯誤, 這是一個已知的bug)\n
Tkinter (windows用戶可以無視, Linux用戶請自行apt-get / yum / pacman一下)

使用方法
========
BPM: 填入BPM\n
左邊數字: 選擇音的高低  (選擇0-2時, logo好像不會順利播出, 原因應該是超出聆聽範圍, 建議最少選3)\n
第二行: 選擇音 (這還不會看-.-)\n
第三行: 選擇長度, 4為一個小節, 2為半個, 如此類推\n
rest: 讀取第三行的內容, 等待相等的時間\n
add: 加入已讀取的音\n
final: 輸出結果, 並抄進剪貼簿中\n
\n
把結果抄進mswlogo中, 就可以播放了 :D\n

已知的bug
=========
音調和長度是有關系的, 但不會計算, 所以不會修復-3-\n
Python2中, 計算會出現錯誤\n

To-do
=====
增加存檔/讀檔功能
整理原始碼, 使用OOP來編程(現在好難讀-.-)
增加選取midi檔的功能
