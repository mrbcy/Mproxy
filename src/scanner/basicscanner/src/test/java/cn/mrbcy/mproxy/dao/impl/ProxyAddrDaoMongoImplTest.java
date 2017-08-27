package cn.mrbcy.mproxy.dao.impl;

import cn.mrbcy.mproxy.scanner.basic.bean.ProxyAddr;
import cn.mrbcy.mproxy.scanner.basic.dao.ProxyAddrDao;
import cn.mrbcy.mproxy.scanner.basic.dao.impl.ProxyAddrDaoMongoImpl;
import org.junit.Assert;
import org.junit.Test;

/**
 * Created by Yang on 2017/8/27.
 */
public class ProxyAddrDaoMongoImplTest {
    private ProxyAddrDao proxyAddrDao = new ProxyAddrDaoMongoImpl();

    @Test
    public void testFindProxyAddr(){
        ProxyAddr addr =  proxyAddrDao.findProxy("127.0.0.1", 8090);
        System.out.println(addr);
    }

    @Test
    public void testUpdate(){
        proxyAddrDao.updateProxy(new ProxyAddr("127.0.0.1", 808, true));
        ProxyAddr addr =  proxyAddrDao.findProxy("127.0.0.1", 808);
        Assert.assertTrue(addr != null);
        Assert.assertTrue(addr.isAvailable());

        proxyAddrDao.updateProxy(new ProxyAddr("127.0.0.1", 808, false));
        addr =  proxyAddrDao.findProxy("127.0.0.1", 808);
        Assert.assertTrue(addr != null);
        Assert.assertFalse(addr.isAvailable());
    }
}
