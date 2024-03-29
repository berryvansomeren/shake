import sys
sys.path.append( "C:/Users/Berry/Documents/development/shake/build/" )
import pyshake
from pyshake.content import Path
from pyshake.core import (
    log,
    Transform2D,
    Transform3D,
    Vec2
)
from pyshake.graphics import (
    draw,
    make_circle_filled_2D,
    Material,
    RenderPack2D
)
from pyshake.hid import Keyboard


class Game:
    #----------------------------------------------------------------
    def __init__( self ):
        self.width = 2560
        self.height = 1440
        self.application = pyshake.Application( 
            lambda      : self.init(),
            lambda dt   : self.update( dt ),
            lambda      : self.draw(),
            lambda      : self.destroy(),
            self.width, 
            self.height,
            "Pyshake Demo Game"
        )

    #----------------------------------------------------------------
    def run( self ) -> None:
        self.application.run()

    #----------------------------------------------------------------
    def init( self ) -> None:
        log( "Game Start" )
        content_manager = self.application.content_manager()
        content_manager.host_content_directory( Path( "C:/Users/Berry/Documents/development/shake/shake_test_game/" ) )
        main_shader = content_manager.get_or_load__Program( Path( "shaders/default_primitive_2d_shader.glsl" ) )
        main_material = Material( main_shader )
        main_geometry = make_circle_filled_2D( 0.5 )
        self.render_pack = RenderPack2D( main_geometry, main_material )
        self.transform = Transform2D()

    #----------------------------------------------------------------
    def update( self, dt : float ) -> None:

        if Keyboard.is_down( Keyboard.Key.Escape ):
            self.application.close()

        v = dt * 0.001
        translations = [
            ( Keyboard.Key.W, Vec2(  0,  -v ) ),
            ( Keyboard.Key.S, Vec2(  0,   v ) ),
            ( Keyboard.Key.A, Vec2( -v,   0 ) ),
            ( Keyboard.Key.D, Vec2(  v,   0 ) ),
        ]

        for key, translation_vector in translations:
             if Keyboard.is_down( key ):
                 self.transform.translate( translation_vector )
        pass

    #----------------------------------------------------------------
    def draw( self ) -> None:
        #self.render_pack.material.set_uniform( "camera_transform", self.camera_transform )
        draw( self.render_pack, self.transform )
        pass

    #----------------------------------------------------------------
    def destroy( self ) -> None:
        log( "Game Exit" )
        pass


#----------------------------------------------------------------
if __name__ == "__main__":
    game = Game()
    game.run()