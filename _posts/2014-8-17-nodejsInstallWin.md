---
layout: post
title: "Node for windows Install"
tagline: ""
description: ""
category: Node
tags: [Node, guide]
---
{% include JB/setup %}

# ��װ Node ����
## ����NodeJs
ǰ�� http://nodejs.org/download/ ����node ���°汾������ѡ��exe�汾������ϲ����������

## ����Ŀ¼
����D:\dev\nodejsĿ¼������node.exe���������Ŀ¼�С�����"D:\dev\nodejs"����ϵͳ��������PATH�У�����������λ��ִ��nodeӦ�á�

## ����npmԴ���룺
    cd  /D/dev/nodejs
	git clone https://github.com/npm/npm --depth 1
	node cli.js install -gf
   ������Ҫע��һ�£���д��ƪ����ʱnpm���°汾Ϊ1.0.106������������°汾��1.0.105��Windowsƽ̨�¶������⡣������ѡ���˰�װ1.0.104�汾��
   https://github.com/isaacs/npm/zipball/v1.0.104