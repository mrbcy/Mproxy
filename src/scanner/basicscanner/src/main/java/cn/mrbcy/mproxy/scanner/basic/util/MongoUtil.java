package cn.mrbcy.mproxy.scanner.basic.util;

import com.mongodb.MongoClient;
import com.mongodb.client.MongoDatabase;

/**
 * Created by Yang on 2017/8/17.
 */
public class MongoUtil {
    private static MongoClient mongoClient = new MongoClient("localhost", 27017);
    public static synchronized MongoDatabase getMongoDatabase(){
        if(mongoClient == null){
            throw new RuntimeException("MongoClient has been disposed.");
        }
        return mongoClient.getDatabase("mproxy");
    }

    public static synchronized void dispose(){
        mongoClient.close();
    }
}
