from flask import Flask, render_template, request

app = Flask(__name__)
import subprocess
import datetime
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
class GpioMonitor(object):
     max_io_number = -1
     def __init__(self):
          if (GPIO.RPI_INFO['TYPE'] == 'Pi 3 Model B'):
               self.max_io_number = 28
          self.gpios_status={}
          for gpio in range(0,self.max_io_number):
               GPIO.setup(gpio, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
               self.gpios_status['GPIO'+str(gpio)]=GPIO.input(gpio)
               print('GPIO'+str(gpio)) 
               print(self.gpios_status['GPIO'+str(gpio)])
@app.route('/')
def index():
    info = GPIO.RPI_INFO
    return render_template('index.html',info=info)

@app.route('/board/', methods=['GET'])
def board():
    a = GpioMonitor()
    templateData = a.gpios_status
    return render_template('rpi3_pinout.html', **templateData)
   
if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')


          