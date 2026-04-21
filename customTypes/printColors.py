class bcolors:
	OKBLUE = "\033[94m"
	OKCYAN = "\033[96m"
	OKGREEN = "\033[92m"
	WARNING = "\033[93m"
	ERROR = "\033[91m"
	ENDC = "\033[0m"


def colorText(text: str, color: str):
	return color + text + bcolors.ENDC
