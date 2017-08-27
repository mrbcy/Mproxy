package cn.mrbcy.mproxy.scanner.basic.dao.impl;

import cn.mrbcy.mproxy.scanner.basic.bean.IPSegment;
import cn.mrbcy.mproxy.scanner.basic.dao.IPSegmentDao;
import cn.mrbcy.mproxy.scanner.basic.util.DocumentConverter;
import cn.mrbcy.mproxy.scanner.basic.util.MongoUtil;
import com.mongodb.MongoClient;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoCursor;
import com.mongodb.client.MongoDatabase;
import com.mongodb.client.model.Sorts;
import org.bson.Document;
import org.bson.types.ObjectId;

import java.util.ArrayList;
import java.util.List;

import static com.mongodb.client.model.Filters.eq;
import static com.mongodb.client.model.Updates.currentDate;

/**
 * Created by Yang on 2017/8/17.
 */
public class IPSegmentDaoMongoImpl implements IPSegmentDao {
    private MongoDatabase mongoDatabase = MongoUtil.getMongoDatabase();
    private MongoCollection<Document> collection = mongoDatabase.getCollection("proxy_segment");
    public List<IPSegment> getIpSegments() {
        return getIpSegments(100);
    }

    public List<IPSegment> getIpSegments(int count) {
        MongoCursor<Document> cursor = collection.find().sort(Sorts.descending("lastModifiedTime")).limit(count).iterator();
        try {
            List<IPSegment> ipSegments = new ArrayList<IPSegment>();
            while (cursor.hasNext()) {
                Document segDoc = cursor.next();
                IPSegment ipSegment = DocumentConverter.docToIpSegment(segDoc);
                ipSegments.add(ipSegment);
            }
            return ipSegments.size() == 0 ? null : ipSegments;
        } finally {
            cursor.close();
        }
    }

    public void updateLastModifiedTime(String id) {
        if(id == null || id.trim().length() == 0){
            throw new RuntimeException("ipSegment id can't be null");
        }
        collection.updateOne(eq("_id", new ObjectId(id)),currentDate("lastModifiedTime"));
    }
}
