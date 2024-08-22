import java.net.*;

class InterTest {
    public static void main(String[] args) {
        try {
            InetAddress i = InetAddress.getLocalHost();
            System.out.println("LocalHost=" + i);
            System.out.println("LocalHost=" + i.getHostName());

            i = InetAddress.getByName("157.240.13.35"); // Use a valid IP address, not "157.240,13.35"
            System.out.println("Address name=" + i.getHostName());

            i = InetAddress.getByName("google.co.in");
            System.out.println(i.getHostAddress());
            System.out.println(i.isMulticastAddress() ? "Yes" : "No");
            System.out.println(i.isLoopbackAddress() ? "Yes Loopback" : "No");

            InetAddress iArr[] = InetAddress.getAllByName("facebook.com"); // Corrected the domain name
            for (int j = 0; j < iArr.length; j++) {
                System.out.println(iArr[j]);
            }
        } catch (UnknownHostException e) {
            e.printStackTrace();
        }
    }
}
