package cn.mrbcy.mproxy.scanner.basic.bean;

import java.util.Date;
import java.util.regex.Pattern;

/**
 * Created by Yang on 2017/8/16.
 */
public class IPSegment {
    private static String IPADDRESS_PATTERN =
            "(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)";
    private static Pattern pattern = Pattern.compile(IPADDRESS_PATTERN);

    private String startIP;
    private String endIP;
    private String id;
    private int port;
    private String safety;
    private String type;
    private String location;
    private Date lastModifiedTime;



    public IPSegment(String ip){
        if(!ip.matches(IPADDRESS_PATTERN)){
            throw new IllegalArgumentException("Param ip must be a valid ip address");
        }
        startIP = ip.substring(0, ip.lastIndexOf(".")) + ".1";
        endIP = ip.substring(0, ip.lastIndexOf(".")) + ".255";
    }


    public String getStartIP() {
        return startIP;
    }

    public void setStartIP(String startIP) {
        this.startIP = startIP;
    }

    public String getEndIP() {
        return endIP;
    }

    public void setEndIP(String endIP) {
        this.endIP = endIP;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public int getPort() {
        return port;
    }

    public void setPort(int port) {
        this.port = port;
    }

    public String getSafety() {
        return safety;
    }

    public void setSafety(String safety) {
        this.safety = safety;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public Date getLastModifiedTime() {
        return lastModifiedTime;
    }

    public void setLastModifiedTime(Date lastModifiedTime) {
        this.lastModifiedTime = lastModifiedTime;
    }

    @Override
    public String toString() {
        return "IPSegment{" +
                "startIP='" + startIP + '\'' +
                ", endIP='" + endIP + '\'' +
                ", id='" + id + '\'' +
                ", port=" + port +
                ", safety='" + safety + '\'' +
                ", type='" + type + '\'' +
                ", location='" + location + '\'' +
                ", lastModifiedTime=" + lastModifiedTime +
                '}';
    }
}
