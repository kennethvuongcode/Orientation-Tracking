**Orientation Tracking and Panorama Generation Through IMU Data**

In this project I implement orientation tracking of a rotating body through raw IMU data then use the data to generate a panorama. I first preprocess the IMU data. I then extract the calibrated linear acceleration and angular velocity data to generate a quaternion kinematics motion model, describing the motion of the rotating body across time. I also implement an observation model that describes the linear acceleration across time. I combine the motion model and observation model to create a cost function that I then use to optimize the estimated quaternion trajectory. The optimization is done through projected gradient descent using the _jax_ library.

From the generated trajectory I then map camera images to a panorama. This is done by projecting a 2D image to a sphere then applying a rotation corresponding to the quaternion trajectory at a specific time.

Core concepts utilized in this project are:
- Quaternion Operations
- Quaternion Kinematics Motion and Observation Model
- Projected Gradient Descent using the _jax_ library
- Coordinate transform and spherical image mapping

A paper detailing the equipment, my process, and results can be found at the "Orientation Tracking and Panorama Generation" pdf. Check it out!
