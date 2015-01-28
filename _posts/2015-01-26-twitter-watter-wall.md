---
layout: post
title: "twitter 面试题，水墙"
description: ""
category: 
tags: [twitter, interview]
---
{% include JB/setup %}
刚才看微信推荐说了一道twitter的面试题，题目链接<http://blog.jobbole.com/50705>

题目中对方提到可以使用`更有意思的一次遍历`，我就提起兴趣了

下面是我的代码，真的只用一次遍历哦！

还是先不看代码吧。。。

分析：

这题相当容易想到微积分，然后就会死在积分求面积上，可是这是离散数学，且具体问题具体分析！

问题是问水在什么情况下可以聚集？我反过来，水在那个短板会流掉？

那么就容易分析了，左边最高墙开始计数，直到比左边最高墙高的墙计数完毕，所得坑中水归入总值中，得`code1`，思想就是算斜率，对比前后墙面高度进行情况判断。经过我再次回顾分析，发现如果出现多坑的情况，那么这货就废了，故思去考`code2`，暂时先去吃饭，不思考了。。。

`code1`适用于题列中的一个坑的情况。

昨天回去测试了别人的代码，哎，各种忧伤，效率和别人差4倍，还有bug。。。

`code1`

    def twitter(list):
        trig = 0
        sum = 0
        tmp = 0
        max = list[0]
        for i in list[1:]:
            rest = max - i
            if max < i:
                max = i
            if rest < 0:
                rest = 0
            if trig == 1 and rest == 0:
                sum = sum + tmp
                tmp = 0
                trig = 0
            else:
                trig = 1
                tmp = tmp + rest
        return sum
    
    if __name__ == "__main__":
        list = [2,5,1,3,1,2,1,7,7,6]
        print twitter(list)
