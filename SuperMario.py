import traceback
import arcade


Ancho_V = 1000
Alto_V  = 500
Titulo  = "Mario_Bros_Basico"


Jugador_Es  = 0.17
Suelo_Es    = 0.20
Cilindro_Es = 0.20
#Constante para escalar las ventanas y sprites

Jugador_Velocidad = 5
Greavedad = 1
Salto_Del_Jugador = 20
#Velocidad del jugador 

class MiJuego(arcade.Window):
#arcade.Window Permite  dibujar o crear la ventana en la pantalla
        
        
        def __init__(self):
                super().__init__(Ancho_V,Alto_V,Titulo)
                #Esta funcion nos permite invocar y conservar un metodo o atributo de una clase sin tener que nombrarla
        
                arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
                #Color
                
                self.Jugador_list = None
                self.Moneda_list  = None
                self.Piso_list    = None
                #Listas que contendran nuestros sprites
                
                self.Jugador_sprite = None
                #Variable del sprite jugador
                
                
                
        
        def setup(self):
        #Inicializo nuestras listas
                self.Jugador_list = arcade.SpriteList()
                self.Piso_list    = arcade.SpriteList()
                self.Moneda_list  = arcade.SpriteList()
                #Inicializo como un objeto spritelist
                
                
                
                
                image_source = "mario.png"
                self.Jugador_sprite = arcade.Sprite(image_source,Jugador_Es)
                self.Jugador_sprite.center_x = 64
                self.Jugador_sprite.center_y = 93
                self.Jugador_list.append(self.Jugador_sprite)
                #Cree al jugador
                
                
                for x in range(0,1250,64):
                        Piso = arcade.Sprite("ground.png",Suelo_Es)
                        Piso.center_x = x 
                        Piso.center_y = 32
                        self.Piso_list.append(Piso)
                        #Cree el piso
                        
                coordenadas_lista = [[512,110],[256,110],[768,110]]     
                #Creo cordenadas de aparicion   
                
                
                for coordenada in coordenadas_lista:
                        Piso = arcade.Sprite("cylinder.png" , Cilindro_Es)
                        Piso.position = coordenada
                        self.Piso_list.append(Piso)
                #Para hacer que aparezca el cilindro en el piso
                
                
                
                self.physics_engine = arcade.PhysicsEnginePlatformer(self.Jugador_sprite,self.Piso_list ,Greavedad)
				#fisicas al jugador
                
                
        def on_draw(self):
                arcade.start_render()
                self.Jugador_list.draw()
                self.Piso_list.draw()
                #Dibuja lo de setup
                
                
                
        def on_key_press(self , key , modifiers):
            if key == arcade.key.UP:
                if self.physics_engine.can_jump():
                    self.Jugador_sprite.change_y = Salto_Del_Jugador

        
            elif key == arcade.key.LEFT:
                self.Jugador_sprite.change_x = -Jugador_Velocidad
        
            elif key == arcade.key.RIGHT:
                self.Jugador_sprite.change_x =  Jugador_Velocidad
                        
        #Detecto pulsasiones o tecla que presione
        
        
        def on_key_release(self , key , modifiers):
                
            if key == arcade.key.LEFT:
                self.Jugador_sprite.change_x = 0
        
            elif key == arcade.key.RIGHT:
                self.Jugador_sprite.change_x = 0
        #Para que pare sino se presiona 

        def on_update(self , delta_time):
               self.physics_engine.update()
			   #actualizacion de fisicas
                
        
        
        
def main():
        window = MiJuego()
        window.setup()
        arcade.run()
        
        
if __name__ == "__main__":
        main()
