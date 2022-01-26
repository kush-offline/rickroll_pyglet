import pyglet
def loop():
        width = 680
        height = 360

        title = "rick rolled"

        window = pyglet.window.Window(width, height, title)
        path= r"icon.ico"
        icon = pyglet.image.load(path)
        window.set_icon(icon)
        vp =r"wifu_hot.mp4"

        player = pyglet.media.Player()

        MediaLoad = pyglet.media.load(vp)

        player.queue(MediaLoad)

        player.play()

        @window.event
        def on_draw():
            if player.source and player.source.video_format:
                player.get_texture().blit(0,0)
        @window.event
        def on_close():
            loop()
        @window.event
        def on_key_press(symbol, modifier):
            if symbol == pyglet.window.key.K:
                window.close()    

        # run the pyglet application
        pyglet.app.run()

loop()
