# 水の呼吸-第十二型-瑟瑟盡除
111213012 郭方朔
111213013 潘劭穎
111213015 蔡昇佑
111213035 羅智穎
111213066 蔡家生
111213081 譚皓宇

## Concept Development

<!-- Why does your team want to build this idea/project?  -->
11月NNN挑戰總是失敗還沒成功過，於是我們想提供那些一樣都是失敗的人提供一個可以有效解決問題的方式，我們沒辦法解決慾望的問題所以我們就想辦法解決有問題的人，水槍的水可以幫使用者降降火，藉由此來阻止做清槍的部分

## Implementation Resources

<!-- e.g., How many Raspberry Pi? How much you spent on these resources? -->
硬體設備：樹莓派、水槍、MOSFET、麵包板、杜邦線、電池、電風扇、一塊錢

## Existing Library/Software

<!-- Which libraries do you use while you implement the project -->

## Implementation Process

<!-- What kind of problems you encounter, and how did you resolve the issue? -->

## Knowledge from Lecture

<!-- What kind of knowledge did you use on this project? -->
Raspberry Pi 3環境設置  
Raspberry Pi 輸出訊號  
Raspberry Pi 腳本設計  
windows default gateway 設置  
linux 防火牆設置  
電晶體接法  
IP查詢
  

## Installation

<!-- How do the user install with your project? -->
防火牆設定：

找A片IP：
1.先搜尋網站並擷取發光的網址 EX:下圖google.com這段  
![image](https://github.com/user-attachments/assets/482c0fa0-2c4e-4209-9576-0c740ceb0ba2)  
2.去CMD用nslookup去尋找ip位置

硬體電路：
1. 將 MOSFET 線插在麵包板上面，每個腳位要在不同的線路上。下圖為 MOSFET 的三個腳位。
![image](https://github.com/user-attachments/assets/e01f7153-f6b0-44af-90c0-5ce4a75ea38b)
2. PI 的 GPIO 接上腳位 G。
3. 水槍的負極接上腳位 D。
4. PI 的接地線接上腳位 S。
5. 電池正極接上水槍的正極。
6. 電池負極接上腳位 S。
最終電路圖如下：
![image](https://github.com/user-attachments/assets/5cd73c2c-f89d-4ecf-a5df-f848524f9f5e)

## Usage

<!-- How to use your project -->
當你查詢被禁止的網站時旁邊的水槍就會開始發射，如果網站都沒關掉會持續發射水柱直到你關掉網站或是電池沒電

## Job Assignment
111213012 郭方朔:查A片  
111213013 潘劭穎:想題目、腳本設計/測試、規則設計/測試  
111213015 蔡昇佑:想題目、電路設計、github編寫  
111213035 羅智穎:想題目、設備處理、初始環境設置、被顏射  
111213066 蔡家生:想題目、提供設備、簡報製作、github編寫  
111213081 譚皓宇:想題目、硬體技術  
## References
https://raspberrytw.tumblr.com/post/48939062042/raspberry-pi-lirc-implement
https://raspberrypi.stackexchange.com/questions/70931/how-do-i-do-a-basic-mosfet-switch-with-pi
https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.lesics.com%2Fhow-does-a-mosfet-work.html&psig=AOvVaw2MxxZidanqnzb0kbDMFeR3&ust=1735886471080000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCOjzp5e31ooDFQAAAAAdAAAAABAE
https://raspberrytw.tumblr.com/post/48939062042/raspberry-pi-lirc-implement  
https://hackmd.io/Sd59QRjvRHGNSpyHHdpccg

