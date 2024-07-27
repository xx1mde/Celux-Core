def hex_to_rgba(hex_color: str, err_handler: object = None):
	if len(hex_color) == 8:
		try: return tuple([round(float(int(hex_color[x:x+2], 16) / 255), 5) for x in range(0, 8, 2)])
		except Exception:
			if err_handler: err_handler("Invalid argument at index 1. The color must have 8 positions, each of which is a hexadecimal digit")
			return (0, 0, 0, 0)
	else:
		if err_handler: err_handler("Invalid argument at index 1. The color must have 8 positions, each of which is a hexadecimal digit")
		return (0, 0, 0, 0)