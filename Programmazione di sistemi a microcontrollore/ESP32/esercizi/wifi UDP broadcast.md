```c#
#include "WiFi.h"
#include "AsyncUDP.h"
AsyncUDP udp;

const char* ssid     = "FRITZ!Box 7530 NH";
const char* password = "3661461500";

// Set your Static IP address
IPAddress local_IP(10, 0, 0, 184);
IPAddress gateway(10, 0, 0, 254);

IPAddress subnet(255, 255, 0, 0);
IPAddress primaryDNS(8, 8, 8, 8);
IPAddress secondaryDNS(8, 8, 4, 4);

IPAddress broadcastIp(10, 0, 0, 255);
unsigned int localUdpPort = 1234;

const char* myssid     = "Walker";
const char* mypassword = "123456789";


void setup()
{
  while (!Serial);
  delay(1000);
  Serial.begin(115200);

  WiFi.mode(WIFI_AP_STA);
  //WiFi.mode(WIFI_STA);

  WiFi.disconnect();
  if (!WiFi.config(local_IP, gateway, subnet, primaryDNS, secondaryDNS))
  {
    Serial.println("\nSTA Failed to configure");
  }
  Serial.print("\nConnecting to Wi-Fi network with SSID and password\n");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\n");
  Serial.println("WiFi connected.");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());


  if (udp.listen(1234)) {
    Serial.println("UDP Listening on IP: ");
    Serial.println(WiFi.localIP());
    udp.onPacket([](AsyncUDPPacket packet) {
      Serial.print("UDP Packet Type: ");
      Serial.print(packet.isBroadcast() ? "Broadcast" : packet.isMulticast() ? "Multicast" : "Unicast");
      Serial.print(", From: ");
      Serial.print(packet.remoteIP());
      Serial.print(":");
      Serial.print(packet.remotePort());
      Serial.print(", To: ");
      Serial.print(packet.localIP());
      Serial.print(":");
      Serial.print(packet.localPort());
      Serial.print(", Length: ");
      Serial.print(packet.length());
      Serial.print(", Data: ");
      Serial.write(packet.data(), packet.length());
      Serial.println();
      //reply to the client
      packet.printf("Got %u bytes of data", packet.length());
    });
  }


  Serial.print("\nSetting AP (Access Point)…");
  //WiFi.softAP(ssid, password);
  WiFi.softAP(myssid);
  Serial.println("\nWait for AP_START...");
  delay(200);
  IPAddress Ip(10, 0, 0, 185);
  IPAddress NMask(255, 255, 255, 0);
  WiFi.softAPConfig(Ip, Ip, NMask);
  IPAddress myIP = WiFi.softAPIP();
  Serial.print("\nAP IP address: ");
  Serial.println(myIP);

}

void loop()
{
  //delay(1000);
  String builtString = String("Ciao! ") + String(micros()/1000000);
  
  udp.broadcast(builtString.c_str());

}
```



```c#
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.Linq;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace UDP_Broadcast_Receiver
{
    public partial class Form1 : Form
    {
        private static void UDPListener()
        {
            Task.Run(async () =>
            {
                using (var udpClient = new UdpClient(1234))
                {
                    //string loggingEvent = "";
                    while (true)
                    {
                        //IPEndPoint object will allow us to read datagrams sent from any source.
                        var receivedResults = await udpClient.ReceiveAsync();
                        //loggingEvent += Encoding.ASCII.GetString(receivedResults.Buffer);
                        Debug.Print(Encoding.ASCII.GetString(receivedResults.Buffer));
                    }
                }
            });
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            UDPListener();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            UdpClient udpClient = new UdpClient();
            Byte[] sendBytes = Encoding.ASCII.GetBytes("Is anybody there");
            try
            {
                udpClient.Send(sendBytes, sendBytes.Length, "10.0.0.184", 1234);
            }
            catch (Exception ext)
            {
                Console.WriteLine(ext.ToString());
            }
        }
    }
}
```