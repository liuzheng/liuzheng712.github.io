---
layout: post
title: "Median of Two Sorted Arrays"
description: ""
category: 
tags: [leetcode,python]
---
{% include JB/setup %}

这题<https://oj.leetcode.com/problems/median-of-two-sorted-arrays/>

    C=sorted(A+B)
    l = len(C)
    if l%2==0:
        return float(C[l/2-1]+C[l/2])/2
    else:
        return C[l/2]

