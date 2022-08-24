import uuid

screenshot = 'screenshots/{0}.png'
print(type(screenshot.format(str(uuid.uuid4().hex))))
print(screenshot.format(str(uuid.uuid4().hex)))