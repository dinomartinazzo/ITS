```c#
#include <WiFi.h>

const char* ssid     = "FRITZ!Box 7530 NH";
const char* password = "3661461500";

// Set your Static IP address
IPAddress local_IP(10, 0, 0, 184);
IPAddress gateway(10, 0, 0, 254);

IPAddress subnet(255, 255, 0, 0);
IPAddress primaryDNS(8, 8, 8, 8);    
IPAddress secondaryDNS(8, 8, 4, 4);  


const char* myssid     = "Walker";
const char* mypassword = "123456789";


void setup() 
{
  while (!Serial);
  delay(1000);
  Serial.begin(115200);

  WiFi.mode(WIFI_AP_STA);   
  
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
 
}

```



```c#
#include <WiFi.h>
#include <WiFiAP.h>

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

  Serial.println("Configuring access point...");

  WiFi.mode(WIFI_AP_STA);
  WiFi.disconnect();
  if (!WiFi.config(local_IP, gateway, subnet, primaryDNS, secondaryDNS))
  {
    Serial.println("\nSTA Failed to configure");
  }
  
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
  WiFi.softAP(myssid, mypassword);
  Serial.println("Wait for AP_START...");
  delay(100);

  Serial.println("Set softAPConfig");
  IPAddress Ip(192, 168, 1, 1);
  IPAddress NMask(255, 255, 255, 0);
  WiFi.softAPConfig(Ip, Ip, NMask);

  IPAddress myIP = WiFi.softAPIP();
  Serial.print("AP IP address: ");
  Serial.println(myIP);
 

  //Connect to UDP Port.
  udp.connect(IPAddress(192, 168, 1, 255), 1234);
  if (udp.listen(1234)) {
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

}


void loop()
{
  sensorValue0 = analogRead(36);
  sensorValue3 = analogRead(39);
  sensorValue6 = analogRead(34);
  sensorValue7 = analogRead(35);
  sensorValue4 = analogRead(32);
  sensorValue5 = analogRead(33);

  String message_send = String(micros())  + "," + String(micros() / 1000000)  + "," + String(sensorValue0) + "," +  String(sensorValue3) + "," +  String(sensorValue6) + "," +  String(sensorValue7) + "," +  String(sensorValue4) + "," +  String(sensorValue5)  ;
  //udp.broadcastTo(message_send.c_str(), 1234);
  udp.writeTo((const uint8_t *)message_send.c_str(), message_send.length(), IPAddress(192, 168, 1, 2), 1234);
}
```