import cv2
import numpy as np
import matplotlib.pyplot as plt
rup = cv2.imread('triangle.jpg')
#rup_in = cv2.bitwise_not(rup)
rup = cv2.cvtColor(rup,cv2.COLOR_BGR2GRAY)
contour,hist = c(rup,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(len(contour[0])) # ได้ 362
plt.imshow(cv2.cvtColor(rup,cv2.COLOR_GRAY2RGB))
x = contour[0][:,0,0]
y = contour[0][:,0,1]
plt.scatter(x,y,s=10,c='m')
plt.show()

'''miku_gr = cv2.cvtColor(miku,cv2.COLOR_BGR2GRAY) # แปลงเป็นขาวดำ
_,miku_thr = cv2.threshold(miku_gr,10,255,0)
# หาเส้นเค้าโครง
contour,_ = cv2.findContours(miku_thr,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
# วาดเส้นเค้าโครงลงบนภาพเดิม
for i in range(len(contour)):
    miku = cv2.drawContours(miku,contour,i,(0,200,0),2)
cv2.imwrite('miku13c02.jpg',miku)
'''
'''contourArea = cv2.contourArea(contour)
ax = plt.gca(aspect=1,xlim=[-3,3],ylim=[4,-1])
plt.title('อาณาเขต = %.2f ตารางพิกเซล'%contourArea,family='Tahoma')
ax.add_patch(plt.Polygon(cnt[:,0],fc='y',ec='k'))
plt.grid(ls=':',c='r')
plt.show()'''