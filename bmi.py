height = float(input("请输入你的身高（米），例如 1.75:"))
weight = float(input("请输入你的体重（公斤），例如 65:"))
bmi = weight/(height**2)
print("你的 BMI 是：",bmi)
if bmi <18.5:
    print("偏瘦")
elif bmi <24:
    print("正常")
elif bmi <28:
    print("偏胖")
else: 
    print("肥胖")
print("记得多运动")
    