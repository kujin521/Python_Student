# @Time :2019/6/18 0018 17:41
# @Author:库金
USB_VS_RMB=6.77
rmb_value=input('请输入带单位（r/u）金额：')
r_u=rmb_value[-1:]
rmb_value=eval(rmb_value[:-1])
if r_u=='r':
    print('转化为美元为：', rmb_value / USB_VS_RMB)
elif r_u=='u':
    print('转化为人名币为：',rmb_value*USB_VS_RMB)
else:
    print('输入非法')