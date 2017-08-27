package cn.mrbcy.mproxy.scanner.basic.validator;

import cn.mrbcy.mproxy.scanner.basic.bean.ProxyAddr;
import cn.mrbcy.mproxy.scanner.basic.dao.ProxyAddrDao;
import cn.mrbcy.mproxy.scanner.basic.dao.impl.ProxyAddrDaoMongoImpl;
import org.apache.commons.httpclient.HttpClient;
import org.apache.commons.httpclient.HttpMethod;
import org.apache.commons.httpclient.methods.GetMethod;


import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;


/**
 * Created by Yang on 2017/8/27.
 */
public class BasicValidator{
    private static ExecutorService executorService = Executors.newFixedThreadPool(10);
    private static ProxyAddrDao proxyAddrDao = new ProxyAddrDaoMongoImpl();
    private static final Object lockObj = new Object();

    public static void submit(ProxyAddr proxyAddr){
        System.out.println("提交代理服务器验证... " + proxyAddr);
        executorService.submit(new ValidatorTask(proxyAddr));
    }

    public static void stop(){
        executorService.shutdown();
        System.out.println("等待代理服务器验证完成...");
        try {
            executorService.awaitTermination(Integer.MAX_VALUE, TimeUnit.DAYS);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    private static class ValidatorTask implements Runnable{
        private ProxyAddr proxyAddr;
        public ValidatorTask(ProxyAddr proxyAddr){
            this.proxyAddr = proxyAddr;
        }
        public void run() {
            boolean valid = doValid(proxyAddr);
            if(valid){
                proxyAddr.setAvailable(true);
                System.out.println(proxyAddr + " 可用");
            }else {
                proxyAddr.setAvailable(false);
                System.out.println(proxyAddr + " 不可用");
            }
            synchronized (lockObj){
                proxyAddrDao.updateProxy(proxyAddr);
            }

        }
        private boolean doValid(ProxyAddr proxyAddr){
            try{
                String reqUrl = "http://t.sohu.com/";
                HttpClient httpClient = new HttpClient();
                httpClient.getHostConfiguration().setProxy(proxyAddr.getIP(), proxyAddr.getPort());

                // 连接超时时间（默认10秒 10000ms） 单位毫秒（ms）
                int connectionTimeout = 5000;
                // 读取数据超时时间（默认30秒 30000ms） 单位毫秒（ms）
                int soTimeout = 3000;
                httpClient.getHttpConnectionManager().getParams().setConnectionTimeout(connectionTimeout);
                httpClient.getHttpConnectionManager().getParams().setSoTimeout(soTimeout);

                HttpMethod method = new GetMethod(reqUrl);
                int statusCode = httpClient.executeMethod(method);
                return statusCode == 200;
            }catch (Exception e){
//                e.printStackTrace();
            }
            return false;

        }
    }


}
