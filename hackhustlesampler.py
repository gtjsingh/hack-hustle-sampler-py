"""
    hackhustlesampler.py
    Hack & Hustle Academy Sampler
    Authored by Gurtej Singh
    Created on July 7, 2017
    Python Version 3.6
"""

import pygame
import json
import constants as const

# updates active sound kit
def update_sounds(sound_kit):
	
	# start with empty dictionary
	updated_sounds = {}

	# root path for each sound's filename
	root_path = sound_kit[const.ROOT_PATH]

	# key_samples is a dictionary
	# key: keyboard input, value: sound filename
	key_samples = sound_kit[const.KEY_SAMPLES]
	
	# iterate, each key is a character, ex. "s"
	for char in key_samples.keys():

		sound_file_name = key_samples[char]			
		
		# get the pygame constant number for keyboard input
		pygame_const = const.PYGAME_CONST_FOR_CHAR[char]			
		
		# check if file name retrieved is a string
		if isinstance(sound_file_name, str):
			# get complete file name path
			full_path = root_path + sound_file_name

			# create sound and add to dictionary
			# key: pygame constant associated with keyboard input
			# value: the appropriate pygame Sound object
			updated_sounds[pygame_const] = pygame.mixer.Sound(file=full_path)

		# check if file name retrieved is a list
		# if so, one key input will trigger multiple sounds at once	
		elif isinstance(sound_file_name, list):
			multiple_sounds = []
			
			# iterate through list of file names
			for file_name in sound_file_name:
				full_path = root_path + file_name
				# building array of sounds before adding to dictionary
				multiple_sounds.append(pygame.mixer.Sound(file=full_path))

			# add array of pygame Sounds as dictionary value
			updated_sounds[pygame_const] = multiple_sounds

	return updated_sounds

# retrieve file names dictionary 
# for associated sound kit dictionary
def get_file_names(sound_kit):
	
	# start with empty dictionary
	file_names = {}

	key_samples = sound_kit[const.KEY_SAMPLES]

	# similar iteration logic as update_sounds function
	for char in key_samples.keys():
		pygame_const = const.PYGAME_CONST_FOR_CHAR[char]
		file_name = key_samples[char]
		if isinstance(file_name, list):
			multiple_file_names = []
			for name in file_name:
				split_file_name = name.split(".")
				multiple_file_names.append(split_file_name[0])
			file_names[pygame_const] = multiple_file_names
		else:
			# file name may have extension at end, ex. "sound.wav"
			# remove file extension to get simple name, ex. "sound"
			split_file_name = file_name.split(".")
			file_names[pygame_const] = split_file_name[0]

	return file_names

def main():

	# initialize pygame
	pygame.mixer.pre_init(44100, -16, 1, 512)
	pygame.init()
	
	# parse configs from json
	with open("config.json") as json_data:
		configs = json.load(json_data)
		sound_kits = configs[const.SOUND_KITS]
	
	# setting a small black screen for display 
	screen = pygame.display.set_mode((100, 100))

	# default sound kit before any options selected
	default_sound_kit = sound_kits[const.ROLAND_TR_808]
	sounds = update_sounds(default_sound_kit)
	file_names = get_file_names(default_sound_kit)

	# loop runs continuously until is_running set to False
	is_running = True
	while is_running:
		# retrieves all pygame events and removes from event queue
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				print("Quitting program...")
				is_running = False				
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					print("Quitting program...")
					is_running = False
				elif event.key == pygame.K_1:
					print(const.ROLAND_TR_808 + " sound kit selected...")
					sound_kit = sound_kits[const.ROLAND_TR_808]
					sounds = update_sounds(sound_kit)
					file_names = get_file_names(sound_kit)
				elif event.key in sounds:
					selected_sound = sounds[event.key]
					# plays multiples sounds at once
					if isinstance(selected_sound, list):
						for sound in selected_sound:
							sound.stop()
							sound.play()
					else:
						# making sure sound not actively playing
						selected_sound.stop()
						# right before playing the sound again
						selected_sound.play()

					# print associated file name in console
					if event.key in file_names:
						print(file_names[event.key])

				else:
					print("Key not recognized...")

# main and helper functions definitions above
# program actually executes main function below
main()