package cn.mrbcy.mproxy.dao.impl;

import cn.mrbcy.mproxy.scanner.basic.bean.IPSegment;
import cn.mrbcy.mproxy.scanner.basic.dao.IPSegmentDao;
import cn.mrbcy.mproxy.scanner.basic.dao.impl.IPSegmentDaoMongoImpl;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

import java.util.List;

/**
 * Created by Yang on 2017/8/27.
 */
public class IPSegmentDaoMongoImplTest {
    IPSegmentDao dao;

    @Before
    public void init(){
        dao = new IPSegmentDaoMongoImpl();
    }
    @Test
    public void testGet(){
        List<IPSegment> segments = dao.getIpSegments(10);
        Assert.assertTrue(segments == null || (segments.size() > 0 && segments.size() <= 10));
    }

    @Test
    public void testUpdateLastModifyTime(){
        List<IPSegment> segments = dao.getIpSegments(10);
        if(segments == null){
            return;
        }
        String id = segments.get(segments.size() - 1).getId();
        dao.updateLastModifiedTime(id);
        segments = dao.getIpSegments(10);
        Assert.assertEquals(id, segments.get(0).getId());
    }
}
