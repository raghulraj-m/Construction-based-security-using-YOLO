**Flask YOLO Object Detection for Construction Site Security**
This Flask-based web application utilizes the YOLO (You Only Look Once) object detection model, integrated with OpenCV and Ultralytics, to provide real-time construction site security monitoring. The application captures video frames from the default webcam, processes them through the YOLO model, and identifies various objects within the construction site environment.

**Key Features**
Real-time Object Detection: The YOLO model identifies and classifies objects in the construction site video stream, including personnel, equipment, safety gear, and potential hazards.

**Dynamic Web Interface:** Flask serves a dynamic web interface where users can visualize the real-time video stream with annotated object detection results.

**Classified Objects:** Detected objects are classified into categories such as 'Excavator,' 'Gloves,' 'Hardhat,' 'Ladder,' 'Mask,' and more, enhancing the system's utility for construction site security.

**Setup Instructions**
Clone the Repository:

**bash**
**Copy code**
git clone https://github.com/yourusername/your-repository.git
cd your-repository
Install Dependencies:

**bash**
**Copy code**
pip install -r requirements.txt
Download YOLO Weights:
Obtain the YOLO pre-trained weights file (e.g., best.pt) and place it in the project directory.

**Run the Application:**

**bash**
**Copy code**
python app.py
**Usage**
Access the application through a web browser by navigating to http://127.0.0.1:5000/.

The main page displays the real-time video stream from the webcam, annotated with bounding boxes around detected objects.

Customize the classNames list in app.py based on your specific construction site objects.

**Project Structure**
app.py: The main Flask application file containing the web server and YOLO object detection logic.

templates/index.html: HTML template for rendering the web interface.

**Contributions**
Contributions to the project are welcome! Feel free to open issues, provide feedback, or submit pull requests to enhance the functionality and usability of the application.
