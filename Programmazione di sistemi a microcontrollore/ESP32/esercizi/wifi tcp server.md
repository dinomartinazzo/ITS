#include <WiFi.h>
#include "esp_wifi.h"
 

const char *myssid = "Walker";
const char *mypassword = "12345678";

const char *ssid     = "FRITZ!Box 7530 NH";
const char *password = "3661461500";

// Set your Static IP address
IPAddress local_IP(10, 0, 0, 184);
IPAddress gateway(10, 0, 0, 254);

IPAddress subnet(255, 255, 0, 0);
IPAddress primaryDNS(8, 8, 8, 8);
IPAddress secondaryDNS(8, 8, 4, 4);


int sensorValue0 = 0;
int sensorValue3 = 0;
int sensorValue6 = 0;
int sensorValue7 = 0;
int sensorValue4 = 0;
int sensorValue5 = 0;

#include "AsyncUDP.h"
AsyncUDP udp;

WiFiServer server(1234);

void PrintStations()
{

  wifi_sta_list_t wifi_sta_list;
  tcpip_adapter_sta_list_t adapter_sta_list;

  memset(&wifi_sta_list, 0, sizeof(wifi_sta_list));
  memset(&adapter_sta_list, 0, sizeof(adapter_sta_list));

  esp_wifi_ap_get_sta_list(&wifi_sta_list);
  tcpip_adapter_get_sta_list(&wifi_sta_list, &adapter_sta_list);

  for (int i = 0; i < adapter_sta_list.num; i++) {

    tcpip_adapter_sta_info_t station = adapter_sta_list.sta[i];

    Serial.print("station nr ");
    Serial.println(i);

    Serial.print("MAC: ");

    for (int i = 0; i < 6; i++) {

      Serial.printf("%02X", station.mac[i]);
      if (i < 5)Serial.print(":");
    }

    //    Serial.print("\nIP: ");
    //    Serial.println(ip4addr_ntoa(&(station.ip)));
  }

  Serial.println("-----------------\r\n");
}

void WiFiStationConnected(WiFiEvent_t event, WiFiEventInfo_t info) {
  Serial.println("Station connected");
  PrintStations();
}

void setup()
{


  // Set all slider pins to INPUT
  pinMode(36, INPUT);
  pinMode(39, INPUT);
  pinMode(34, INPUT);
  pinMode(35, INPUT);
  pinMode(32, INPUT);
  pinMode(33, INPUT);


  while (!Serial);
  delay(1000);
  Serial.begin(115200);

  uint32_t Freq = 0;
  setCpuFrequencyMhz(80);
  Freq = getCpuFrequencyMhz();
  Serial.print("CPU Freq = ");
  Serial.print(Freq);
  Serial.println(" MHz");
  Freq = getXtalFrequencyMhz();
  Serial.print("XTAL Freq = ");
  Serial.print(Freq);
  Serial.println(" MHz");
  Freq = getApbFrequency();
  Serial.print("APB Freq = ");
  Serial.print(Freq);
  Serial.println(" Hz");

  Serial.println("Configuring access point...");
  WiFi.mode(WIFI_AP_STA);
  //  WiFi.disconnect();
  //  if (!WiFi.config(local_IP, gateway, subnet, primaryDNS, secondaryDNS))
  //  {
  //    Serial.println("\nSTA Failed to configure");
  //  }
  //
  //  Serial.print("\nConnecting to Wi-Fi network with SSID and password\n");
  //  Serial.println(ssid);
  //  WiFi.begin(ssid, password);
  //  while (WiFi.status() != WL_CONNECTED)
  //  {
  //    delay(500);
  //    Serial.print(".");
  //  }
  //  Serial.println("\n");
  //  Serial.println("WiFi connected.");
  //  Serial.println("IP address: ");
  //  Serial.println(WiFi.localIP());


  //WiFi.mode(WIFI_AP);
  WiFi.softAP(myssid);
  Serial.println("Wait for AP_START...");
  delay(100);

  //  Serial.println("Set softAPConfig");
  //  IPAddress Ip(192, 168, 1, 1);
  //  IPAddress NMask(255, 255, 255, 0);
  //  WiFi.softAPConfig(Ip, Ip, NMask);

  IPAddress myIP = WiFi.softAPIP();
  Serial.print("AP IP address: ");
  Serial.println(myIP);


  //  //Connect to UDP Port.
  //  udp.connect(IPAddress(192, 168, 4, 255), 1234);
  //  if (udp.listen(1234)) {
  //    udp.onPacket([](AsyncUDPPacket packet) {
  //      Serial.print("UDP Packet Type: ");
  //      Serial.print(packet.isBroadcast() ? "Broadcast" : packet.isMulticast() ? "Multicast" : "Unicast");
  //      Serial.print(", From: ");
  //      Serial.print(packet.remoteIP());
  //      Serial.print(":");
  //      Serial.print(packet.remotePort());
  //      Serial.print(", To: ");
  //      Serial.print(packet.localIP());
  //      Serial.print(":");
  //      Serial.print(packet.localPort());
  //      Serial.print(", Length: ");
  //      Serial.print(packet.length());
  //      Serial.print(", Data: ");
  //      Serial.write(packet.data(), packet.length());
  //      Serial.println();
  //      //reply to the client
  //      packet.printf("Got %u bytes of data", packet.length());
  //    });
  //  }

  WiFi.onEvent(WiFiStationConnected, SYSTEM_EVENT_AP_STACONNECTED);

  server.begin();
}



void loop()
{
  if (WiFiClient  client = server.available()) {
    String message_send = String(micros())  + "," + String(micros() / 1000000)  + "," + String(sensorValue0) + "," +  String(sensorValue3) + "," +  String(sensorValue6) + "," +  String(sensorValue7) + "," +  String(sensorValue4) + "," +  String(sensorValue5)  ;
    //client.println(message_send);
    client.write((const uint8_t *)message_send.c_str(), message_send.length());
    //client.stop();
  }

  sensorValue0 = analogRead(36);
  sensorValue3 = analogRead(39);
  sensorValue6 = analogRead(34);
  sensorValue7 = analogRead(35);
  sensorValue4 = analogRead(32);
  sensorValue5 = analogRead(33);
  String message_send = String(micros())  + "," + String(micros() / 1000000)  + "," + String(sensorValue0) + "," +  String(sensorValue3) + "," +  String(sensorValue6) + "," +  String(sensorValue7) + "," +  String(sensorValue4) + "," +  String(sensorValue5)  ;

  //udp.broadcastTo(message_send.c_str(), 1234);
  //udp.writeTo((const uint8_t *)message_send.c_str(), message_send.length(), IPAddress(192, 168, 4, 2), 1234);

 
}



-------------------

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.Linq;
using System.Net;
using System.Net.Sockets;

using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace UDP_Broadcast_Receiver
{
    public partial class Form1 : Form
    {



        public Form1()
        {
            InitializeComponent();
        }




        private void button1_Click(object sender, EventArgs e)
        {
            UdpClient UDPClient = new UdpClient();
            int localPort = 1234;
            int remotePort = 1234;
            IPEndPoint localEP = new IPEndPoint(IPAddress.Any, localPort);
            IPEndPoint remoteEP = new IPEndPoint(IPAddress.Parse("192.168.4.255"), remotePort);

            UDPClient.ExclusiveAddressUse = false;
            UDPClient.Client.SetSocketOption(SocketOptionLevel.Socket, SocketOptionName.ReuseAddress, true);
            UDPClient.Client.Bind(localEP);

            byte[] emptyByte = { };
            UDPClient.Send(emptyByte, emptyByte.Length, remoteEP);

            try
            {
                while (true)
                {

                    Byte[] receivedBytes = UDPClient.Receive(ref localEP);
                    string s = Encoding.ASCII.GetString(receivedBytes);

                    Debug.WriteLine(DateTime.Now.ToString("HH:mm:ss.ffff ") + "  " + s);

                }
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.ToString());
            }


        }



        private void button2_Click(object sender, EventArgs e)
        {
            UdpClient udpClient = new UdpClient();
            Byte[] sendBytes = Encoding.ASCII.GetBytes("Is anybody there");
            try
            {
                udpClient.Send(sendBytes, sendBytes.Length, "192.168.4.255", 1234);
            }
            catch (Exception ext)
            {
                Console.WriteLine(ext.ToString());
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Thread thdUDPServer = new Thread(new ThreadStart(serverThread));
            thdUDPServer.Start();
        }

        public void serverThread()
        {
            UdpClient udpClient = new UdpClient();
            int localPort = 1234;

            udpClient.Client.Bind(new IPEndPoint(IPAddress.Parse("192.168.4.2"), localPort));
            udpClient.Client.SetSocketOption(SocketOptionLevel.Socket, SocketOptionName.ReceiveTimeout, 500);


            byte[] emptyByte = { };
            int remotePort = 1234;
            IPEndPoint remoteEP = new IPEndPoint(IPAddress.Parse("192.168.4.255"), remotePort);
            udpClient.Send(emptyByte, emptyByte.Length, remoteEP);




            while (true)
            {



                IPEndPoint RemoteIpEndPoint = new IPEndPoint(IPAddress.Parse("192.168.4.2"), localPort);
                Byte[] receiveBytes = udpClient.Receive(ref RemoteIpEndPoint);
                string returnData = Encoding.ASCII.GetString(receiveBytes);
                Debug.WriteLine(DateTime.Now.ToString("HH:mm:ss.ffff ") + "  " + returnData);





            }


        }



        private void button4_Click(object sender, EventArgs e)
        {
            var t = new Thread(ReceiveData);
            t.Name = "ReceiveData";
            t.Priority = ThreadPriority.AboveNormal;
            t.Start();


        }

        void ReceiveData()
        {

            while (true)
            {
                Byte[] dataReceive = new Byte[256];
                var client = new TcpClient("192.168.4.1", 1234);
                NetworkStream stream = client.GetStream();
                String responseData = String.Empty;
                Int32 bytes = stream.Read(dataReceive, 0, dataReceive.Length);
                responseData = System.Text.Encoding.ASCII.GetString(dataReceive, 0, bytes);
                Debug.WriteLine(responseData);
                stream.Close();
                client.Close();
            }



        }


    }
}
