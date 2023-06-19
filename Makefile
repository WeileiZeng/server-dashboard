serve:
	docker run -it --rm -p 8080:8080 \
 -v "${PWD}/home":/app zauberzeug/nicegui
