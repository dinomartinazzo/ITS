# Compensate the accelerometer readings from gravity. 

```js
# Compensate the accelerometer readings from gravity. 
# @param q the quaternion representing the orientation of a 9DOM MARG sensor array
# @param acc the readings coming from an accelerometer expressed in g
#
# @return a 3d vector representing dinamic acceleration expressed in g
def gravity_compensate(q, acc):
  g = [0.0, 0.0, 0.0]
  
  # get expected direction of gravity
  g[0] = 2 * (q[1] * q[3] - q[0] * q[2])
  g[1] = 2 * (q[0] * q[1] + q[2] * q[3])
  g[2] = q[0] * q[0] - q[1] * q[1] - q[2] * q[2] + q[3] * q[3]
  
  # compensate accelerometer readings with the expected direction of gravity
  return [acc[0] - g[0], acc[1] - g[1], acc[2] - g[2]]


      // Define output variables from updated quaternion---these are Tait-Bryan
      // angles, commonly used in aircraft orientation. In this coordinate system,
      // the positive z-axis is down toward Earth. Yaw is the angle between Sensor
      // x-axis and Earth magnetic North (or true North if corrected for local
      // declination, looking down on the sensor positive yaw is counterclockwise.
      // Pitch is angle between sensor x-axis and Earth ground plane, toward the
      // Earth is positive, up toward the sky is negative. Roll is angle between
      // sensor y-axis and Earth ground plane, y-axis up is positive roll. These
      // arise from the definition of the homogeneous rotation matrix constructed
      // from quaternions. Tait-Bryan angles as well as Euler angles are
      // non-commutative; that is, the get the correct orientation the rotations
      // must be applied in the correct order which for this configuration is yaw,
      // pitch, and then roll.
      // For more see
      // http://en.wikipedia.org/wiki/Conversion_between_quaternions_and_Euler_angles
      // which has additional links.

      myIMU.yaw   = atan2(2.0f * (*(getQ() + 1) * *(getQ() + 2) + *getQ() *
                                  *(getQ() + 3)), *getQ() * *getQ() + * (getQ() + 1) * *(getQ() + 1)
                          - * (getQ() + 2) * *(getQ() + 2) - * (getQ() + 3) * *(getQ() + 3));
      myIMU.pitch = -asin(2.0f * (*(getQ() + 1) * *(getQ() + 3) - *getQ() *
                                  *(getQ() + 2)));
      myIMU.roll  = atan2(2.0f * (*getQ() * *(getQ() + 1) + * (getQ() + 2) *
                                  *(getQ() + 3)), *getQ() * *getQ() - * (getQ() + 1) * *(getQ() + 1)
                          - * (getQ() + 2) * *(getQ() + 2) + * (getQ() + 3) * *(getQ() + 3));
      myIMU.pitch *= RAD_TO_DEG;
      myIMU.yaw   *= RAD_TO_DEG;
      // Declination of SparkFun Electronics (40°05'26.6"N 105°11'05.9"W) is
      // 	8° 30' E  ± 0° 21' (or 8.5°) on 2016-07-19
      // - http://www.ngdc.noaa.gov/geomag-web/#declination
      myIMU.yaw   -= 8.5;
      myIMU.roll  *= RAD_TO_DEG;





a12 =   2.0f * (q[1] * q[2] + q[0] * q[3]);
a22 =   q[0] * q[0] + q[1] * q[1] - q[2] * q[2] - q[3] * q[3];
a31 =   2.0f * (q[0] * q[1] + q[2] * q[3]);
a32 =   2.0f * (q[1] * q[3] - q[0] * q[2]);
a33 =   q[0] * q[0] - q[1] * q[1] - q[2] * q[2] + q[3] * q[3];
pitch1 = -asinf(a32);
roll1  = atan2f(a31, a33);
yaw1   = atan2f(a12, a22);
pitch1 *= 180.0f / pi;
yaw1   *= 180.0f / pi; 
yaw1   += 13.8f; // Declination at Danville, California is 13 degrees 48 minutes and 47 seconds on 2014-04-04
if(yaw1 < 0) yaw1   += 360.0f; // Ensure yaw stays between 0 and 360
roll1  *= 180.0f / pi;
//lin_ax1 = ax1 + a31;
//lin_ay1 = ay1 + a32;
lin_az1 = az1 - a33;


lin_ax = ax + a32;
lin_ay = ay - a31;

for the x axis (perpendicular to Yaw=0):
float x = lin_ax * cos(pitch) * cos(roll) * sin(yaw) 
        + lin_ax * cos(pitch) * sin(roll) * sin(yaw)
        + lin_ay * cos(pitch) * cos(roll) * cos(yaw)
        + lin_ay * sin(pitch) * cos(roll) * cos(yaw)
        + lin_az * cos(pitch) * sin(roll) * cos(yaw)
        + lin_az * sin(pitch) * cos(roll) * sin(yaw);


        private const double damping = 0.05;
        private double vspeed;
        private const double vspeedDamping = 0.95;

   		double deltaTime = timer.ElapsedMilliseconds*0.001;
                timer.Restart();

                double newHeel = -90 + 180.0*(e.WiimoteState.AccelState.RawValues.X - 94)/(143 - 94);
                double newTrim = -90 + 180.0*(e.WiimoteState.AccelState.RawValues.Y - 94)/(143 - 94);
                Heel = Heel + (newHeel - Heel)*damping;
                Trim = Trim + (newTrim - Trim)*damping;

                double verticalAcceleration = 100.0*(e.WiimoteState.AccelState.RawValues.Z - 143);
                vspeed += verticalAcceleration*deltaTime;
                vspeed *= vspeedDamping;
                Heave = (Heave + vspeed*deltaTime)*0.95;

```





