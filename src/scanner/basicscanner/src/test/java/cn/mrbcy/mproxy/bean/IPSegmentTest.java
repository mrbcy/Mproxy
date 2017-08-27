package cn.mrbcy.mproxy.bean;

import cn.mrbcy.mproxy.scanner.basic.bean.IPSegment;
import org.junit.Assert;
import org.junit.Test;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by Yang on 2017/8/17.
 */
public class IPSegmentTest {

    @Test
    public void testConstructor(){
        IPSegment ip = new IPSegment("192.168.5.5");
        Assert.assertEquals("192.168.5.1",ip.getStartIP());
        Assert.assertEquals("192.168.5.255",ip.getEndIP());
    }

    @Test(expected = IllegalArgumentException.class)
    public void testInvalidIP(){
        IPSegment ip = new IPSegment("192.168.5.a");
    }


}
