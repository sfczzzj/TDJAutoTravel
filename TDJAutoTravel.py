import basefunc
import time
import AntiCheck
import datetime
import random
# 1058 1218

x = 1218
y = 650
d = 160
h = 170

def SendTeam():
	basefunc.Log("开始派遣游历")
	i = 0
	ret = None
	while (ret == None):
		ret = basefunc.FindAndClick(10, 50, 1430, 780, "SendPeople.png", 0.9)
		if (ret == None):
			i = i + 1
			AntiCheck.RandomSleep(5)
		if (i > 5):
			basefunc.Log("未找到前往按键，异常")
			return
		
	AntiCheck.RandomSleep(5)
	
	i = 0
	while (i < 10):
		AntiCheck.RangeSwipe(1200, 750, 20, 200, 750, 20)
		i = i + 1
		
	AntiCheck.RandomSleep(6)
		
	for i in range(0, 5):
		ret = basefunc.FindImageInRect(x - d * i, y, x + d - d * i, y + h, "AlreadySend.png", 0.9)
		if (ret == None):
			AntiCheck.RangeClick(x - d * i + (d / 2), y + (h / 2), 3);
			AntiCheck.RandomSleep(5)
			break
		
	ret = basefunc.FindAndClick(10, 50, 1430, 780, "Go.png", 0.9)
	if (ret == None):
		basefunc.Log("未找到出行按键，异常")
		return

	basefunc.Log("派遣出行")
	AntiCheck.RandomSleep(6)

basefunc.GetBaseRect("天地劫：幽城再临 - MuMu模拟器")

while(True):

	basefunc.Log("等待完成游历")
	ret = None
	while (ret == None):
		AntiCheck.RandomSleep(4)
		ret = basefunc.FindImageInRect(710, 440, 770, 500, "FinishTravel.png", 0.9)
		
	basefunc.Log("发现已完成游历")
	AntiCheck.RandomSleep(5)
	AntiCheck.RangeClick(735, 470, 3);
	AntiCheck.RandomSleep(7)
		
	basefunc.Log("等待领取按键")
	ret = None
	while (ret == None):
		AntiCheck.RandomSleep(6)
		ret = basefunc.FindAndClick(770, 730, 970, 810, 'ConfirmRecv.png', 0.9)
		if (ret != None):
			basefunc.Log("领取完毕，等待画境或后续领取界面")
			ret = None
		AntiCheck.RandomSleep(6)
		ret = basefunc.FindImageInRect(560, 470, 750, 550, 'WorldInScroll.png', 0.9)
		
	basefunc.Log("领取完毕，回到画境，开始查找叹号")
	
	#益州
	ret = basefunc.FindImageInRect(100, 490, 200, 550, 'Notice.png', 0.9)
	if (ret != None):
		AntiCheck.RandomSleep(3)
		basefunc.Log("益州可派遣游历")
		AntiCheck.RangeClick(150, 600, 3);
		AntiCheck.RandomSleep(5)
		SendTeam()
		
	#成都
	ret = basefunc.FindImageInRect(100, 170, 200, 350, 'Notice.png', 0.9)
	if (ret != None):
		AntiCheck.RandomSleep(3)
		basefunc.Log("成都可派遣游历")
		AntiCheck.RangeClick(130, 260, 3);
		AntiCheck.RandomSleep(5)
		SendTeam()
	
	#洛阳
	ret = basefunc.FindImageInRect(730, 110, 820, 290, 'Notice.png', 0.9)
	if (ret != None):
		AntiCheck.RandomSleep(3)
		basefunc.Log("洛阳可派遣游历")
		AntiCheck.RangeClick(765, 210, 3);
		AntiCheck.RandomSleep(5)
		SendTeam()
	
	#临安
	ret = basefunc.FindImageInRect(1310, 190, 1420, 390, 'Notice.png', 0.9)
	if (ret != None):
		AntiCheck.RandomSleep(3)
		basefunc.Log("临安可派遣游历")
		AntiCheck.RangeClick(1360, 310, 3);
		AntiCheck.RandomSleep(5)
		SendTeam()
	
	#建阳
	ret = basefunc.FindImageInRect(1110, 530, 1250, 740, 'Notice.png', 0.9)
	if (ret != None):
		AntiCheck.RandomSleep(3)
		basefunc.Log("建阳可派遣游历")
		AntiCheck.RangeClick(1160, 650, 3);
		AntiCheck.RandomSleep(5)
		SendTeam()
	
	
	
	
	