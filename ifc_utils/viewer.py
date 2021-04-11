class Viewer:

    
    def __init__(self, file, elements):
        import k3d
        import ifcopenshell
        import ifcopenshell.geom
        
        self.file = file
        self.elements = elements
        # Set renderer
        self.settings = ifcopenshell.geom.settings()
        self.settings.set(self.settings.USE_WORLD_COORDS, True)
        self.plot = k3d.plot()

    def close(self):
        if self.plot:
            self.plot.close()
            
    def display(self):
        import ifcopenshell
        import ifcopenshell.geom
        import k3d

        for product in self.file.by_type('IfcProduct'):
            if product.is_a('IfcOpeningElement') or product.is_a('IfcSpace'): continue
            if product.Representation :  
                # Change color of selected elements   
                if product in self.elements:
                    opacidade = 1.0
                    cor = 0xdd2779
                else:
                    opacidade = 0.15
                    cor = 0xc0aec 
                # Create shape
                shape = ifcopenshell.geom.create_shape(self.settings, product)
                vertices = shape.geometry.verts
                faces = shape.geometry.faces

                # Add meshes
                self.plot += k3d.mesh(vertices, faces, opacity=opacidade, color=cor)        

        # Render
        self.plot.mode='Change'
        self.plot.camera_mode='orbit'
        self.plot.display()