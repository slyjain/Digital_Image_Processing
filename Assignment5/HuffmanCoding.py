# Learned about heapq and collections and pillow
import heapq
from collections import defaultdict,Counter
from PIL import Image
# How to read image in Pillow
img =Image.open("./image.png")
def grayScaleImage(img):
    # Easy method to convert to grayscale
    img=img.convert("L")
    return img
img=grayScaleImage(img)
pixels=list(img.getdata())
# print(pixels)
freq=Counter(pixels)
print(len(freq))
class HuffmanNode:
    def __init__ (self,frequency,symbol=None,left=None,right=None):
        self.frequency=frequency
        self.symbol=symbol
        self.left=left
        self.right=right
    def __lt__(self,other):
        return self.frequency<other.frequency
priority_queue=[]
for symbol,frequency in freq.items():
    heapq.heappush(priority_queue,HuffmanNode(frequency,symbol))

while(len(priority_queue)>1):
    node1=heapq.heappop(priority_queue)
    node2=heapq.heappop(priority_queue)
    merged=HuffmanNode(node1.frequency+node2.frequency,left=node1,right=node2)
    heapq.heappush(priority_queue,merged)
huffmanTreeRoot=heapq.heappop(priority_queue)
def generateHuffmanCodes(node,code="",huffmanCodes={}):
    if node is None:
        return
    #leafNode 
    if node.symbol is not None:
        huffmanCodes[node.symbol]=code
    #traverse the left and right children
    generateHuffmanCodes(node.left,code+"0",huffmanCodes)
    generateHuffmanCodes(node.right,code+"1",huffmanCodes)
    return huffmanCodes
huffmanCodes=generateHuffmanCodes(huffmanTreeRoot)
print(huffmanCodes)
encodedImage=''.join(huffmanCodes[pixel] for pixel in pixels)
print(encodedImage[:50])
def decodeHuffman(encodedData,huffmanTreeRoot):
    decodedPixels=[]
    node= huffmanTreeRoot
    for bit in encodedData:
        if bit=='0':
            node=node.left
        else:
            node=node.right
        if node.symbol is not None:
            decodedPixels.append(node.symbol)
            node=huffmanTreeRoot
    return decodedPixels
decodedPixels=decodeHuffman(encodedImage,huffmanTreeRoot)
decodedImage=Image.new('L',img.size)
decodedImage.putdata(decodedPixels)
decodedImage.save('decodedImage.png')