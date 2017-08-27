package cn.mrbcy.mproxy.scanner.basic.dao.impl;

import cn.mrbcy.mproxy.scanner.basic.bean.ProxyAddr;
import cn.mrbcy.mproxy.scanner.basic.dao.ProxyAddrDao;
import cn.mrbcy.mproxy.scanner.basic.util.DocumentConverter;
import cn.mrbcy.mproxy.scanner.basic.util.MongoUtil;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import org.bson.Document;
import org.bson.types.ObjectId;

import java.util.Date;

import static com.mongodb.client.model.Filters.eq;
import static com.mongodb.client.model.Updates.combine;
import static com.mongodb.client.model.Updates.currentDate;
import static com.mongodb.client.model.Updates.set;

/**
 * Created by Yang on 2017/8/27.
 */
public class ProxyAddrDaoMongoImpl implements ProxyAddrDao{
    private MongoDatabase mongoDatabase = MongoUtil.getMongoDatabase();
    private MongoCollection<Document> collection = mongoDatabase.getCollection("proxy");

    public void updateProxy(ProxyAddr proxyAddr) {
        if(proxyAddr == null || proxyAddr.getIP() == null || proxyAddr.getIP().trim().length() == 0){
            throw new RuntimeException("proxyAddr can't be null.");
        }
        if(findProxy(proxyAddr.getIP(), proxyAddr.getPort()) == null){
            // insert
            collection.insertOne(new Document("ip", proxyAddr.getIP())
                    .append("port",proxyAddr.getPort())
                    .append("available", proxyAddr.isAvailable())
                    .append("lastValidateTime", new Date()));
            return;
        }
        // update
        collection.updateOne(new Document("ip", proxyAddr.getIP()).append("port", proxyAddr.getPort()),
                combine(set("available", proxyAddr.isAvailable()),currentDate("lastValidateTime")));
    }

    public ProxyAddr findProxy(String ip, int port) {
        Document document = collection.find(new Document("ip", ip).append("port", port)).first();
        if(document != null){
            return DocumentConverter.docToProxyAddr(document);
        }
        return null;
    }
}
