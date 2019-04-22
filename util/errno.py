err_pro_type = {
    0: "验证错误",
    1: "业务错误",
}

errno_mess = {
    0: "成功",
    -10001: "数据错误",
    -10002: "数据格式错误",
    -10003: "数据内容错误",
    -10004: "数据类型错误",
    -10005: "无解密数据",

    -10101: "字段错误",
    -10102: "字段格式错误",
    -10103: "字段内容错误",
    -10104: "字段类型错误",
    -10105: "缺少字段",
    -10106: "缺少字段或者字段内容错误",
    -10107: "缺少字段或者字段格式错误",

    -10201: "数据库查询错误",
    -10202: "存在多个相同的结果",
    -10203: "查询没有结果",
    -10204: "数据表中不存在此字段",
    -10205: "数据库插入失败",

    -10301: "Redis服务查询失败",

    -10401: "拒绝相同内容重复请求",
    -10411: "APP未启用",
    -10412: "APP已停用",
    -10413: "APP未授权",
    -10420: "HTTP请求内容类型不正确，要求是JSON",
    -10421: "没有提供请求方法或者方法不正确",
    -10422: "此方法未授权，拒绝服务",
    -10423: "未授权的IP请求",
    -10424: "匹配请求IP出现错误",
    -10425: "未授权的域名请求",
    -10426: "匹配请求域名出现错误",
    -10427: "没有任何操作",

    -10501: "解密失败",
    -10502: "验证签名失败",
    -10503: "签名失败",
    -10504: "密钥长度错误，取值范围[1024, 2048, 4096]",
    -10505: "密钥序列化失败",

    -10601: "appid已经存在",
    
    # 钱包提醒 -11xxx
    -11101: "缺少密码字段",
    -11102: "缺少address字段",
    -11103: "密码错误",
    
    # 合约 -12xxx
    -12101: "合约交易回滚!",
    -12201: "该appid无主合约!",
    
    #
    -40000: "系统服务错误!",
}


def err_format(err_type_n=0, errno_n=0, addition=""):
    err_info = {
        # "code": "fail",                    # 错误码
        # "error": "",                       # 错误说明
        # "type": err_pro_type[err_type_n],  # 错误类型
        "status": errno_n,                   # 错误码NEW
        "msg": errno_mess[errno_n],          # 错误说明
        # "addition": addition               # 附加说明
    }
    return err_info



