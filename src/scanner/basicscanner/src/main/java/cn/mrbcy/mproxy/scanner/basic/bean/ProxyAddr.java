package cn.mrbcy.mproxy.scanner.basic.bean;

/**
 * Created by Yang on 2017/8/27.
 */
public class ProxyAddr {
    private String IP;
    private int port;
    private boolean available;

    public ProxyAddr(){

    }

    public ProxyAddr(String IP, int port) {
        this.IP = IP;
        this.port = port;
    }

    public ProxyAddr(String IP, int port, boolean available) {
        this.IP = IP;
        this.port = port;
        this.available = available;
    }

    public String getIP() {
        return IP;
    }

    public void setIP(String IP) {
        this.IP = IP;
    }

    public int getPort() {
        return port;
    }

    public void setPort(int port) {
        this.port = port;
    }

    public boolean isAvailable() {
        return available;
    }

    public void setAvailable(boolean available) {
        this.available = available;
    }

    @Override
    public String toString() {
        return "ProxyAddr{" +
                "IP='" + IP + '\'' +
                ", port=" + port +
                ", available=" + available +
                '}';
    }
}
