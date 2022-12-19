from ursina import *
app=Ursina
me=Animation('assets\player',
Collider='box',y=5
)
Sky(
    window.bgcolor('red')
)
camera.orthographic=True
camera.fov=20
name=Sky
model='sky_demo'
Entity(
    model='quad',
    Texture='assets\BG',
    scale=36,z=1
)
app.run()