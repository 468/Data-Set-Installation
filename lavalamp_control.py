from tplink_smartplug import SmartPlug

lamp = SmartPlug('0.0.0.0')

def turn_on_lavalamp():
	try:
		lamp.turn_on()
	except:
		print('Failed to turn lava lamp on')


def turn_off_lavalamp():
	try:
		lamp.turn_off()
	except:
		print('Failed to turn lava lamp off')