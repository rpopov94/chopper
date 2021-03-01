import fw_status
import chopper


def get_data(name):
    chopper.connect(name)
    chopper.smc32_command(0, 0, 'R', 0)
    response = chopper.smc32response()[11:15].decode("utf-8")
    data = int('0x'+response, 16)
    return data


h = get_data("COM4")
print(h)
st = fw_status.Status(h)
r = st.get_response()
print(st.get_status(r))