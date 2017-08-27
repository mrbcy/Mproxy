package cn.mrbcy.mproxy.scanner.basic.util;

import cn.mrbcy.mproxy.scanner.basic.bean.IPSegment;
import cn.mrbcy.mproxy.scanner.basic.bean.ProxyAddr;
import com.sun.corba.se.impl.ior.OldJIDLObjectKeyTemplate;
import org.bson.Document;

import java.lang.reflect.Field;

/**
 * Created by Yang on 2017/8/27.
 */
public class DocumentConverter {
    public static Object docToObject(Document doc, Class clazz){
        try{
            Object obj = clazz.newInstance();
            Field[] fields = clazz.getFields();
            for(Field field : fields){
                try {
                    field.set(obj,doc.get(field.getName()));
                }catch (Exception ex){}
            }
            return obj;
        }catch(Exception e){
            e.printStackTrace();
        }


        return null;
    }

    public static IPSegment docToIpSegment(Document doc){
        IPSegment segment = new IPSegment(doc.getString("ip"));
        segment.setId(doc.getObjectId("_id").toString());
        segment.setLastModifiedTime(doc.getDate("lastModifiedTime"));
        segment.setLocation(doc.getString("location"));
        segment.setPort(doc.getInteger("port"));
        segment.setSafety(doc.getString("safety"));
        segment.setType(doc.getString("type"));
        return segment;
    }

    public static ProxyAddr docToProxyAddr(Document doc){
        ProxyAddr proxyAddr = new ProxyAddr();
        proxyAddr.setIP(doc.getString("ip"));
        proxyAddr.setPort(doc.getInteger("port"));
        proxyAddr.setAvailable(doc.getBoolean("available"));
        return proxyAddr;
    }
}
