import arcade

Ancho_V = 1000
Alto_V  = 500
Titulo  = "Mario_Bros_Basico"


Jugador_Es  = 0.17
Suelo_Es    = 0.20
Cilindro_Es = 0.20
#Constante para escalar las ventanas y sprites



class MiJuego(arcade.Window):
#arcade.Window Permite  dibujar o crear la ventana en la pantalla
	
	
	def __init__(self):
		super().__init__(Ancho_V,Alto_V,Titulo)
		#Esta función nos permite invocar y conservar un método o atributo de una clase sin tener que nombrarla
	
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
		
	def on_draw(self):
		arcade.start_render()
		self.Jugador_list.draw()
		self.Piso_list.draw()
		#Dibuja lo de setup
	
	
def main():
	window = MiJuego()
	window.setup()
	arcade.run()
	
	
if __name__ == "__main__":
	main()