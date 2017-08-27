package cn.mrbcy.mproxy.scanner.basic;


import cn.mrbcy.PortScanner.PortScanner;
import cn.mrbcy.PortScanner.listener.ScanProgressListener;
import cn.mrbcy.mproxy.scanner.basic.bean.IPSegment;
import cn.mrbcy.mproxy.scanner.basic.bean.ProxyAddr;
import cn.mrbcy.mproxy.scanner.basic.dao.IPSegmentDao;
import cn.mrbcy.mproxy.scanner.basic.dao.impl.IPSegmentDaoMongoImpl;
import cn.mrbcy.mproxy.scanner.basic.validator.BasicValidator;

import java.util.Iterator;
import java.util.List;
import java.util.Set;

/**
 * Created by Yang on 2017/8/14.
 */
public class Main {

    public static void main(String[] args) {
        final IPSegmentDao ipSegmentDao = new IPSegmentDaoMongoImpl();
        final List<IPSegment> ipSegments = ipSegmentDao.getIpSegments(1);
        final PortScanner scanner = new PortScanner();


        scanner.startScan(new ScanProgressListener() {
            public void onScanProgress(Set<String> openRecords, Set<String> closeRecords, long restNum) {
                System.out.println(String.format("扫描到端口开启的主机 %d 个，端口关闭的主机 %d 个，待扫描主机 %d 个",
                        openRecords.size(), closeRecords.size(), restNum));
                Iterator<String> iterator = openRecords.iterator();
                while(iterator.hasNext()){
                    String addr = iterator.next();
                    System.out.println(addr + " 开启");
                    BasicValidator.submit(new ProxyAddr(addr.split(":")[0],Integer.parseInt(addr.split(":")[1])));
                }
            }

            public void onScanComplete(Set<String> allOpenRecords) {
                BasicValidator.stop();
//                scanner.stopScan();
            }

            public boolean onTaskQueueEmpty(PortScanner portScanner) {
                if(ipSegments.size() > 0){
                    for(IPSegment segment : ipSegments){
                        portScanner.addTaskBatch(segment.getStartIP(), segment.getEndIP(), segment.getPort());
                        ipSegmentDao.updateLastModifiedTime(segment.getId());
                        System.out.println("添加任务项：" + segment);
                    }
                    ipSegments.clear();
                    return true;
                }else{
                    List<IPSegment> s = ipSegmentDao.getIpSegments(200);
                    ipSegments.addAll(s);
                    return true;
                }
            }
        }, 200, 1200);
    }
}
