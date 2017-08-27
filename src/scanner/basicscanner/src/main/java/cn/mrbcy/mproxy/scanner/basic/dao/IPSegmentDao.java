package cn.mrbcy.mproxy.scanner.basic.dao;

import cn.mrbcy.mproxy.scanner.basic.bean.IPSegment;

import java.util.List;

/**
 * Created by Yang on 2017/8/17.
 */
public interface IPSegmentDao {
    /**
     * 获取待扫描的IP地址段，按照最后修改时间升序排列
     * @return 默认100条，如果没有返回空List
     */
    List<IPSegment> getIpSegments();

    /**
     * 获取指定条数的待扫描的IP地址段，按照最后修改时间升序排列
     * @return 如果没有返回空List
     */
    List<IPSegment> getIpSegments(int count);

    /**
     * 修改IP地址段的最后扫描时间
     * @param id
     */
    void updateLastModifiedTime(String id);
}
