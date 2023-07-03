import pygame
from glob import glob

surf = pygame.display.set_mode((384, 256))
blockDict = {}
blockNum = None
for blockPath in glob("blocks/*"):
	block = blockPath.split(".")[0].split("/")[1]
	blockNum = ""
	for char in block:
		blockNum += char
	while not blockNum.isdigit():
		blockNum = list(blockNum)
		print(blockNum)
		blockNum.pop(0)
		blockNum = "".join(blockNum)
	if not block.replace(blockNum, "") in list(blockDict.keys()):
		blockDict.update({block.replace(blockNum, ""): {int(blockNum): pygame.image.load(blockPath)}})
	else:
		blockDict[block.replace(blockNum, "")].update({int(blockNum): pygame.image.load(blockPath)})
print(blockDict)
pygame.display.set_icon(blockDict["flipper"][0])
verStr = "0.beta1"
pygame.display.set_caption(" ".join(["Machinic", verStr]), " ".join(["Machinic", verStr]))
running = True

while running:
	surf.fill("White")
	pygame.display.update()