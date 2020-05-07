import Augmentor

p = Augmentor.Pipeline("images") #initialized_the_source_directory_for_images

#rotating_images
p.rotate(probability=0.7, max_left_rotation=10, max_right_rotation=10)
p.rotate90(probability=0.3)
p.rotate180(probability=0.8)#rotate_by_a_certain_degree
p.rotate270(probability=0.8)


#zooming_images
p.zoom(probability=0.5, min_factor=1.1, max_factor=1.5)

#skewing_images
p.skew_tilt(probability=0.6, magnitude=0.7)
p.skew(probability=0.6, magnitude=0.5)  #random_skewing

#flipping operations
p.flip_left_right(probability=0.7)
p.flip_top_bottom(probability=0.8)
p.flip_random(probability=0.5)


p.sample(100) #how_much_images_we_want_to_generate
p.process() #if the process gets slow use multi_threaded = False as a parameter here