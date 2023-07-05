import pygame
from glob import glob
import os
import time

surf = pygame.display.set_mode((576, 384))
pathSep = os.path.join("e", "e").replace("e", "")
blockDict = {}
blockNum = None
for blockPath in glob(f"blocks{pathSep}*"):
	block = blockPath.split(".")[0].split(pathSep)[1]
	blockNum = ""
	for char in block:
		blockNum += char
	while not (blockNum.isdigit() or blockNum == ""):
		blockNum = list(blockNum)
		blockNum.pop(0)
		blockNum = "".join(blockNum)
	if blockNum == "":
		continue
	if not block.replace(blockNum, "") in list(blockDict.keys()):
		blockDict.update({block.replace(blockNum, ""): {int(blockNum): pygame.image.load(blockPath)}})
	else:
		blockDict[block.replace(blockNum, "")].update({int(blockNum): pygame.image.load(blockPath)})
print(blockDict)
pygame.display.set_icon(blockDict["flipper"][0])
verStr = "0.beta1"
pygame.display.set_caption(" ".join(["Machinic", verStr]), " ".join(["Machinic", verStr]))
running = True
selInd = 0
showBlks = 8
blkHold = None

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				if selInd != 0:
					selInd -= 1
				continue
			if event.key == pygame.K_RIGHT:
				if selInd != len(list(blockDict.keys())) - 1:
					selInd += 1
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mousePos = event.pos
			xCount = 0
			blkCount = selInd
			while blkCount not in [selInd + showBlks, len(list(blockDict.keys()))]:
				#surf.blit(blockDict[list(blockDict.keys())[blkCount]][0], (8 + xCount * 40, 8))
				if (mousePos[0] > 7 + xCount * 40 and mousePos[0] < (8 + xCount * 40) + 32) and mousePos[1] >= 8 and mousePos[1] < 40:
					print("+----+")
					blkHold = blkCount
					break
				xCount += 1
				blkCount += 1
		elif event.type == pygame.MOUSEBUTTONUP:
			if str(blkHold) != "None":
				print("+----+")
			blkHold = None
	if str(blkHold) != "None":
		print(blkHold)
	surf.fill("White")
	xCount = 0
	blkCount = selInd
	while blkCount not in [selInd + showBlks, len(list(blockDict.keys()))]:
		surf.blit(blockDict[list(blockDict.keys())[blkCount]][0], (8 + xCount * 40, 8))
		xCount += 1
		blkCount += 1
	pygame.display.update()