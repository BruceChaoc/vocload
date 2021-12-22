import os
from PIL import Image, ImageDraw
from lxml import etree

xmlLists = os.listdir("data_set/train/ANNOTATIONS")

for xmlList in xmlLists:
    # imName = xmlList.split(".", -1)[0]
    with open(os.path.join("data_set/train/ANNOTATIONS/", xmlList)) as xml:
        imObjName = []
        imObjBndbox = []
        imXml = etree.parse(xml)
        # print(etree.tostring(imXml, pretty_print=True))
        imFileName = imXml.xpath("./filename/text()")[0]
        imXmlObjs = imXml.xpath("//object")
        with Image.open(os.path.join("data_set/train/IMAGES/", imFileName)) as im:
            drawR = ImageDraw.ImageDraw(im)
            for imXmlObj in imXmlObjs:
                imObjName.append(imXmlObj.xpath("./name/text()"))
                imObjBndbox=[int(imXmlObj.xpath(".//xmin/text()")[0]),
                             int(imXmlObj.xpath(".//ymin/text()")[0]),
                             int(imXmlObj.xpath(".//xmax/text()")[0]),
                             int(imXmlObj.xpath(".//ymax/text()")[0])]
                drawR.rectangle((imObjBndbox[0], imObjBndbox[1]),
                                (imObjBndbox[2], imObjBndbox[3]),
                                fill=None, outline='red', width=1)
                im.show()
            im.save("drawR/train/IMAGES/0.jpg")
            pass

