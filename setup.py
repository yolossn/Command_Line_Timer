from setuptools import setup

setup(
	name="timer",
	description="terminal timer",
	author="yolossn",
	author_email="nssvlr@gmail.com",
	license="MIT",
	keywords=["timer"],
	scripts=["timer"],
	data_files=[("mp3",["beep_beep_beep_alarm.mp3"])],
	zip_safe=False
)
