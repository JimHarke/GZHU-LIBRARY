infos = [
    {
        'sno': '32264400003',         # 学号
        'pwd': '#*Zr5815jB',         # 密码
        'devName': '511-B16',   # 预约的座位号（不足3位数的要补零）
        'name': 'Mr.曾',        # 随便起个名字
        'periods': (            # 预约时间段（每段时间不能超过4小时）
            ('9:30:00', '12:30:00'),
            ('12:30:00', '16:30:00'),
            ('16:30:00', '20:30:00'),
            ('20:30:00', '21:45:00')
        ),
        'pushplus': '',         # pushplus 的 token（用于推送消息到微信）
    },

   
    # 如果只是一个人预约座位，不需要帮别人预约签到，则可把下面三个字典注释/删除
   #{
   #     'sno': '******',
   #     'pwd': '******',
   #     'devName': 'G101-008',
   #     'name': '皮卡丘',
   #     'periods': (
   #         ('8:30:00', '12:30:00'),
   #         ('12:30:00', '16:30:00'),
   #         ('16:30:00', '20:30:00'),
   #         ('20:30:00', '21:45:00')
   #     ),
   #     'pushplus': '',
   # }
]
