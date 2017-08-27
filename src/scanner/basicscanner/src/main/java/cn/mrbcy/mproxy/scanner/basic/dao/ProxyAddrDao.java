package cn.mrbcy.mproxy.scanner.basic.dao;

import cn.mrbcy.mproxy.scanner.basic.bean.ProxyAddr;

/**
 * Created by Yang on 2017/8/27.
 */
public interface ProxyAddrDao {
    /**
     * 更新代理服务器信息，如果不存在则插入，否则更新
     * @param proxyAddr
     */
    void updateProxy(ProxyAddr proxyAddr);

    /**
     * 查找代理服务器
     * @param ip IP地址
     * @param port 端口号
     * @return 代理服务器信息，不存在返回null
     */
    ProxyAddr findProxy(String ip, int port);

}
