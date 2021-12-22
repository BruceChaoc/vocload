import os
from PIL import Image, ImageDraw, ImageFont
from lxml import etree

fnt = ImageFont.truetype("simhei.ttf", 10)
xmlLists = os.listdir("data_set/train/ANNOTATIONS")
colorSelect = {'rolled-in_scale': 0xff0000,
               'patches': 0x00ff00,
               'crazing': 0x0000ff,
               'pitted_surface': 0xee00ee,
               'inclusion': 0x00eeee,
               'scratches': 0xeeee00}

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
                imObjName = imXmlObj.xpath("./name/text()")[0]
                imObjBndbox=[int(imXmlObj.xpath(".//xmin/text()")[0]),
                             int(imXmlObj.xpath(".//ymin/text()")[0]),
                             int(imXmlObj.xpath(".//xmax/text()")[0]),
                             int(imXmlObj.xpath(".//ymax/text()")[0])]
                drawR.rectangle(imObjBndbox, fill=None, outline=colorSelect[imObjName], width=1)
                drawR.text((imObjBndbox[0], imObjBndbox[1]), imObjName, font=fnt, fill=colorSelect[imObjName])
                im.save(os.path.join("drawR/train/IMAGES/", imFileName))

