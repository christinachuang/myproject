import pickle

number_of_image = 50
sorted_sim = []
#load file from disk
with open ('outfile', 'rb') as fp:
    sorted_sim = pickle.load(fp)
	
#find the similar image
rec_clothes = []
chosen_images = []
chosen_images.append(20) #6
chosen_images.append(35) #20
for k in range(len(chosen_images)):
	chosen_img = chosen_images[k]
	recommand_num = 4 #decide how many images to recommand
	for i in range(4):
		im_num = sorted_sim[chosen_img][i][1]
		rec_clothes.append(sorted_sim[chosen_img][i][1])
	print("cloth %d" %chosen_img)
	print(rec_clothes)




