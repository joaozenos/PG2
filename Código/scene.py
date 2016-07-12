#flake8:noqa


camera = None
zbuffer = None
buffer_t = None

def scene(camera):
	global camera, buffer_t,zbuffer
	
	camera = camera
	buffer_t = None
	zbuffer = None

def get_camera():
	global camera
	return camera

def set_buffer(w, h):
	global buffer_t

	if buffer_t is not None:
		delete[] buffer;
	
	if zbuffer is not None:
		delete[] zbuffer;

	value = 3*w*h
	i = 0
	buffer_t = []

	while (i < value):
		buffer[i + 0] = 1.0f;
		buffer[i + 1] = 0.0f;
		buffer[i + 2] = 0.0f;
		i = i + 3
	
	zbuffer = []
	for(int i = 0; i < w * h; ++i)
		zbuffer[i] = FLT_MAX;
}
