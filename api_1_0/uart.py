import serial
import serial.tools.list_ports

class Uart():
    def __init__(self, port, baud):
        try:
            if port in self.get_com_list():
                self.uart = serial.Serial(port=port, baudrate=baud)
            else:
                raise Exception("uart port '{0}' not found".format(port))
        except serial.SerialException as err:
            raise Exception(err)

    def get_com_list(self):
        return [item.device for item in serial.tools.list_ports.comports()]

    def send(self, cmd):
        self.uart.write(cmd)

    def close(self):
        self.uart.close()

# Unit Test
if __name__ == '__main__':
    try:
        # Open uart
        rs232 = Uart(port='COM1', baud=115200)
        # Send test command
        rs232.send('Unit-test for Class Uart()\n'.encode(encoding='utf-8'))
        # Close uart
        rs232.close()
    except Exception as err:
        print('Error: {}'.format(err))